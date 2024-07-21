from .base import BaseModel
from django.db import models
from .image import Image

class Gallery(BaseModel):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    images = models.ManyToManyField(Image, related_name='gallery_image', blank=True)
    to_show = models.BooleanField(default=True)
    position = models.IntegerField(default=0)

    def __str__(self):
        return str(self.title)