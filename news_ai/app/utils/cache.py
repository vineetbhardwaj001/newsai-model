from cachetools import LRUCache

cache = LRUCache(maxsize=100)

def get_cache(key):
    return cache.get(key)

def set_cache(key, value):
    cache[key] = value