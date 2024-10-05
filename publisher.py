import redis
import json

from demo.payload_dto import PayloadDto

# Connect to Redis
client = redis.StrictRedis(host='localhost', port=6379, db=0)


def publish_message(channel: str, payload_dto: PayloadDto):
    if payload_dto.headers is None:
        payload_dto.headers = {}

    # Construct the payload as a dictionary
    print(payload_dto.to_dict())

    # Convert the payload to a JSON string
    message = json.dumps(payload_dto.to_dict())

    # Publish the message to the chosen channel
    client.publish(channel, message)
    print(f"Published on [{channel}]: {message}")


if __name__ == '__main__':
    event = 'payment.transaction.success'

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
        event=event,
        url=webhook_url,
        body=sample_body,
        headers=headers,
    )

    publish_message('webhook', payload)

    # event = 'payment.transaction.failed'
    # sample_body['status'] = 'failed'
    # payload = PayloadDto(
    #     event=event,
    #     url=webhook_url,
    #     body=sample_body,
    #     headers=headers,
    # ) 
    # publish_message('webhook', payload)
    
    # event = 'invalid_event'
    # sample_body['status'] = 'invalid_event'
    # payload = PayloadDto(
    #     event=event,
    #     url=webhook_url,
    #     body=sample_body,
    #     headers=headers,
    # )
    # publish_message('webhook', payload)
