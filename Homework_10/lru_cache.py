import json

from functools import wraps
from redis import StrictRedis
import redis

client = redis.StrictRedis(host="localhost", port=6379, password=None)
print(client.info())

redis = StrictRedis()


def redis_cache(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # собираем ключ из аргументов ф-и.
        key_parts = [func.__name__] + list(args)
        key = '-'.join(key_parts)
        result = redis.get(key)

        if result is None:
            # ничего не нашли в кэше – дергаем ф-ю и сохраняем результат.
            value = func(*args, **kwargs)
            value_json = json.dumps(value)
            redis.set(key, value_json)
        else:
            # Ура, данные есть в кэше – используем их.
            value_json = result.decode('utf-8')
            value = json.loads(value_json)

        return value

    return wrapper

