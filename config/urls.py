
from django.contrib import admin
from django.urls import path,include
from products.views import ProductAPIView,LessonsAPIView,CreateGroupAPIView,CreateLessonsAPIView,CreateEmployeeAPIView
from students.views import CreateUserView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductAPIView.as_view()),
    path('reg/',CreateUserView.as_view(),),
    path('', include('rest_framework.urls',)),
    path('accounts/profile/', LessonsAPIView.as_view()),
    path('create/group/', CreateGroupAPIView.as_view()),
    path('create/lesson/', CreateLessonsAPIView.as_view()),
    path('add/employee',CreateEmployeeAPIView.as_view() )
  
    ]
