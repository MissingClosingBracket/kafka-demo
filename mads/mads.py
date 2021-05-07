from kafka import KafkaProducer
import json

def json_serializer(data):
    return json.dumps(data).encode("utf-8")

producer = KafkaProducer(bootstrap_servers=['0.0.0.0:9092'],
                         value_serializer=json_serializer)


if __name__ == "__main__":
    while True:
        topic, message = input().split()

        if (topic == "alphanumerical"):
            data = {"message": message}
            producer.send(topic, data)
            producer.send("all",data)

        if (topic == "numerical"):
            data = {"message": message}
            producer.send(topic, data)    

        if (topic == "date"):
            data = {"message": message}
            producer.send(topic, data)    

        if (topic == "time"):
            data = {"message": message}
            producer.send(topic, data)    

        if (topic == "rgb"):
            data = {"message": message}
            producer.send(topic, data)  