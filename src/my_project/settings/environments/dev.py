"""Dev настройки приложения."""

import logging

from my_project.settings.environments.base import *  # @UnusedWildImport


USE_X_FORWARDED_HOST = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ('*',)


INSTALLED_APPS = INSTALLED_APPS + (
    'nplusone.ext.django',
)

MIDDLEWARE = MIDDLEWARE + (
    'nplusone.ext.django.NPlusOneMiddleware',
)


NPLUSONE_LOGGER = logging.getLogger('nplusone')
NPLUSONE_LOG_LEVEL = logging.WARN

DEBUG = os.getenv('DEBUG', True)
