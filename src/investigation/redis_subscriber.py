import redis

red = redis.Redis(host='localhost', port=6379, decode_responses=True)

def user_counter():
    sub = red.pubsub()
    sub.subscribe('usernames')
    for message in sub.listen():
        if message is not None and isinstance(message, dict):
            username = message.get('data')
            print(username)

while True:
  user_counter()