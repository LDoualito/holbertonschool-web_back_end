#!/usr/bin/python3
"""3-lru_cache"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class that inherits from BaseCaching"""

    def __init__(self):
        """Initialize the LRU Cache"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Add an item to the cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key not in self.cache_data:
                    last_key = self.keys.pop(0)
                    del self.cache_data[last_key]
                    print("DISCARD: {}".format(last_key))
            elif key in self.keys:
                self.keys.remove(key)
            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        """Get an item from the cache"""
        if key is not None and key in self.cache_data:
            self.keys.remove(key)
            self.keys.append(key)
            return self.cache_data[key]
        return None
