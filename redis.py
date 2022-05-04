import redis

red = redis.Redis(
    host='redis-14984.c299.asia-northeast1-1.gce.cloud.redislabs.com',
    port=14984,
    password='1jMk0iT3jvynXmbBcudpUqy2reIwR076'
)

red.set('var1', 'value1')
print(red.get('var1'))