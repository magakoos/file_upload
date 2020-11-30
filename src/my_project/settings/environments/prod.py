"""Production настройки приложения."""


from my_project.settings.environments.base import *  # @UnusedWildImport


USE_X_FORWARDED_HOST = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ('prod_host',)

DEBUG = False

