import redis
import requests
import json
import event_emitter as events


em = events.EventEmitter()

client = redis.StrictRedis(host='localhost', port=6379, db=0)

default_headers = {
    'user-agent': 'Python Webhook Server',
    'accept': 'application/json',
}

@events.once(emitter=em, event='webhook')
def send_post_request(payload):
    try:
        # Initialize headers with default headers
        headers = default_headers.copy()  # Use copy to avoid modifying the original

        # Add payload['headers'] if it exists
        if 'headers' in payload:
            headers.update(payload['headers'])  # Update headers with any additional ones

        response = requests.post(payload['url'], json=payload['body'], headers=headers)
        print(f"POST request sent, response: {response.status_code}, response body: {response.text}")
    except Exception as e:
        print(f"Error sending POST request: {e}")


def message_handler(message):
    message_data = message['data'].decode('utf-8')
    payload = json.loads(message_data)  # json have url, and body
    print(f"Received message: {message_data}")

    em.emit('webhook', payload=payload)

    # Send the POST request with the JSON payload
    # send_post_request(payload)


def subscribe():
    pubsub = client.pubsub()
    pubsub.subscribe(**{'webhook': message_handler})
    print("Subscribed to 'webhook'. Waiting for messages...")

    # Listen for messages
    pubsub.run_in_thread(sleep_time=0.001)


if __name__ == '__main__':
    subscribe()
