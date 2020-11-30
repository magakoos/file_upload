"""Root URL конфигурация."""

from typing import Tuple

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import URLResolver, include, path

from my_project.file_upload.views import index

urlpatterns: Tuple[URLResolver, ...] = (
    path('admin/', admin.site.urls),
    path('api/v1/', include('my_project.api.urls')),
    path('', index, name='index')
)

if settings.DEBUG:
    urlpatterns += tuple(static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT,
    ))
    urlpatterns += tuple(static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT,
    ))
