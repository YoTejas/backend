from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from users.serializers import *
from copy import deepcopy
import datetime
import jwt
from django.contrib.auth import authenticate
from middleware.auth import *
from .models.client import *
from .models.agent import *
from django.core import mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags


SECRET = 'SECRET'
ALGO = 'HS256'

@api_view(['POST'])
def register(request):
    try:
        data = {
            'username': request.data['email'],
            'first_name': request.data['first_name'],
            'last_name': request.data['last_name'],
            'email': request.data['email'],
            'password': request.data['password'],
        }

        if User.objects.filter(username=data['username']).exists():
            return Response({"error": "This email is already in use. Kindly use a different email."}, status=400)

        user = UserSerializer(data=data)

        if user.is_valid():
            user = user.save()
            user.is_active = False
            user.save()
        else:
            return Response({"error": "Please check entered data"}, status=400)
        
        data = {
            'user': user.id,
            'phone': request.data['phone'],
        }

        if request.data['role'] == 'client':

            client = ClientSerializer(data=data)
            if client.is_valid():
                client.save()
            else:
                return Response({"error": "Error occurred in client creation"}, status=400)
            
        elif request.data['role'] == 'agent':

            agent = AgentSerializer(data=data)
            if agent.is_valid():
                agent.save()
            else:
                return Response({"error": "Error occurred in agent creation"}, status=400)
            
        else:
            return Response({"error": "Invalid Role"}, status=400)
        
        return Response({"message": "User registered successfully. Please, wait for activation."}, status=201)
    
    except Exception as e:
        return Response({"error": "Internal Server Error"}, status=500)
    
@api_view(['POST'])
def login(request):
    try:

        user = User.objects.filter(username=request.data['email']).first()

        if user is None:
            return Response({'error': 'Incorrect Email'}, status=400)
        
        if user.is_active == False:
            return Response({'error': 'Account not activated yet'}, status=400)
        
        user = authenticate(username=request.data['email'], password=request.data['password'])

        if user is None:
            return Response({'error': 'Incorrect Password'}, status=400)
        
        client = Client.objects.filter(user=user).first()
        agent = Agent.objects.filter(user=user).first()

        payload = {
                'id': user.id,
                'role': 'client' if client else 'agent',
                'exp': datetime.datetime.now() + datetime.timedelta(days=1)
            }
        token = jwt.encode(payload, SECRET, algorithm=ALGO)

        return Response({
            'message': 'Logged in successfully', 
            'token': token, 
            'role': 'client' if client else 'agent', 
            'user': {
                    'id': user.id,
                    'username': user.username,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'email': user.email,
                    'phone': client.phone if client else agent.phone
                }
            })
    except Exception as e:
        return Response({"error": "Internal Server Error"}, status=500)
    
@api_view(['PATCH'])
@authentication_classes([Authentication])
def edit(request):
    try:
        user = request.user
        client = Client.objects.filter(user=user).first()
        agent = Agent.objects.filter(user=user).first()
        if "phone" in request.data:
            if client:
                client.phone = request.data["phone"]
                client.save()
            elif agent:
                agent.phone = request.data["phone"]
                agent.save()
            else:
                return Response({"error": "Your registration is incomplete"}, status=401)
        data = deepcopy(request.data)
        data.pop("phone", None)
        if "email" in request.data:
            obj = User.objects.filter(username=request.data['email']).first()
            if obj and obj.id != user.id:
                return Response({"error": "This email is already in use. Kindly use a different email."}, status=400)
            data['username'] = request.data['email']
        serializer = UserSerializer(user, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User updated successfully", "user": serializer.data})
        else:
            return Response({"error": "Entered Field's are Invalid"}, status=400)
    except Exception as e:
        return Response({"error": "Internal Server Error"})

@api_view(['POST'])
def forgot_password(request):
    try:
        user = User.objects.filter(username=request.data['email']).first()
        if user:
            payload = {
                'id': user.id,
                'exp': datetime.datetime.now() + datetime.timedelta(days=1)
            }
            token = jwt.encode(payload, SECRET, algorithm=ALGO)
            html_template = 'forgot_password.html'
            html_message = render_to_string(html_template, { 'frontend_link': settings.FRONTEND_URL, 'token':token, 'first_name': user.first_name, 'last_name': user.last_name })
            plain_message = strip_tags(html_message)
            mail.send_mail('Vista Residency: Password Reset Link', plain_message, settings.EMAIL_HOST_USER, [user.email], html_message=html_message, fail_silently=False)
            return Response({'message': 'Password reset link has been sent to your email.'})
        else:
            return Response({'error': 'Email not found'}, status=400)
    except Exception as e:
        return Response({"error": "Internal Server Error"})
    
@api_view(['POST'])
def reset_password(request):
    try:
        payload = jwt.decode(request.data['token'], SECRET, algorithms=[ALGO])
        user = User.objects.get(id=payload['id'])
        print(user, request.data['password'])
        user.set_password(request.data['password'])
        user.save()
        return Response({'message': 'Password reset successfully'})
    except Exception as e:
        return Response({"error": "Internal Server Error"})

@api_view(['GET'])
@authentication_classes([Authentication])
def get_profile(request):
    try:
        user = request.user
        client = Client.objects.filter(user=user).first()
        agent = Agent.objects.filter(user=user).first()
        return Response({
            'user': {
                'id': user.id,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'phone': client.phone if client else agent.phone
            }
        })
    except Exception as e:
        return Response({"error": "Internal Server Error"})