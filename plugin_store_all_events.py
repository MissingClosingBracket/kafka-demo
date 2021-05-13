from kafka import KafkaConsumer
import json

all_events = []
write_to_file = False

if __name__ == "__main__":
    consumer = KafkaConsumer(
        "event_all",
        bootstrap_servers='0.0.0.0:9092',
        auto_offset_reset='latest',
        group_id="all-1")
    print("Starting the consumer: plugin_store_all_events")
    #open file
    f = open(r"/home/christian/repos/kafka-demo/test/test_03.out", "w")
    for msg in consumer:
        print("Storing an event. The event had the message = {}".format(json.loads(msg.value)))
        all_events.append(msg)
        if (write_to_file):
            f.write(json.dumps(json.loads(msg.value)) + "\n")
    f.close()        