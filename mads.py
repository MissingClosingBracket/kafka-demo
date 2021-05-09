from kafka import KafkaProducer
import json
import grpc
import mads_pb2_grpc
import mads_pb2
from concurrent import futures
import threading
import time


#define function json_serializer and create kafka producer:
def json_serializer(data):
    return json.dumps(data).encode("utf-8")

producer = KafkaProducer(bootstrap_servers=['0.0.0.0:9092'],
                         value_serializer=json_serializer)

#initialize database representation:
object_table = {}                        #(oid, uri)                                  example: (1, "google.com/images/search=iceland+snow,top=1")                     
tag_set_table = {}                       #(oid, tsid)                                 example: (1, 2)                                                                  
tag_to_tagset_table = {}                 #(tid, tsid)                                 example: (23, 2)                                                                
tag_table = {}                           #(tid, [type, coord/descr/descr/geodata])    example: (23, ["exif", "12.3433535, 34.3429385"])                                    

#entries in database:
object_table[0] = 0
tag_set_table[0] = 0
tag_to_tagset_table[0] = 0
tag_table[0] = ["",""]



#define different kafka events and topics:
def kafka_event(topic, message):
    producer.send(topic, message)
    message["topic"] = topic
    producer.send("event_all", message)

#get tags bu object id:
def getTagsByOID(oid):
    if oid >= len(object_table) or oid == 0:
        return []
    else:    
        lst = []
        tsid = tag_set_table[oid]
        for key, value in tag_to_tagset_table.items():
            if value == tsid:
                lst.append(key)
        return lst

#define gRPC calls:
class Listener(mads_pb2_grpc.mads_serviceServicer):
    
    #increase index in object table and tagset table when new object gets added. 
    def userCreateObject(self, request, context):
        uri = request.URI
        print("--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--")
        print("Server received new object: " + uri)
        print("")
        oid = len(object_table) 
        tsid = len(tag_set_table) 
        object_table[oid] = uri
        tag_set_table[oid] = tsid
        kafka_event("event_newObject",{"oid":oid,"uri":uri})
        return mads_pb2.UserCreateObjectResponse(object = mads_pb2.Object(oid = oid, URI = uri))

    #the plugin for automatically creating a description to an object.     
    def pluginCreateDescription(self, request, context):
        oid = request.oid
        uri = request.URI
        descr = request.description
        print("--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--")
        print("Server received description for the object: oid = " + str(oid) + " with the URI = " + uri + ". The description is: " + descr)
        print("")
        tsid = tag_set_table[oid]
        tid = len(tag_table) 
        tag_to_tagset_table[tid] = tsid
        tag_table[tid] = ["descr", descr]
        kafka_event("event_auto_description_created", {"oid":oid, "tid":tid, "description":descr})
        return mads_pb2.PluginCreateDescriptionResponse(tag = mads_pb2.Tag(tid = tid, value = descr, type = mads_pb2.TagType.DESCR))

    #the plugin for translating an automatically created description into the language of the user when reading the event: event_auto_description_created.
    def pluginTranslateDescription(self, request, context):
        oid = request.oid
        descr = request.description
        print("--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--")
        print("Server received a translated description for the object: oid = " + str(oid) + ". The translated description is: " + descr) 
        print("")
        tsid = tag_set_table[oid]
        tid = len(tag_table)
        tag_to_tagset_table[tid] = tsid
        tag_table[tid] = ["transl_descr", descr]
        kafka_event("event_translated_auto_description", {"oid":oid, "tid":tid, "description":descr})
        return mads_pb2.PluginTranslateDescriptionResponse(tag = mads_pb2.Tag(tid = tid, value = descr, type = mads_pb2.TagType.TRANSL_DESCR))

    #the plugin for extracting exif data from an object.
    def pluginExtractExifData(self, request, context):
        oid = request.oid
        lat = request.latitude
        lon = request.longitude
        print("--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--")
        print("Server received extracted EXIF data from the object: oid = " + str(oid) + ". The latitude and longitude (lat, long) is: (" + str(lat) + ", " + str(lon) + ").")   
        print("")
        tsid = tag_set_table[oid]
        tid = len(tag_table)
        tag_to_tagset_table[tid] = tsid
        tag_table[tid] = ["exif", "(" + str(lat) + ", " + str(lon) + ")"]
        kafka_event("event_exif_data_extracted", {"oid":oid, "tid":tid, "latitude":lat, "longitude":lon})
        v = "(" + str(lat) + ", " + str(lon) + ")"
        return mads_pb2.PluginExtractExifDataResponse(tag = mads_pb2.Tag(tid = tid, value = v, type = mads_pb2.TagType.EXIFDATA))

    #the plugin that supplies additional geodate when reading event: event_exif_data_extracted.
    def pluginSupplyGeodata(self, request, context):
        oid = request.oid
        geodata = request.geodata
        print("--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--")
        print("Server received additional geodata for the object: oid = " + str(oid) + ". The geodata received is: " + geodata)    
        print("")
        tsid = tag_set_table[oid]
        tid = len(tag_table)
        tag_to_tagset_table[tid] = tsid
        tag_table[tid] = ["geodata", geodata]
        kafka_event("event_geodata_supplied", {"oid":oid, "tid":tid, "geodata":geodata})
        return mads_pb2.PluginSupplyGeodataResponse(tag = mads_pb2.Tag(tid = tid, value = geodata, type = mads_pb2.TagType.GEODATA))

    #the user/program wants to retrieve all tags associated with an object:
    def userRequestsTagsForObject(self, request, context):
        oid = request.oid
        kafka_event("user_requests_tags", {"oid":oid})
        print("--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--")
        print("Server received a request for giving the client all tags associated with the object: oid = " + str(oid) + ".")
        tags = getTagsByOID(oid)
        if (len(tags) == 0):
            print("  --Server has no tags to return because oid does not exist.")
            print("")
        else:
            for tagid in tags:
                elem1 = tag_table[tagid][0]
                elem2 = tag_table[tagid][1]
                print("  --Server is returning: " + str(elem1) + ", " + str(elem2) + ".")
                if (elem1=="geodata"):
                    yield mads_pb2.UserRequestsTagsForObjectResponse(tag = mads_pb2.Tag(tid = tagid, value = str(elem2), type = mads_pb2.TagType.GEODATA))
                elif (elem1=="exif"):
                    yield mads_pb2.UserRequestsTagsForObjectResponse(tag = mads_pb2.Tag(tid = tagid, value = str(elem2), type = mads_pb2.TagType.EXIFDATA))
                elif (elem1=="descr"):
                    yield mads_pb2.UserRequestsTagsForObjectResponse(tag = mads_pb2.Tag(tid = tagid, value = str(elem2), type = mads_pb2.TagType.DESCR))
                elif (elem1=="transl_descr"):
                    yield mads_pb2.UserRequestsTagsForObjectResponse(tag = mads_pb2.Tag(tid = tagid, value = str(elem2), type = mads_pb2.TagType.TRANSL_DESCR))    
            print("")
        
#define server:
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mads_pb2_grpc.add_mads_serviceServicer_to_server(Listener(), server)
    server.add_insecure_port("[::]:9999")
    server.start()
    try:
        while True:
            print("Server Running : threadcount %i" % (threading.active_count()))
            time.sleep(60)
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        server.stop(0)


if __name__ == "__main__":
    serve()


