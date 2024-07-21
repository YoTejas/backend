from .base import BaseModel
from django.db import models

class Video(BaseModel):
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return str(self.video) + "-" + str(self.id)