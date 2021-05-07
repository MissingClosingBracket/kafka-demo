from kafka import KafkaConsumer
import json

if __name__ == "__main__":
    consumer = KafkaConsumer(
        "all",
        bootstrap_servers='0.0.0.0:9092',
        auto_offset_reset='earliest',
        group_id="all-1")
    print("starting the consumer: plugin_store_all_events")
    for msg in consumer:
        print("all message being stored = {}".format(json.loads(msg.value)))