from rest_framework import serializers
from products.models.lessons import Lesson

class LessonSerializer(serializers.ModelSerializer):
  class Meta:
    model = Lesson
    fields=  ('__all__')
    
