#!/usr/bin/env python3
"""A script for FIFO caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFO cache system"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ put key value pair into cache"""
        if key is None or item is None:
            return
        elif len(self.cache_data) >= FIFOCache.MAX_ITEMS:
            sorted_keys = sorted(self.cache_data.keys())
            if sorted_keys:
                first_key = sorted_keys[0]
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")
        self.cache_data[key] = item

    def get(self, key):
        """ return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist
        in self.cache_data, return None."""
        return self.cache_data.get(key)
