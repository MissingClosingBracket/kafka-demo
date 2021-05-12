from kafka import KafkaConsumer
import json
import time
import grpc

import mads_pb2
import mads_pb2_grpc

if __name__ == "__main__":

    def translateDescription(description):
        return "To personer i skoven."

    consumer = KafkaConsumer(
        "event_auto_description_created",
        bootstrap_servers='0.0.0.0:9092',
        auto_offset_reset='latest',
        group_id="translate-1")
    print("Starting the consumer: plugin_translate_description")
    for msg in consumer:
        print("--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--")
        print("Translating descritpion for an automatically created description. The event had the message = {}".format(json.loads(msg.value)))

        with grpc.insecure_channel("localhost:9999") as channel:
            stub = mads_pb2_grpc.mads_serviceStub(channel)
            try:
                objid = int(json.loads(msg.value)['oid'])
                descr = str(json.loads(msg.value)['description'])
                #create translated description for object:
                translated_description = translateDescription(descr)
                response = stub.pluginTranslateDescription(mads_pb2.PluginTranslateDescriptionRequest(oid = objid, description = translated_description))
                print("I just received a response on translating a description: ")
                print(response)
                print("")
                channel.unsubscribe(channel.unsubscribe)
                #

            except KeyboardInterrupt:
                print("KeyboardInterrupt")
                channel.unsubscribe(channel.unsubscribe)
                exit()