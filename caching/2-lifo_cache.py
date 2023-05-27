#!/usr/bin/python3
"""2-lifo_cache"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class that inherits from BaseCaching"""

    def __init__(self):
        """Initialize the LIFO Cache"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Add an item to the cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key not in self.cache_data:
                    last_key = self.keys.pop()
                    del self.cache_data[last_key]
                    print("DISCARD: {}".format(last_key))
            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        """Get an item from the cache"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
