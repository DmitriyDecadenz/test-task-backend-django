from django.urls import reverse_lazy
from rest_framework import generics

from students.serializer.users import RegistrationSerializer
from django.contrib.auth.models import User

from django.shortcuts import redirect

users = User.objects.all()



class RegistrationView(generics.CreateAPIView):
  queryset =  users
  serializer_class = RegistrationSerializer
  api_root = reverse_lazy('api-root')
