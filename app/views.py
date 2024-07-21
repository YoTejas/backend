from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from middleware.auth import *
from .models.property import *
from .models.image import *
from .models.amenity import *
from .models.city import *
from .models.video import *
from .models.employee import *
from .models.partner import *
from .models.statistic import *
from .models.testimonial import *
from .models.section import *
from .models.contact import *
from .models.header import *
from .models.page import *
from .models.gallery import *
from .models.values import *
from .serializers import *
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import render

# Create your views here.


@api_view(['GET'])
def get_properties(request):
    try:
        properties = Property.objects.all()
        if "floor" in request.GET:
            properties = properties.filter(floor__floor=request.GET['floor'])
        if "locality" in request.GET:
            properties = properties.filter(locality=request.GET['locality'])
        if "city" in request.GET:
            properties = properties.filter(city=request.GET['city'])
        if "area" in request.GET:
            lower, upper = request.GET['area'].split('-')
            properties = properties.filter(area__gte=lower, area__lte=upper)
        if "rooms" in request.GET:
            properties = properties.filter(rooms=request.GET['rooms'])

        # Order the properties by status and rank from the Floor model
        status_order = {'AVAILABLE': 0, 'SOLD': 1, 'UNDER_CONSTRUCTION': 2}
        properties = sorted(properties, key=lambda x: (
            status_order.get(x.propertyStatus, 3), -x.floor.rank))

        paginator = PageNumberPagination()
        paginator.page_size = 10
        if request.GET.get('page_size'):
            paginator.page_size = int(request.GET.get('page_size'))
        result_page = paginator.paginate_queryset(properties, request)
        serializer = PropertySerializer(result_page, many=True)

        return Response({"message": "Properties fetched successfully", "properties": serializer.data})

    except Exception as e:
        return Response({"error": str(e)}, status=500)


@api_view(['GET'])
def get_property(request, id):
    try:
        property = Property.objects.get(id=id)
        serializer = PropertySerializer(property)
        return Response({"message": "Property fetched successfully", "property": serializer.data})

    except Exception as e:
        return Response({"error": str(e)}, status=500)


def visualizer(request, pk):
    property = Property.objects.get(pk=pk)
    return render(request, 'visualizer.html', {'property': property})


@api_view(['GET'])
def get_cities(request):
    cities = City.objects.all().order_by('name')
    serializer = CitySerializer(cities, many=True)
    data = serializer.data
    for city in data:
        city['localities'] = LocalitySerializer(Locality.objects.filter(city=city["id"]).order_by('name'), many=True).data
    return Response({"message": "Cities fetched successfully", "cities": data}, status=200)


@api_view(['GET'])
def get_partners(request):
    try:
        partners = Partner.objects.filter(is_active=True)
        serializer = PartnerSerializer(partners, many=True)
        return Response({"message": "Partners fetched successfully", "partners": serializer.data})

    except Exception as e:
        return Response({"error": str(e)}, status=500)


@api_view(['GET'])
def get_employees(request):
    try:
        employees = Employee.objects.filter(is_active=True)
        serializer = EmployeeSerializer(employees, many=True)
        return Response({"message": "Employees fetched successfully", "employees": serializer.data})

    except Exception as e:
        return Response({"error": str(e)}, status=500)


@api_view(['GET'])
def get_statistics(request):
    try:
        statistics = Statistic.objects.filter(to_show=True)
        serializer = StatisticSerializer(statistics, many=True)
        return Response({"message": "Statistics fetched successfully", "statistics": serializer.data})

    except Exception as e:
        return Response({"error": str(e)}, status=500)

@api_view(['GET'])
def get_testimonials(request):
    try:
        testimonials = Testimonial.objects.all()
        serializer = TestimonialSerializer(testimonials, many=True)
        return Response({"message": "Testimonials fetched successfully", "testimonials": serializer.data})

    except Exception as e:
        return Response({"error": str(e)}, status=500)
    
@api_view(['GET'])
def get_sections(request):
    try:
        sections = Section.objects.all()
        serializer = SectionSerializer(sections, many=True)
        return Response({"message": "Sections fetched successfully", "sections": serializer.data})
    except Exception as e:
        return Response({"error": str(e)}, status=500)
    
@api_view(['GET'])
def get_contacts(request):
    try:
        contact = Contact.objects.all()
        serializer = ContactSerializer(contact, many=True)
        return Response({"message": "Contact fetched successfully", "contacts": serializer.data})
    except Exception as e:
        return Response({"error": str(e)}, status=500)
    
@api_view(['POST'])
def send_message(request):
    try:
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Message sent successfully"})
        return Response(serializer.errors, status=400)
    except Exception as e:
        return Response({"error": "Internal Server Error"}, status=500)
    
@api_view(['GET'])
def header_media(request):
    try:
        media = HeaderMedia.objects.filter(title="Background").first()
        serializer = HeaderMediaSerializer(media)
        return Response(serializer.data, status=200)
    except Exception as e:
        return Response({"error": str(e)}, status=500)
    
@api_view(['GET'])
def get_pages(request):
    try:
        pages = Page.objects.all()
        serializer = PageSerializer(pages, many=True)
        return Response({"message": "Pages fetched successfully", "pages": serializer.data})
    except Exception as e:
        return Response({"error": str(e)}, status=500)
    
@api_view(['GET'])
def get_gallery(request):
    try:
        galleries = Gallery.objects.filter(to_show=True).order_by('position')
        serializer = GallerySerializer(galleries, many=True)
        return Response({"message": "Galleries fetched successfully", "galleries": serializer.data})
    except Exception as e:
        return Response({"error": str(e)}, status=500)
    
@api_view(['GET'])
def get_values(request):
    try:
        values = Values.objects.all()
        serializer = ValuesSerializer(values, many=True)
        return Response({"message": "Values fetched successfully", "values": serializer.data})
    except Exception as e:
        return Response({"error": str(e)}, status=500)


@api_view(['GET'])
def get_floors(request):
    try:
        floors = Floor.objects.all().order_by('rank')
        serializer = FloorSerializer(floors, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({"error": str(e)}, status=500)
    
@api_view(['GET'])
def get_bhks(request):
    try:
        bhks = Property.objects.all().order_by('rooms').values('rooms').distinct()
        return Response({"bhks": bhks})
    except Exception as e:
        return Response({"error": str(e)}, status=500)
