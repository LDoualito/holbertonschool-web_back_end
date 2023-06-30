#!/usr/bin/env python3
""" Writing strings to Redis """
import redis
from typing import Union, Optional, Callable
from uuid import uuid4
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ count how many times methods are called """
    name = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ wrapper method """
        self._redis.incr(name)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """ Store the history of inputs and outputs for a function """
    name = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ wrapper method """
        input = str(args)
        self._redis.rpush(name + ":inputs", input)

        output = str(method(self, *args, **kwargs))
        self._redis.rpush(name + ":outputs", output)

        return output

    return wrapper


def replay(method: Callable):
    """ Display the history of a function """
    name = method.__qualname__
    inputs = name + ':inputs'
    outputs = name + ':outputs'
    redis = method.__self__._redis
    count = redis.get(name).decode("utf-8")
    print("{} was called {} times:".format(name, count))
    inputList = redis.lrange(inputs, 0, -1)
    outputList = redis.lrange(outputs, 0, -1)
    zipped_list = list(zip(inputList, outputList))
    for inp, out in zipped_list:
        inp = inp.decode("utf-8")
        out = out.decode("utf-8")
        print("{}(*{}) -> {}".format(name, inp, out))


class Cache:
    """ Represents the cache """
    def __init__(self) -> None:
        """ constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store in db """
        key = str(uuid4())
        self._redis.append(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """ get the data """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, data: str) -> str:
        """ parametrize to str """
        return data.decode("utf-8")

    def get_int(self, data: str) -> int:
        """ parametrize to str """
        try:
            data = int(data.decode("utf-8"))
        except Exception:
            data = 0
        return data