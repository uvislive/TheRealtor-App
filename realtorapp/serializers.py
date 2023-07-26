from dataclasses import fields
from rest_framework import serializers
from .models import *

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields=('firstname','lastname','nickname','email')


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields= ("HomeId","HomeName","HomeCat","HomePrice","HomeImage")


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model= Like
        fields= ("count","homename")