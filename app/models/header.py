from .base import BaseModel
from django.db import models

class HeaderMedia(BaseModel):
    MEDIA_TYPES = [
        ('image', 'Image'),
        ('video', 'Video'),
    ]
    media_type = models.CharField(max_length=255, choices=MEDIA_TYPES, default='image')
    file = models.FileField(upload_to='header/', null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.media_type) + "-" + str(self.title)