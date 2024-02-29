
from rest_framework import generics
from products.models.groups import Group
from students.serializer.users import RegistrationSerializer
from django.contrib.auth.models import User



users = User.objects.all()



class RegistrationView(generics.CreateAPIView):
  queryset =  users
  serializer_class = RegistrationSerializer