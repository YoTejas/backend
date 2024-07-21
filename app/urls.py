from django.urls import path
from .views import *

urlpatterns = [
    path('properties/', get_properties, name='get_properties'),
    path('property/<int:id>/', get_property, name='get_property'),
    path('visualizer/<int:pk>/', visualizer, name='visualizer'),
    path('cities/', get_cities, name='get_cities'),
    path('partners/', get_partners, name='get_partners'),
    path('employees/', get_employees, name='get_employees'),
    path('statistics/', get_statistics, name='get_statistics'),
    path('testimonials/', get_testimonials, name='get_testimonials'),
    path('sections/', get_sections, name='get_sections'),
    path('contacts/', get_contacts, name='get_contacts'),
    path('message/', send_message, name='send_message'),    
    path('headermedia/', header_media, name='get_header_media'),
    path('pages/', get_pages, name='get_pages'),
    path('gallery/', get_gallery, name='get_gallery'),
    path('values/', get_values, name='get_values'),
    path('floors/', get_floors, name='get_floors'),
    path('bhks/', get_bhks, name='get_bhks'),
]
