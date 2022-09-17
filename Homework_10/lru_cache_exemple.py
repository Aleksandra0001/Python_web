from functools import lru_cache

import redis
from redis_lru import RedisLRU
import timeit

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)



def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def factorial_cache(n):
    if n == 0:
        return 1
    else:
        if cache.get(n):
            return cache.get(n)
        else:
            cache.set(n, n * factorial_cache(n - 1))
            return cache.get(n)


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
        print(result)
        return result


if __name__ == "__main__":
    pass
    # print([fib(n) for n in range(5)])
    # print(fib(5))
    # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]

    # print(fib.cache_info())
    # CacheInfo(hits=28, misses=16, maxsize=None, currsize=16)

    # start_time = timeit.default_timer()
    # # factorial(100)
    # fibonacci(5)
    # end_time = timeit.default_timer() - start_time
    # # print(f"Time without cache: {end_time}")
    #
    # start_time = timeit.default_timer()
    # # factorial_cache(100)
    # end_time = timeit.default_timer() - start_time
    # # print(f"Time with cache: {end_time}")
