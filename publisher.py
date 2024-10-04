import redis
import json

# Connect to Redis
client = redis.StrictRedis(host='localhost', port=6379, db=0)


def publish_message(url, body):
    # Construct the payload as a dictionary
    payload = {
        'url': url,
        'body': body
    }

    # Convert the payload to a JSON string
    message = json.dumps(payload)

    # Publish the message to the 'webhook' channel
    client.publish('webhook', message)
    print(f"Published message: {message}")


if __name__ == '__main__':
    # Use the specified webhook URL
    webhook_url = 'https://webhook.site/58480b38-cea1-4c32-893a-6898ef01987c'

    # Sample JSON body to send
    sample_body = {
        'message': 'Hello, this is a test message!',
        'status': 'success'
    }

    publish_message(webhook_url, sample_body)
