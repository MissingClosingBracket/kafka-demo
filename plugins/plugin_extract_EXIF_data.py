from kafka import KafkaConsumer
import json


if __name__ == "__main__":
    consumer = KafkaConsumer(
        "newObject",
        bootstrap_servers='0.0.0.0:9092',
        auto_offset_reset='earliest',
        group_id="exif-1")
    print("starting the consumer: plugin_extract_EXIF_data")
    for msg in consumer:
        print("extracting EXIF data from image = {}".format(json.loads(msg.value)))
