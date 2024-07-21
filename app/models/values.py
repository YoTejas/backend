from .base import BaseModel
from django.db import models

class Values(BaseModel):
    title = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='values/', null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.title)