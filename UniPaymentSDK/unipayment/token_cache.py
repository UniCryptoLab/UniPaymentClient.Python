from __future__ import absolute_import

import time


class TokenCache:
    _cache = {}
    ACCESS_TOKEN = 'access_token'  # Define the constant

    @staticmethod
    def set_access_token(value, ttl=3600):
        expiry = int(time.time()) + ttl
        TokenCache._cache[TokenCache.ACCESS_TOKEN] = {'expiry': expiry, 'value': value}

    @staticmethod
    def get_access_token():
        cached_item = TokenCache._cache.get(TokenCache.ACCESS_TOKEN)
        if cached_item is None:
            return None

        if time.time() > cached_item['expiry']:
            del TokenCache._cache[TokenCache.ACCESS_TOKEN]
            return None

        return cached_item['value']
