from rest_framework import serializers
from products.models.groups import Group

class GroupSerializer(serializers.ModelSerializer):
  class Meta:
    model = Group
    fields=  ('__all__')
    
