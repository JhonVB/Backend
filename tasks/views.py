
from .models import Persona
from rest_framework import viewsets
from .serializers import PersonaSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class PersonasViewset(viewsets.ModelViewSet):
   permission_classes=[IsAuthenticated] 
   serializer_class = PersonaSerializer
   queryset= Persona.objects.all()

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(["GET"])
def getRoutes(request):
   routes=[
      "/token",
      "/api/token/refresh",
   ]
   return Response(routes)

from django.shortcuts import render
from .models import Persona
from rest_framework import viewsets
from .serializers import PersonaSerializer
# Create your views here.

class PersonasViewset(viewsets.ModelViewSet):
   serializer_class = PersonaSerializer
   queryset= Persona.objects.all()

