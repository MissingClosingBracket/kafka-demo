from kafka import KafkaConsumer
import json

write_to_test_file = False

if __name__ == "__main__":
    consumer = KafkaConsumer(
        "event_all",
        bootstrap_servers='0.0.0.0:9092',
        auto_offset_reset='latest',
        group_id="all-1")
    print("Starting the consumer: plugin_store_all_events")
    #open file. Also test file, even though may not be use (open/close actions take time)
    log_file = open("log_file.txt", "w")
    test_file = open(r"/home/christian/repos/objectcube_test_system/test/test_03.out", "w")
    for msg in consumer:
        print("Storing an event. The event had the message = {}".format(json.loads(msg.value)))
        log_file.write(json.dumps(json.loads(msg.value)) + "\n")
        if (write_to_test_file):
            test_file.write(json.dumps(json.loads(msg.value)) + "\n")
    test_file.close()  
    log_file.close      