from kafka import KafkaConsumer
import json

if __name__ == "__main__":
    consumer = KafkaConsumer(
        "date",
        bootstrap_servers='0.0.0.0:9092',
        auto_offset_reset='earliest',
        group_id="date-2")
    print("starting the consumer: date")
    for msg in consumer:
        print("Date message = {}".format(json.loads(msg.value)))

