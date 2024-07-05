from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from image_cropping import ImageRatioField


class MainPage(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    header_image = models.ImageField(upload_to='images/')
    cropping = ImageRatioField('header_image', '900x400')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('page_detail', kwargs={'page_id': self.pk})


