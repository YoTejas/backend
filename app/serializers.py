from rest_framework import serializers
from .models.property import *
from .models.amenity import *
from .models.image import *
from .models.video import *
from .models.city import *
from .models.employee import *
from .models.partner import *
from .models.statistic import *
from .models.testimonial import *
from .models.section import *
from .models.contact import *
from .models.message import *
from .models.header import *
from .models.locality import *
from .models.page import *
from .models.gallery import *
from .models.values import * 
from .models.floor import *


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'


class AmenitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Amenity
        fields = '__all__'


class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floor
        fields = '__all__'


class PropertySerializer(serializers.ModelSerializer):

    images = serializers.SerializerMethodField(read_only=True)
    amenities = serializers.SerializerMethodField(read_only=True)
    city = serializers.SerializerMethodField(read_only=True)
    locality = serializers.SerializerMethodField(read_only=True)
    floor = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Property
        fields = '__all__'

    def get_images(self, obj):
        return ImageSerializer(obj.images.all(), many=True).data

    def get_amenities(self, obj):
        return AmenitySerializer(obj.amenities.all(), many=True).data

    def get_city(self, obj):
        return CitySerializer(obj.city).data
    
    def get_locality(self, obj):
        return LocalitySerializer(obj.locality).data

    def get_floor(self, obj):
        return obj.floor.floor


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'


class PartnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Partner
        fields = '__all__'


class StatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        fields = '__all__'

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        exclude = ('addressed',)


class HeaderMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeaderMedia
        fields = '__all__'

class LocalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Locality
        fields = '__all__'

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'

class GallerySerializer(serializers.ModelSerializer):
    
    images = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Gallery
        fields = '__all__'

    def get_images(self, obj):
        return ImageSerializer(obj.images.all(), many=True).data
    
class ValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Values
        fields = '__all__'