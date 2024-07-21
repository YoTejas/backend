from .base import BaseModel
from django.db import models

class Image(BaseModel):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.image) + "-" + str(self.id)