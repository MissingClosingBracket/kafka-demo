from kafka import KafkaConsumer
import json

if __name__ == "__main__":
    consumer = KafkaConsumer(
        "geodata",
        bootstrap_servers='0.0.0.0:9092',
        auto_offset_reset='earliest',
        group_id="geodata-1")
    print("starting the consumer: plugin_return_geodata_from_coordinates")
    for msg in consumer:
        print("geodata message = {}".format(json.loads(msg.value)))

