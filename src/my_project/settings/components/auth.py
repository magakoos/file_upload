"""Модуль конфигурации Аутентификации."""

from typing import Tuple


AUTHENTICATION_BACKENDS: Tuple[str, ...] = (
    'django.contrib.auth.backends.ModelBackend',
)
