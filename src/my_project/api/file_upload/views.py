from rest_framework.viewsets import ModelViewSet

from my_project.file_upload.models import Image


class ImageView(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = Image
