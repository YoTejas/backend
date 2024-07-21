from django.db import models
from .base import BaseModel

class City(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    cityCoordinates = models.CharField(
        max_length=255, null=True, blank=True, help_text="coordinate of center of city, format: Latitude, Longitude , eg:-25.290747656764527, 23.480395215646162 (to get this right click on the map and select ')", default="-25.290747656764527, 23.480395215646162")
    mapZoom = models.IntegerField(
        null=True, blank=True, help_text="Map zoom level for city (ideally between 5 to 20) (default 12)", default=12)
    state = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
