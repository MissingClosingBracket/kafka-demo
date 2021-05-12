from kafka import KafkaConsumer
import json
import time
import grpc

import mads_pb2
import mads_pb2_grpc

if __name__ == "__main__":

    #simulate call to aut. image annotation
    def getDescription(uri):
        return "Two people in the woods"

    consumer = KafkaConsumer(
        "event_new_object",
        bootstrap_servers='0.0.0.0:9092',
        auto_offset_reset='latest',
        group_id="description-1")
    print("Starting the consumer: plugin_create_automatic_description")
    for msg in consumer:
        print("--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--")
        print("Creating descritpion for an object. The event had the message = {}".format(json.loads(msg.value)))

        with grpc.insecure_channel("localhost:9999") as channel:
            stub = mads_pb2_grpc.mads_serviceStub(channel)
            try:
                objid = int(json.loads(msg.value)['oid'])
                uri = json.loads(msg.value)['uri']
                #create description for object:
                auto_description = getDescription(uri)
                response = stub.pluginCreateDescription(mads_pb2.PluginCreateDescriptionRequest(oid = objid, description = auto_description))
                print("I just received a response on adding a description to an object: ")
                print(response)
                print("")
                channel.unsubscribe(channel.unsubscribe)
                #

            except KeyboardInterrupt:
                print("KeyboardInterrupt")
                channel.unsubscribe(channel.unsubscribe)
                exit()

