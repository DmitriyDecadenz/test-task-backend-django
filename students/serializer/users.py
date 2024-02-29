from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class RegistrationSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields=  ('username','email','password')
    
