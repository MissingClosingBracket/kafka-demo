from kafka import KafkaConsumer
import json

if __name__ == "__main__":
    consumer = KafkaConsumer(
        "rgb",
        bootstrap_servers='0.0.0.0:9092',
        auto_offset_reset='earliest',
        group_id="rgb-1")
    print("starting the consumer: rgb")
    for msg in consumer:
        print("RGB message = {}".format(json.loads(msg.value)))

