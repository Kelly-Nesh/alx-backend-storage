#!/usr/bin/env python3
"""Writing strings to Redis
Reading from Redis and recovering original type
"""
import redis
import uuid
from typing import Union


class Cache:
    """Redis Cache"""

    def __init__(self):
        """store an instance of the Redis client as a private variable"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Takes a data argument and returns a string(key)."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn=None):
        """Takes a key argument and returns the data stored in the key.
        fn: callable will be used to convert the data
            back to the desired format."""
        value = self._redis.get(key)
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        '''
            Get a string from the cache.
        '''
        value = self._redis.get(key)
        return value.decode('utf-8')

    def get_int(self, key: str) -> int:
        '''
            Get an int from the cache.
        '''
        value = self._redis.get(key)
        try:
            value = int(value.decode('utf-8'))
        except Exception:
            value = 0
        return value


cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value
