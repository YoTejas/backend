from django.db import models
from .base import BaseModel

class Page(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    route = models.CharField(max_length=255, null=True, blank=True)
    to_show = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
