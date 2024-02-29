from django.shortcuts import render
from rest_framework import generics
from products.models.products import Product
from products.models.lessons import Lesson
from products.serializer.lessons import LessonSerializer
from products.serializer.products import ProductSerializer

class ProductView(generics.ListAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  permission_classes = ['AllowAny']

class LessonsAPIView(generics.ListAPIView):
  queryset = Lesson.objects.all()
  serializer_class = LessonSerializer
  permission_classes = ['IsOwnerOrReadOnly']