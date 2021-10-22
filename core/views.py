from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from core.models import * 
from core.serializers import *

# Create your views here.
class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()
    
    def perform_create(self, serializer):
        return serializer.save(self.request.user) 

        
