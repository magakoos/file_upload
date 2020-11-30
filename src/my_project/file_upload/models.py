from django.db import models
from sorl.thumbnail import ImageField


class Image(models.Model):
    image = ImageField(
        upload_to='img/',
        verbose_name='Оригинальное изображение',
    )

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'
