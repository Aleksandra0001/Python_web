from collections import deque
from functools import lru_cache


class LruCache:
    def __init__(self, maxsize=100, typed=False):
        self.maxsize = maxsize
        self.typed = typed
        self.cache = {}
        self.queue = deque()

    def __call__(self, user_function):
        def wrapper(*args, **kwargs):
            key = args
            if self.typed:
                key += tuple([type(arg) for arg in args])
            key += tuple(kwargs.items())
            if key in self.cache:
                self.queue.remove(key)
                self.queue.append(key)
                return self.cache[key]
            else:
                if len(self.cache) == self.maxsize:
                    del self.cache[self.queue.popleft()]
                self.cache[key] = user_function(*args, **kwargs)
                self.queue.append(key)
                return self.cache[key]

        return wrapper


@lru_cache()
def foo(x):
    return x


def lruCache(maxsize=100, typed=False):
    queue = deque()
    return "".join((str(ch) for ch in queue))
