from .base import BaseModel
from django.db import models


class Contact(BaseModel):
    phone = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    facebookLink = models.URLField(null=True, blank=True)
    instagramLink = models.URLField(null=True, blank=True)
    twitterLink = models.URLField(null=True, blank=True)
    youtubeLink = models.URLField(null=True, blank=True)
    linkedinLink = models.URLField(null=True, blank=True)
    addressLine1 = models.TextField(null=True, blank=True)
    addressLine2 = models.TextField(null=True, blank=True)
    city = models.TextField(null=True, blank=True)
    pincode = models.CharField(max_length=255, null=True, blank=True)
    googleMapIframeLink = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.city) + "-" + str(self.id)
