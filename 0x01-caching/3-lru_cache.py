#!/usr/bin/python3
"""
LRUCache module
"""

BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class"""

    def __init__(self):
        super().__init__()
        self._lru_keys = set()

    def put(self, key, item):
        """put method"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            self._lru_keys.add(key)
            if len(self.cache_data) > self.MAX_ITEMS:
                removed_key = self._lru_keys.pop()
                del self.cache_data[removed_key]
                print(f"DISCARD: {removed_key}")

    def get(self, key):
        """get method"""
        if key in self.cache_data.keys():
            self._lru_keys.remove(key)
            self._lru_keys.add(key)
        return self.cache_data.get(key, None)
