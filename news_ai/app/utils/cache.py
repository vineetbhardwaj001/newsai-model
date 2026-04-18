from cachetools import TTLCache

cache = TTLCache(maxsize=200, ttl=600)

def get_cache(key):
    return cache.get(key)

def set_cache(key, value):
    cache[key] = value