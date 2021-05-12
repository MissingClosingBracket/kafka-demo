from kafka import KafkaConsumer
import json
import time
import grpc

import mads_pb2
import mads_pb2_grpc

if __name__ == "__main__":

    def getGeodata(lat, lon):
        return "DR Congo, Bumba"

    consumer = KafkaConsumer(
        "event_exif_data_extracted",
        bootstrap_servers='0.0.0.0:9092',
        auto_offset_reset='latest',
        group_id="geodata-1")
    print("Starting the consumer: plugin_supply_geodata")
    for msg in consumer:
        print("--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--")
        print("Supplying with additional geodata. The event had the message = {}".format(json.loads(msg.value)))

        with grpc.insecure_channel("localhost:9999") as channel:
            stub = mads_pb2_grpc.mads_serviceStub(channel)
            try:
                objid = int(json.loads(msg.value)['oid'])
                lat = float(json.loads(msg.value)['latitude'])
                lon = float(json.loads(msg.value)['longitude'])
                #supply additional geodata for object:
                data = getGeodata(lat, lon)
                response = stub.pluginSupplyGeodata(mads_pb2.PluginSupplyGeodataRequest(oid = objid, geodata = data))
                print("I just received a response on supplying geodata: ")
                print(response)
                print("")
                channel.unsubscribe(channel.unsubscribe)
                #

            except KeyboardInterrupt:
                print("KeyboardInterrupt")
                channel.unsubscribe(channel.unsubscribe)
                exit()