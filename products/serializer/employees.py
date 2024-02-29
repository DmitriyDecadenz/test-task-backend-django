from rest_framework import serializers
from products.models.products import Employee
class EmployeeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Employee
    fields=  ('__all__')
    
