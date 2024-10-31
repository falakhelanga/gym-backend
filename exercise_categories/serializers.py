from rest_framework import serializers
from .models import ExerciseCategory

class ExerciseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseCategory
        fields = '__all__'