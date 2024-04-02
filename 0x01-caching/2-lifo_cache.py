#!/usr/bin/env python3
"""A script for LIFO caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFO cache system"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ put key value pair into cache"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            deleted_key = key
        elif len(self.cache_data) >= LIFOCache.MAX_ITEMS:
            sorted_keys = sorted(self.cache_data.keys())
            if sorted_keys:
                deleted_key = sorted_keys[-1]
            del self.cache_data[deleted_key]
            print(f"DISCARD: {deleted_key}")
        self.cache_data[key] = item

    def get(self, key):
        """ return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist
        in self.cache_data, return None."""
        return self.cache_data.get(key)
