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
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)
