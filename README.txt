//
If first time running kafka, install zookeeper and kafka.
Also run "pip install kafka-python" 
//

// Set up kafka:
First, go into the kafka-folder and run in seperate windows: 

    cd /Downloads/kafka_2.13-2.7.0

    ./bin/zookeeper-server-start.sh config/zookeeper.properties 
    ./bin/kafka-server-start.sh config/server.properties 

This will start the zookeeper server
//

// Set up kafka producer and consumers (plugins)
Now that the server is running, we can start up one or more consumers listening to topics.
Go into this directory 
    cd /repos/kafka-demo/plugins
and run:
    python3 <plugin>.py    
    (...)
Be aware, that previous messages send on this topic will display. This can be changed in the consumer-classes.

Now, run a producer (mads). mads is both a gRPC server and a kafka producer. 
Go into this directory 
    cd /repos/kafka-demo/mads/
and run:
    python3 mads.py    
//






