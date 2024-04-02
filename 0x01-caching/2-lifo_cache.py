#!/usr/bin/python3
"""lifo cahce 2"""

from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """LIFOCache"""
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
            k = list(self.cache_data.keys())[-2]
            del self.cache_data[k]
            self.discard = k

    def get(self, key):
        """get method"""
        try:
            return self.cache_data[key]
        except Exception:
            return None


my_cache = LIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()