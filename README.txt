//
If first time running kafka, install zookeeper and kafka.
Also run "pip install kafka-python" 
//

First, go into the kafka-folder and run in seperate windows: 

    cd /Downloads/kafka_2.13-2.7.0

    ./bin/zookeeper-server-start.sh config/zookeeper.properties 
    ./bin/kafka-server-start.sh config/server.properties 

This will start the zookeeper server



Now that the server is running, we can start up one or more consumers listening to topics.
Go into this directory 
    cd /repos/kafka-demo
and run:
    python3 alphanumerical_consumer.py    
    python3 time_consumer.py 
    (...)
Be aware, that prevois messages send on this topic will display. This can be changed in the consumer-class.

Now, run a producer. 
Go into this directory 
    cd /repos/kafka-demo
and run:
    python3 producer.py    

Now, enter message in console, like: "time 12:32:54"
                                 or: "alphanumerical 1a2b3c4d"                           




