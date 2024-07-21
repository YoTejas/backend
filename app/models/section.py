from .base import BaseModel
from django.db import models


class Section(BaseModel):
    page = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    heading = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='sections/', null=True, blank=True)

    def __str__(self):
        return str(self.name) + "-" + str(self.id)
