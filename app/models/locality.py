from django.db import models
from .base import BaseModel
from .city import City

class Locality(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="localities")

    def __str__(self):
        return str(self.name) + "-" + str(self.city.name)
