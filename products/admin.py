from django.contrib import admin
from products.models import products, groups,lessons
from products.models.products import Employee

@admin.register(groups.Group)
class GroupAdmin(admin.ModelAdmin):
  list_display = ('id', 'name',)
  



@admin.register(products.Product)
class Admin(admin.ModelAdmin):
  list_display = ('id', 'name',)

@admin.register(lessons.Lesson)
class LessonAdmin(admin.ModelAdmin):
  list_display = ('id', 'name',)

@admin.register(products.Employee)
class EmployeeAdmin(admin.ModelAdmin):
  list_display = ('id','user','product')