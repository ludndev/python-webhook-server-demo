import redis
import json

from demo.payload_dto import PayloadDto

# Connect to Redis
client = redis.StrictRedis(host='localhost', port=6379, db=0)


def publish_message(url, body, headers=None):
    if headers is None:
        headers = {}

    # Construct the payload as a dictionary
    payload = {
        'url': url,
        'body': body,
        'headers': headers,
    }

    # Convert the payload to a JSON string
    message = json.dumps(payload)

    # Publish the message to the 'webhook' channel
    client.publish('webhook', message)
    print(f"Published message: {message}")


def publish_message_from_payload_dto(payload_dto: PayloadDto):
    if payload_dto.headers is None:
        payload_dto.headers = {}

    # Construct the payload as a dictionary
    print(payload_dto.to_dict())

    # Convert the payload to a JSON string
    message = json.dumps(payload_dto.to_dict())

    # Publish the message to the 'webhook' channel
    client.publish('webhook', message)
    print(f"Published message: {message}")


if __name__ == '__main__':
    # Use the specified webhook URL
    webhook_url = 'https://webhook.site/58480b38-cea1-4c32-893a-6898ef01987c'

    headers = {
        'x-api-key': '<KEY>',
    }

    # Sample JSON body to send
    sample_body = {
        'message': 'Hello, this is a test message!',
        'status': 'success',
    }

    payload = PayloadDto(
        url=webhook_url,
        body=sample_body,
        headers=headers,
    )

    # publish_message(webhook_url, sample_body, headers)
    publish_message_from_payload_dto(payload)
