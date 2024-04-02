#!/usr/bin/env python3
"""FIFOCache class"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class"""
    def __init__(self):
        """__init__ constructor"""
        super().__init__()

    def put(self, key, item):
        """put method"""
        if key is None or item is None:
            return
        else:
            try:
                if self.cache_data[key] is item:
                    return
                self.cache_data[key] = item
            except Exception:
                self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            k = list(self.cache_data.keys())[0]
            del self.cache_data[k]
            self.discard = k

    def get(self, key):
        """get method"""
        try:
            return self.cache_data[key]
        except Exception:
            return None
