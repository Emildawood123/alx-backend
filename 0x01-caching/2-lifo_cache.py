#!/usr/bin/python3
"""
LIFOCache module
"""

BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class"""

    def __init__(self):
        super().__init__()
        self._last_key = None

    def put(self, key, item):
        """put method"""
        if key is not None and item is not None:
            if (
                len(self.cache_data) == self.MAX_ITEMS
                and key not in self.cache_data.keys()
            ):
                discarded_key = self._last_key
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")

            self.cache_data[key] = item
            self._last_key = key

    def get(self, key):
        """get method"""
        try:
            return self.cache_data[key]
        except Exception:
            return None
