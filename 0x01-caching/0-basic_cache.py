#!/usr/bin/env python3
"""basicCach iherted class"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache"""
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

    def get(self, key):
        """get method"""
        try:
            return self.cache_data[key]
        except Exception:
            return None
