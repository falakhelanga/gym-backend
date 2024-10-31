
from .models import User
from rest_framework import serializers
from companies.serializers import CompanySerializer
from drf_writable_nested.serializers import WritableNestedModelSerializer
from drf_writable_nested.mixins import UniqueFieldsMixin
from django.db import transaction
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



class UserSerializer(serializers.ModelSerializer):
    company = CompanySerializer(required=False)
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True, 'required': False},  
            'is_superuser': {'read_only': True},
            'is_staff': {'read_only': True},
            'is_active': {'read_only': True},
            'is_coach': {'read_only': True},
            'is_admin': {'read_only': True},
            'last_login': {'read_only': True},
            'date_joined': {'read_only': True},

        }


    def create(self, validated_data):
        with transaction.atomic():
            user = User.objects.create_user(**validated_data) 
            return user

    def update(self, instance, validated_data):
        with transaction.atomic():
            user = super().update(instance, validated_data)
            instance.save()
            return user
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Remove the password field if it exists in the representation
        representation.pop('password', None)
        return representation


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['is_registration_complete'] = user.is_registration_complete
        

        return token
