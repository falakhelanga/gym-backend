from rest_framework import serializers
from companies.models import Company
from .models import Exercise
from users.models import User

class ExerciseSerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)
    class Meta:
        model = Exercise
        fields = '__all__'
