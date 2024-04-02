#!/usr/bin/env python3
"""A script for LRU caching system
"""
from collections import deque
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRU cache system"""
    def __init__(self):
        super().__init__()
        self.keys = deque()

    def put(self, key, item):
        """ put key value pair into cache"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.rotate(key)
        elif len(self.cache_data) >= LRUCache.MAX_ITEMS:
            deleted_key = self.keys.popleft()
            del self.cache_data[deleted_key]
            print(f"DISCARD: {deleted_key}")
        self.keys.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist
        in self.cache_data, return None."""
        if key in self.keys:
            self.rotate(key)
            self.keys.append(key)
        return self.cache_data.get(key)

    def rotate(self, key):
        ''' rotate keys list'''
        index = self.keys.index(key)
        self.keys.rotate(-index)
        self.keys.popleft()
        self.keys.rotate(index)
