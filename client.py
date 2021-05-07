import time
import grpc
import mads_pb2
import mads_pb2_grpc

#make client do a gRPC
def run():
    with grpc.insecure_channel("localhost:9999") as channel:
        stub = mads_pb2_grpc.mads_serviceStub(channel)
        try:
            response = stub.ping(mads_pb2.UserCreateObjectRequest(URI = "test_uri"))
            resp = response.Object
            print("I just received an object!")
            print(resp)
        except KeyboardInterrupt:
            print("KeyboardInterrupt")
            channel.unsubscribe(close)
            exit()


def close(channel):
    channel.close()


if __name__ == "__main__":
    run()