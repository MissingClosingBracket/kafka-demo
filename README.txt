First, go into the kafka-folder and run: 

    cd /Downloads/kafka_2.13-2.7.0

    ./bin/zookeeper-server-start.sh config/zookeeper.properties 
    ./bin/kafka-server-start.sh config/server.properties 

This will start the zookeeper server



Now that the server is running, we can start up a consumer listening to a topic.
Go into this directory 
    cd /repos/kafka-demo
and run:
    python3 consumer.py    
Be aware, that prevois messages send on this topic will display. This can be changed in the consumer-class.

Now, run a producer. 
Go into this directory 
    cd /repos/kafka-demo
and run:
    python3 producer.py    
Be aware, that it will send a new message every 4 seconds.
