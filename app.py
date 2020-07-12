from json import dumps
from kafka import KafkaProducer
import os

producer = KafkaProducer(bootstrap_servers=['kafka-headless.kafka.svc.cluster.local:9092'],
                         acks=1,
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

move_type = "tv"
directory = os.listdir("/output")
for filename in directory:
    message = {'filename': filename, 'move_type': move_type}
    print("Sending message {}".format(message), flush=True)
    future = producer.send(topic='handbrakeFile', value=message)
    result = future.get(timeout=60)
