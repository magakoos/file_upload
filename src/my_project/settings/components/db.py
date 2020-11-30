"""Модуль конфигурации Базы Данных."""

import os


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'db_dev'),
        'USER': os.getenv('POSTGRES_USER', 'db_dev'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'db_dev'),
        'HOST': os.getenv('POSTGRES_HOST', '127.0.0.1'),
        'PORT': os.getenv('POSTGRES_PORT', '5432'),
    },
}
