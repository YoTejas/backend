from .base import BaseModel
from django.db import models


class Statistic(BaseModel):
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    value = models.IntegerField(null=True, blank=True)
    to_show = models.BooleanField(default=False)
    image = models.FileField(upload_to='statistics/', null=True, blank=True)

    def __str__(self):
        return str(self.name)
