from .base import BaseModel
from django.db import models

class Message(BaseModel):

    ROLE_CHOICES = (
        ('client', 'client'),
        ('agent', 'agent'),
    )

    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    role = models.CharField(max_length=255, choices=ROLE_CHOICES, default='client')
    message = models.TextField(null=True, blank=True)
    addressed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.first_name) + "-" + str(self.last_name) + "-" + str(self.id)