from django.urls import path
from rest_framework.routers import DefaultRouter


from my_project.api.file_upload.views import ImageView

router = DefaultRouter()

router.register('file_upload', ImageView)

urlpatterns = [] + router.urls