from django.contrib import admin
from products.models import products, groups,lessons

@admin.register(groups.Group)
class GroupAdmin(admin.ModelAdmin):
  list_display = ('id', 'name',)
  



@admin.register(products.Product)
class OfferAdmin(admin.ModelAdmin):
  list_display = ('id', 'name',)


@admin.register(lessons.Lesson)
class GroupAdmin(admin.ModelAdmin):
  list_display = ('id', 'name',)

@admin.register(products.Employee)
class GroupAdmin(admin.ModelAdmin):
  list_display = ('id',)