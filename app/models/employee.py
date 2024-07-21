from .base import BaseModel
from django.db import models

class Employee(BaseModel):
    name = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='employees/', null=True, blank=True)
    designation = models.CharField(max_length=255, null=True, blank=True)
    team  = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    facebookLink= models.URLField(null=True, blank=True)
    linkedinLink= models.URLField(null=True, blank=True)
    twitterLink= models.URLField(null=True, blank=True)
    instagramLink= models.URLField(null=True, blank=True)

    def __str__(self):
        return str(self.name) + "-" + str(self.designation)