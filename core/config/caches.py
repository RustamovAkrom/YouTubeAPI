CACHES = {
    "default": {
        # "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        # "BACKEND": 'django.core.cache.backends.db.DatabaseCache',
        # "BACKEND": 'django.core.cache.backends.filebased.FileBasedCache',
        # "BACKEND": 'django.core.cache.backends.dummy.DummyCache',
        # "BACKEND": 'django.core.cache.backends.locmem.LocMemCache',
        # "BACKEND": 'django.core.cache.backends.memcached.PyMemcacheCache',
        # "BACKEND": 'django.core.cache.backends.memcached.PyLibMCCache',
        "BACKEND": 'django.core.cache.backends.redis.RedisCache',
        "LOCATION": "http://localhost:6379/0"
    }
}
