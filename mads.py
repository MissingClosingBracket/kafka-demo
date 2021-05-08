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
object_table = {}                        #(oid, uri)         example: (1, "google.com/images/search=iceland+snow,top=1")    (int, varchar)
tag_set_table = {}                       #(oid, tsid)        example: (1,2)                                                 (int, int)
tag_table = {}                           #(tid, tsid)        example: (23, 2)                                               (int, int)
exif_tag_table = {}                      #(tid, coord)       example: (23, "12.3433535, 34.3429385")                        (int, varchar)
description_tag_table = {}               #(tid, descr)       example: (24, "Three people in the woods") (auto-generated)    (int, varchar)
translated_description_tag_table = {}    #(tid, descr)       example: (24, "Tveir menn ganga í skóginum.") (auto-generated) (int, varchar)
geodata_tag_table = {}                   #(tid, descr)       example: (25, "Vexö, Sverige. Malleby Forest.")                (int, varchar)

#entries in database:
object_table[0] = 0
tag_set_table[0] = 0
tag_table[0] = 0



#define different kafka events and topics:
def kafka_event(topic, message):
    producer.send(topic, message)
    message["topic"] = topic
    producer.send("event_all", message)

#define gRPC calls:
class Listener(mads_pb2_grpc.mads_serviceServicer):
    
    #increase index in object table and tagset table when new object gets added. 
    def userCreateObject(self, request, context):
        uri = request.URI
        print("Server received new object: " + uri)
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
        print("Server received description for the object: oid = " + str(oid) + " with the URI = " + uri + ". The description is: " + descr)
        tsid = tag_set_table[oid]
        tid = len(tag_table) 
        tag_table[tid] = tsid
        description_tag_table[tid] = descr
        kafka_event("event_auto_description_created", {"oid":oid, "tid":tid, "description":descr})
        return mads_pb2.PluginCreateDescriptionResponse(tag = mads_pb2.Tag(tid = tid))

    #the plugin for translating an automatically created description into the language of the user when reading the event: event_auto_description_created.
    def pluginTranslateDescription(self, request, context):
        oid = request.oid
        descr = request.description
        print("Server received a translated description for the object: oid = " + str(oid) + ". The translated description is: " + descr) 
        tsid = tag_set_table[oid]
        tid = len(tag_table)
        tag_table[tid] = tsid
        translated_description_tag_table[tid] = descr
        kafka_event("event_translated_auto_description", {"oid":oid, "tid":tid, "description":descr})
        return mads_pb2.PluginTranslateDescriptionResponse(tag = mads_pb2.Tag(tid = tid))

    #the plugin for extracting exif data from an object.
    def pluginExtractExifData(self, request, context):
        oid = request.oid
        lat = request.latitude
        lon = request.longitude
        print("Server received extracted EXIF data from the object: oid = " + str(oid) + ". The latitude and longitude (lat, long) is: (" + str(lat) + ", " + str(lon) + ").")   
        tsid = tag_set_table[oid]
        tid = len(tag_table)
        tag_table[tid] = tsid
        exif_tag_table[tid] = [lat,lon]
        kafka_event("event_exif_data_extracted", {"oid":oid, "tid":tid, "latitude":lat, "longitude":lon})
        return mads_pb2.PluginExtractExifDataResponse(tag = mads_pb2.Tag(tid = tid))

    #the plugin that supplies additional geodate when reading event: event_exif_data_extracted.
    def pluginSupplyGeodata(self, request, context):
        oid = request.oid
        geodata = request.geodata
        print("Server received additional geodata for the object: oid = " + str(oid) + ". The geodata received is: " + geodata)    
        tsid = tag_set_table[oid]
        tid = len(tag_table)
        tag_table[tid] = tsid
        geodata_tag_table[tid] = geodata
        kafka_event("event_geodata_supplied", {"oid":oid, "tid":tid, "geodata":geodata})
        return mads_pb2.PluginSupplyGeodataResponse(tag = mads_pb2.Tag(tid = tid))

#define server:
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mads_pb2_grpc.add_mads_serviceServicer_to_server(Listener(), server)
    server.add_insecure_port("[::]:9999")
    server.start()
    try:
        while True:
            print("Server Running : threadcount %i" % (threading.active_count()))
            time.sleep(30)
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        server.stop(0)


if __name__ == "__main__":
    serve()


