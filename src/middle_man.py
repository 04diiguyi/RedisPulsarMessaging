import redis
import pulsar

redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)
pulsar_client = pulsar.Client('pulsar://localhost:6650')

# Check the settings of Redis
max_memory = redis_client.config_get('maxmemory')
print('max memory: ', max_memory)

maxmemory_policy = redis_client.config_get('maxmemory-policy')
print('max memory policy: ', maxmemory_policy)

config_reponse = redis_client.config_set('notify-keyspace-events', 'KEAe')
print(config_reponse)

# Set up pub/sub for Redis and Pulsar
redis_sub = redis_client.pubsub()

pulsar_producer = pulsar_client.create_producer('Redis-Evicted')

# Redis Eviction message
##{'type': 'pmessage', 'pattern': '*', 'channel': '__keyevent@0__:evicted', 'data': '96IIUME8L8'}

def forward_message():
    redis_sub.subscribe('__keyevent@0__:evicted')
    for message in redis_sub.listen():
        if message is not None and isinstance(message, dict):
            evicted_key = message.get('data')
            print('key evicted: ', evicted_key)
            # 1 indicates connection created
            if evicted_key != 1:
                pulsar_producer.send(evicted_key.encode('utf-8'))
                
while True:
    forward_message()

pulsar_client.close()