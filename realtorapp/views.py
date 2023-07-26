from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
# Create your views here.


class LoginView(viewsets.ModelViewSet):
    queryset= Login.objects.all()
    serializer_class= LoginSerializer



class HomeView(viewsets.ModelViewSet):
    queryset= Home.objects.all()
    serializer_class= HomeSerializer


class LikeView(viewsets.ModelViewSet):
    queryset= Like.objects.all()
    serializer_class= LikeSerializer