
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from students.views import RegistrationView
router = DefaultRouter()


urlpatterns = [
  path('reg/',RegistrationView.as_view(),),
  path('login/', include('rest_framework.urls',)),
  
]