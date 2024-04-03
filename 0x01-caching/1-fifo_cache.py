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
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                discard = sorted(self.cache_data.keys())[0]
                del self.cache_data[discard]
                print(f"DISCARD: {discard}")

    def get(self, key):
        """get method"""
        try:
            return self.cache_data[key]
        except Exception:
            return None
