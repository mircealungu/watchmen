import collections


class LRUCache:
    """ Simple Least Recently Used caching implementation. """
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        """ Update the order or return a fetch error. """
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return False

    def set(self, key, value):
        """ Update the order or add a new value.
            Will remove old values from the cache if we reached our maximum capacity."""
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
        self.cache[key] = value