from kafka import KafkaConsumer
import json

all_events = []

if __name__ == "__main__":
    consumer = KafkaConsumer(
        "event_all",
        bootstrap_servers='0.0.0.0:9092',
        auto_offset_reset='latest',
        group_id="all-1")
    print("Starting the consumer: plugin_store_all_events")
    for msg in consumer:
        print("Storing an event. The event had the message = {}".format(json.loads(msg.value)))
        all_events.append(msg)