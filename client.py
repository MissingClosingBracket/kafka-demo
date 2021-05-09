import time
import grpc
import mads_pb2
import mads_pb2_grpc
import time

#make client do a gRPC
def run():
    with grpc.insecure_channel("localhost:9999") as channel:
        stub = mads_pb2_grpc.mads_serviceStub(channel)
        while True:
            cl_in = input()
            if (cl_in == "new_object"):
                try:
                    #Add a picture to the system:
                    response = stub.userCreateObject(mads_pb2.UserCreateObjectRequest(URI = "test_uri"))
                    print("--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--")
                    print("I just received a response on adding an object to the system: (object) =")
                    print(response)
                    print("")
                    channel.unsubscribe(close)
                    #
                except KeyboardInterrupt:
                    print("KeyboardInterrupt")
                    channel.unsubscribe(close)
                    exit()
            elif (cl_in.split()[0] == "tags"):
                try:
                    #Retrieve tags for an object:
                    oid = int(cl_in.split()[1])
                    print("--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--")
                    print("I just received a response on requesting for all tags associated with an object: oid = " + str(oid) + ".")
                    for res in stub.userRequestsTagsForObject(mads_pb2.UserRequestsTagsForObjectRequest(oid = oid)):
                        print(res)
                    print("")    
                    channel.unsubscribe(close)
                    #
                except KeyboardInterrupt:
                    print("KeyboardInterrupt")
                    channel.unsubscribe(close)
                    exit()        

def close(channel):
    channel.close()


if __name__ == "__main__":
    run()