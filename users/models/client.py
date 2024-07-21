from .base import BaseModel
from django.db import models
from django.contrib.auth.models import User

class Client(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client')
    phone = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return "client-" + str(self.user.first_name) + "-" + str(self.id)