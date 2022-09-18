import json

from tabulate import tabulate

from redis_client import redis_client
from redis_lru import RedisLRU

cache = RedisLRU(redis_client)
redis_client.flushdb()


def show_cache():
    for key in redis_client.scan_iter():
        print('Key:', key)
        print('Value:', redis_client.get(key))


def print_data(value):
    table_data = [
        ['First name', 'Last name', 'Email', 'Phone'],
        [value["first_name"], value["last_name"], value["email"], value["phone"]]
    ]
    print(tabulate(table_data, headers='firstrow', tablefmt='grid'))


class LruCache:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        key = args[0]
        if cache.get(key) is not None:
            value_json = cache.get(key)
            value = json.loads(value_json)
            print_data(value)
            show_cache()

        else:
            value = self.func(*args, **kwargs)
            value_json = json.dumps(value)
            cache.set(key, value_json)
            print_data(value)
            show_cache()
