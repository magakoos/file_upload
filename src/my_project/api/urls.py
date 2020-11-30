"""Роуты для API приложения. Схема API."""

from typing import Tuple

from django.urls import URLResolver, include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


from .file_upload.urls import urlpatterns as file_upload_urlpatterns


schema_view = get_schema_view(
    openapi.Info(
        title='Test Case',
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns: Tuple[URLResolver, ...] = (
    path('file_upload/', include(file_upload_urlpatterns)),
    path(
        'swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
    path(
        'redoc/',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'
    ),
)
