from kafka import KafkaConsumer
import json
import time
import grpc

import mads_pb2
import mads_pb2_grpc

if __name__ == "__main__":

    def extractEXIF(uri):
        return [2.34324, 23.02423]

    consumer = KafkaConsumer(
        "event_new_object",
        bootstrap_servers='0.0.0.0:9092',
        auto_offset_reset='latest',
        group_id="exif-1")
    print("Starting the consumer: plugin_extract_exif_data")
    for msg in consumer:
        print("--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--")
        print("Extracting EXIF data from an object. The event had the message = {}".format(json.loads(msg.value)))

        with grpc.insecure_channel("localhost:9999") as channel:
            stub = mads_pb2_grpc.mads_serviceStub(channel)
            try:
                objid = int(json.loads(msg.value)['oid'])
                uri = json.loads(msg.value)['uri']
                #extract exif data from object:
                coords = extractEXIF(uri)                
                response = stub.pluginExtractExifData(mads_pb2.PluginExtractExifDataRequest(oid = objid, latitude = coords[0], longitude = coords[1]))
                print("I just received a response on extracting EXIF data from an object: ")
                print(response)
                print("")
                channel.unsubscribe(channel.unsubscribe)
                #

            except KeyboardInterrupt:
                print("KeyboardInterrupt")
                channel.unsubscribe(channel.unsubscribe)
                exit()

