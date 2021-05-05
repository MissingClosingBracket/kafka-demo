from kafka import KafkaConsumer
import json

if __name__ == "__main__":
    consumer = KafkaConsumer(
        "translate",
        bootstrap_servers='0.0.0.0:9092',
        auto_offset_reset='earliest',
        group_id="translate-1")
    print("starting the consumer: plugin_translate_from_english_into_local")
    for msg in consumer:
        print("translate message = {}".format(json.loads(msg.value)))

