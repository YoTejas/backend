from .base import BaseModel
from django.db import models

class Partner(BaseModel):
    title = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='partners/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.title)