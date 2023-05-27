#!/usr/bin/python3
""" 4-mru_cache """
from base_caching import BaseCaching

class MRUCache(BaseCaching):
    """ MRUCache class that inherits from BaseCaching """

    def __init__(self):
        """ Initialize the MRU Cache """
        super().__init__()

    def put(self, key, item):
        """ Add an item to the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key not in self.cache_data:
                    mru_key = list(self.cache_data.keys())[-1]
                    del self.cache_data[mru_key]
                    print("DISCARD: {}".format(mru_key))
            elif key in self.cache_data:
                del self.cache_data[key]
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache """
        if key is not None and key in self.cache_data:
            value = self.cache_data[key]
            del self.cache_data[key]
            self.cache_data[key] = value
            return value
        return None
