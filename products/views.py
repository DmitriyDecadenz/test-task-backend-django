
from rest_framework import generics
from products.models.products import Employee, Product
from products.models.lessons import Lesson
from products.models.lessons import Lesson
from products.models.groups import Group
from products.serializer.employees import EmployeeSerializer
from products.serializer.lessons import LessonSerializer
from products.serializer.products import ProductSerializer
from products.serializer.groups import GroupSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny

class ProductAPIView(generics.ListAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  permission_classes = [AllowAny]

class LessonsAPIView(generics.ListAPIView):
  queryset = Lesson.objects.all()
  serializer_class = LessonSerializer
  permission_classes = [IsAuthenticated]
  

class CreateLessonsAPIView(generics.CreateAPIView):
  queryset = Lesson.objects.all()
  serializer_class = LessonSerializer
  permission_classes = [IsAdminUser]
  
class CreateGroupAPIView(generics.CreateAPIView):
  queryset = Group.objects.all()
  serializer_class = GroupSerializer
  permission_classes = [IsAdminUser]
  
class CreateEmployeeAPIView(generics.CreateAPIView):
  queryset = Employee.objects.all()
  serializer_class =  EmployeeSerializer
  permission_classes = [IsAdminUser]
  