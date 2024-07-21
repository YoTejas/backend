from .base import BaseModel
from django.db import models
from .amenity import Amenity
from .image import Image
from .city import City
from .locality import Locality
from .floor import Floor

PROPERTY_STATUS = (
    ('SOLD', 'SOLD'),
    ('UNDER_CONSTRUCTION', 'UNDER_CONSTRUCTION'),
    ('AVAILABLE', 'AVAILABLE'),
)

class Property(BaseModel):
    # floor = models.CharField(max_length=255, null=True, blank=True)
    floor = models.ForeignKey(Floor, on_delete=models.SET_NULL,
                              null=True, blank=True, related_name='properties')
    city =  models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True, related_name='properties')
    locality = models.ForeignKey(Locality, on_delete=models.SET_NULL, null=True, blank=True, related_name='properties')
    landmarkName = models.CharField(max_length=255, null=True, blank=True)
    landmarkCoordinates = models.CharField(
        max_length=255, null=True, blank=True, help_text="format: Latitude, Longitude , eg:-25.290747656764527, 23.480395215646162 (to get this right click on the map and select')")
    partialAddress = models.CharField(max_length=255, null=True, blank=True)
    completeAddress = models.TextField(null=True, blank=True)
    rooms = models.CharField(max_length=255, null=True, blank=True)
    area = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    floorDetails = models.TextField(null=True, blank=True)
    amenities = models.ManyToManyField(Amenity, related_name='amenities', blank=True)
    images = models.ManyToManyField(Image, related_name='images', blank=True)
    panorama = models.FileField(upload_to='panoramas/', null=True, blank=True)
    # proprtyStatus field for property status like sold, finished, under construction, available etc
    propertyStatus = models.CharField(
        max_length=255, choices=PROPERTY_STATUS, default='AVAILABLE')
    locationCoordinates = models.CharField(
        max_length=255, null=True, blank=True, help_text="format: Latitude, Longitude , eg:-25.290747656764527, 23.480395215646162 (to get this right click on the map and select')")





    def __str__(self):
        return str(self.floor) + "-" + str(self.locality) + "-" + str(self.city) + "-" + str(self.id)