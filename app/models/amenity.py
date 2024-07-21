from .base import BaseModel
from django.db import models

class Amenity(BaseModel):
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.name) + "-" + str(self.id)