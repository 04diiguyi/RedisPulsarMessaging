import string
import random
import time

import redis

# initializing size of string
N = 10

# Build connection to Redis
red = redis.Redis(host='localhost', port=6379, decode_responses=True)

# Check whether Redis setting is proper for the demo
max_memory = red.config_get('maxmemory')
print('max memory: ', max_memory)

red.config_set('maxmemory-policy', 'allkeys-random')

maxmemory_policy = red.config_get('maxmemory-policy')
print('max memory policy: ', maxmemory_policy)

# using random.choices()
# generating random strings
while(True):
    key = ''.join(random.choices(string.ascii_uppercase +
                                string.digits, k=N))

    red.set(key, key)

    print('insert key: ', key)

    print('max memory: ', max_memory)

    used_memory = red.info().get('used_memory')
    print("used_memory: ", used_memory)

    used_memory_human = red.info().get('used_memory_human')
    print("used_memory_human: ", used_memory_human)

    time.sleep(0.05)