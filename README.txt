// Setup first time
    If first time running kafka, install zookeeper and kafka. This project uses: kafka 2.13.2.7, zookeeper 3.6.2 and protobuf 3.13.
    Also run: 
    -pip install kafka-python
    -grpcio
    -grpcio-tools 
//

// Set up kafka:
    First, go into the kafka-folder and run in seperate windows (choose your own directory): 

        cd /Downloads/kafka_2.13-2.7.0

        ./bin/zookeeper-server-start.sh config/zookeeper.properties 
        ./bin/kafka-server-start.sh config/server.properties 

    This will start the zookeeper server
//

// Set up kafka producer and consumers (plugins)
    Now, run a producer (mads). mads is both a gRPC server and a kafka producer. 
    Go into this directory 
        cd /repos/objectcube_test_system/mads/
    and run:
        python3 mads.py  

    Now that the servers are running, we can start up one or more consumers listening to topics.
    Go into this directory 
        cd /repos/objectcube_test_system
    and run:
        python3 <plugin>.py    
        (...)
    Be aware, that previous messages send on this topic will display. This can be changed in the consumer-classes.
  
//

// The gRPC server (mads) is already running from above step. Now run the client
    open the directory and run: python3 client.py 

    OBS: the clients takes arguments in console to simulate interaction:
     - "new_object" adds new new_object                                     example: "new_object"
     - "change_tag <int> <newvalue>"                                        example: "change_tag 3 <En mand i skoven>"
     - "get_tags <int>" returns all tags associated with the objectid<int>  example: "get_tags 2"
//

// Compiling the .proto file:
    python3 -m grpc_tools.protoc -I./Proto --python_out=. --grpc_python_out=. ./Proto/mads.proto
//

// Deleting logs:
    rm -rf /tmp/kafka-logs /tmp/zookeeper
//

//For testing:
    run in client and choose the test file. Also set bool value in plugin_store_all_data to True and select proper .out-file
    python3 client.py < /home/christian/repos/objectcube_test_system/test/test_03.in
//

    