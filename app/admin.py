from django.contrib import admin
from .models.property import Property
from .models.amenity import Amenity
from .models.image import Image
from .models.city import City
from .models.video import Video
from .models.employee import Employee
from .models.partner import Partner
from .models.statistic import Statistic
from .models.testimonial import Testimonial
from .models.section import Section
from .models.contact import Contact
from .models.message import Message
from .models.locality import Locality
from .models.header import HeaderMedia
from .models.page import Page
from .models.gallery import Gallery
from .models.values import Values
from .models.floor import Floor
from django.http import HttpResponse
import csv

class PropertyAdmin(admin.ModelAdmin):
    filter_horizontal = ('images', 'amenities')

def download_csv(modeladmin, request, queryset):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=messages.csv'

    writer = csv.writer(response)
    writer.writerow(["first_name", "last_name", "email", "phone", "role", "message", "addressed"])
    for s in queryset:
        writer.writerow([s.first_name, s.last_name, s.email, s.phone, s.role, s.message, s.addressed])
    
    return response


class MessageAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone", "role", "message", "addressed")
    actions = [download_csv]


# Register your models here.
admin.site.register(Amenity)
admin.site.register(Image)
admin.site.register(Property, PropertyAdmin)
admin.site.register(City)
admin.site.register(Video)
admin.site.register(Employee)
admin.site.register(Partner)
admin.site.register(Statistic)
admin.site.register(Testimonial)
admin.site.register(Section)
admin.site.register(Contact)
admin.site.register(Message, MessageAdmin)
admin.site.register(Locality)
admin.site.register(HeaderMedia)
admin.site.register(Page)
admin.site.register(Gallery)
admin.site.register(Values)
admin.site.register(Floor)
