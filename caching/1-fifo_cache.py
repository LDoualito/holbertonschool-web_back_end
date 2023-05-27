#!/usr/bin/python3
"""1-fifo_cache"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class that inherits from BaseCaching"""

    def __init__(self):
        """Initialize the FIFO Cache"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Add an item to the cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key not in self.cache_data:
                    first_key = self.keys[0]
                    del self.cache_data[first_key]
                    self.keys.pop(0)
                    print("DISCARD: {}".format(first_key))
            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        """Get an item from the cache"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
