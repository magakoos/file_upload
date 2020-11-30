from rest_framework import serializers

from my_project.file_upload.models import Image


class Image(serializers.ModelSerializer):
    """Серализатор для загрузки картинок."""
    image = serializers.ImageField(
        required=True,
    )

    class Meta:
        model = Image
        fields = (
            'image',
        )
