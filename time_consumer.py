from kafka import KafkaConsumer
import json

if __name__ == "__main__":
    consumer = KafkaConsumer(
        "time",
        bootstrap_servers='0.0.0.0:9092',
        auto_offset_reset='earliest',
        group_id="time-1")
    print("starting the consumer: time")
    for msg in consumer:
        print("Time message = {}".format(json.loads(msg.value)))

