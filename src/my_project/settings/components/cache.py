"""Модуль конфигурации Кэша."""

from my_project.settings.components.common import REDIS_URL


CACHE_REDIS_HOSTS = f'{REDIS_URL}/0'

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': CACHE_REDIS_HOSTS,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'IGNORE_EXCEPTIONS': True,
        }
    }
}

SOLO_CACHE = 'default'
SOLO_CACHE_TIMEOUT = 60
SOLO_CACHE_PREFIX = 'solo'

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'

CACHEOPS_REDIS = f'{REDIS_URL}/2'
CACHEOPS_DEGRADE_ON_FAILURE = True

CACHEOPS_DEFAULTS = {
    'timeout': 60 * 60,
}

CACHEOPS = {
}
