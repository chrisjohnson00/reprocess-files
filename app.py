from json import dumps
import pulsar
import os
import pygogo as gogo

# logging setup
kwargs = {}
formatter = gogo.formatters.structured_formatter
logger = gogo.Gogo('struct', low_formatter=formatter).get_logger(**kwargs)


def send_completion_message(file_name, move_type_name):
    pulsar_server = get_config('PULSAR_SERVER')
    pulsar_topic = get_config('PULSAR_TOPIC')
    if pulsar_server and pulsar_topic:
        client = pulsar.Client(f"pulsar://{pulsar_server}")
        producer = client.create_producer(pulsar_topic)
        message = {'filename': file_name, 'move_type': move_type_name}
        producer.send(dumps(message).encode('utf-8'))
        logger.info("Notification sent", extra={'message_body': message, 'topic': pulsar_topic, 'file': file_name})
        client.close()
    else:
        logger.warning("PULSAR_SERVER or PULSAR_TOPIC was not found in configs, no messages will be sent")


def get_config(key):
    if os.environ.get(key):
        return os.environ.get(key)


if __name__ == "__main__":
    directory = os.listdir("/output")
    for filename in directory:
        send_completion_message(filename, get_config('MOVE_TYPE'))
