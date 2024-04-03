#!/usr/bin/python3
"""
LFUCache module
"""

BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """LFUCache class"""

    def __init__(self):
        super().__init__()
        self._lfu = []

    def put(self, key, item):
        """put methods"""
        if key is None and item is None:
            pass
        else:
            if key in self.cache_data:
                self.cache_data[key] = item
                self._lfu.pop(self._lfu.index(key))
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    lfu = self._lfu.pop(0)
                    del self.cache_data[lfu]
                    print(f"DISCARD: {lfu}")
                self.cache_data[key] = item
            self._lfu.append(key)

    def get(self, key):
        """get method"""
        if key is not None and key in self.cache_data:
            self._lfu.pop(self._lfu.index(key))
            self._lfu.append(key)
        return self.cache_data.get(key, None)
