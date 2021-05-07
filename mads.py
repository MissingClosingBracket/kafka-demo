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

#producer = KafkaProducer(bootstrap_servers=['0.0.0.0:9092'],
                         #value_serializer=json_serializer)


#define gRPC calls:
class Listener(mads_pb2_grpc.mads_serviceServicer):
    def userCreateObject(self, request, context):
        uri = request.URI
        print("Server received: " + uri)
        return mads_pb2.UserCreateObjectResponse(object = mads_pb2.Object(id = 1, URI = uri))

#define server:
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    mads_pb2_grpc.add_mads_serviceServicer_to_server(Listener(), server)
    server.add_insecure_port("[::]:9999")
    server.start()
    try:
        while True:
            print("Server Running : threadcount %i" % (threading.active_count()))
            time.sleep(10)
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        server.stop(0)


if __name__ == "__main__":
    serve()





        
    #data = {"message": message}
    #producer.send(topic, data)
    #producer.send("all",data)