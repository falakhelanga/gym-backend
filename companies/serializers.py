from rest_framework import serializers
from users.models import User
from brands.models import Brand
from .models import Company

class CompanySerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(queryset=Brand.objects.all(),required=False)
    class Meta:
        model = Company
        fields = '__all__'