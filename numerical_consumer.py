from kafka import KafkaConsumer
import json

if __name__ == "__main__":
    consumer = KafkaConsumer(
        "numerical",
        bootstrap_servers='0.0.0.0:9092',
        auto_offset_reset='earliest',
        group_id="numerical-1")
    print("starting the consumer: numerical")
    for msg in consumer:
        print("Numerical meesage = {}".format(json.loads(msg.value)))

