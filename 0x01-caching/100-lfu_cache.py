#!/usr/bin/python3
"""
LFU Caching
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFU class
    """

    def __init__(self):
        """
        constructor
        """
        self.usedKey = {}
        self.timesKey = {}
        self.time = 0
        super().__init__()

    def put(self, key, item):
        """
        add to the cache
        """
        if key is not None and item is not None:
            # modify the used key
            if key not in self.usedKey:
                self.usedKey[key] = 1
            else:
                self.usedKey[key] += 1

            # modify the time and change the next newer value
            self.timesKey[key] = self.time
            self.time += 1

            # add the new item
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # copy the dict and delete the new key
            cpyusedKey = self.usedKey.copy()
            del cpyusedKey[key]

            # get the smallest value
            smallest_value = min(cpyusedKey, key=cpyusedKey.get)
            smallest_value = cpyusedKey[smallest_value]

            # find the keys to delete
            sameKeyValue = {}
            for _key, _value in cpyusedKey.items():
                if _value == smallest_value:
                    sameKeyValue[_key] = _value

            # if by lfu or lru
            if len(sameKeyValue) == 1:
                discard_key = list(sameKeyValue.keys())[0]
            else:
                # times of the samekeyvalues
                time_sameKeyValue = {}
                for _key, _value in self.timesKey.items():
                    if _key in sameKeyValue:
                        time_sameKeyValue[_key] = _value

                # get the smallest time value
                discard_key = min(time_sameKeyValue, key=time_sameKeyValue.get)

            # del key in used and cache data
            del self.cache_data[discard_key]
            del self.usedKey[discard_key]
            del self.timesKey[discard_key]

            print("DISCARD: {}".format(discard_key))

    def get(self, key):
        """
        get the cache item value
        """
        if key is None or key not in self.cache_data:
            return None

        # modify the used
        self.usedKey[key] += 1

        # modify the time and change the next newer value
        self.timesKey[key] = self.time
        self.time += 1

        return self.cache_data[key]
