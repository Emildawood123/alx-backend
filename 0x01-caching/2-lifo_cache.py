#!/usr/bin/python3
"""lifo cahce 2"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache"""
    def __init__(self):
        """__init__ constructor"""
        super().__init__()
        self._last_key = None

    def put(self, key, item):
        """put method"""
        if key is None or item is None:
            return
        else:
            if (
                len(self.cache_data) == self.MAX_ITEMS
                and key not in self.cache_data.keys()
            ):
                discard = self._last_key
                del self.cache_data[discard]
                print(f"DISCARD: {discard}")
            self.cache_data[key] = item
            self._last_key = key

    def get(self, key):
        """get method"""
        try:
            return self.cache_data[key]
        except Exception:
            return None
