from cachetools import TTLCache

# LRU Cache with TTL (10 minutes)
pokemon_cache = TTLCache(maxsize=100, ttl=600)
