import redis

red = redis.Redis(host='localhost', port=6379, decode_responses=True)

red.publish('usernames', "myname")