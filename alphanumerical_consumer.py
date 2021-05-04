from kafka import KafkaConsumer
import json

if __name__ == "__main__":
    consumer = KafkaConsumer(
        "alphanumerical",
        bootstrap_servers='0.0.0.0:9092',
        auto_offset_reset='earliest',
        group_id="alphanumerical-1")
    print("starting the consumer: alphanumerical")
    for msg in consumer:
        print("Alphanumerical message = {}".format(json.loads(msg.value)))
