from task_2.models import MainPage

from django.contrib import admin
from image_cropping import ImageCroppingMixin

class MainPageAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

admin.site.register(MainPage, MainPageAdmin)

