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
            elif (cl_in.split()[0] == "get_tags"):
                try:
                    #Retrieve tags for an object:
                    oid = int(cl_in.split()[1])
                    print("--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--")
                    print("I just received a response on requesting for all tags associated with an object: oid = " + str(oid) + ".")
                    for res in stub.userRequestsTagsForObject(mads_pb2.UserRequestsTagsForObjectRequest(oid = oid)):
                        if (res.HasField("tag")):    
                            print(res)
                        else:
                            print("Something went wrong. Make sure the id represented.")    
                    print("")    
                    channel.unsubscribe(close)
                    #
                except KeyboardInterrupt:
                    print("KeyboardInterrupt")
                    channel.unsubscribe(close)
                    exit()      
            elif (cl_in.split()[0] == "change_tag"):
                try:
                    #Change value for tag:
                    tid = int(cl_in.split()[1])
                    s1 = cl_in.split("<")
                    s2 = s1[1].split(">")[0]
                    print("--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--")
                    print("I just received a response on changing the tag: tid = " + str(tid) + ".")
                    response = stub.userChangeTag(mads_pb2.UserChangeTagRequest(tid = tid, value = s2))
                    if (response.HasField("tag") == False): 
                        print("Something went wrong. Make sure the id exists.")
                        print("")
                        channel.unsubscribe(close)
                    else:    
                        print(response)
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