from rest_framework import generics
from .serializers import UserSerializer,MyTokenObtainPairSerializer
from companies.models import Company
from companies.serializers import CompanySerializer
from .models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.tokens import RefreshToken


class UserCreateView(generics.CreateAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        with transaction.atomic():
            user = serializer.save()  # Save the user instance within the transaction
            # Generate tokens for the created user
            refresh = RefreshToken.for_user(user)
            access = refresh.access_token
            # Add custom claims to the token payload
            access['is_registration_complete'] = False
            refresh['is_registration_complete'] = False

            # Return the response with tokens and user data
            return Response({
                'user': serializer.data,
                'access_token': str(access),
                'refresh_token': str(refresh),
            }, status=status.HTTP_201_CREATED)

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class SignInView(TokenObtainPairView):
    permission_classes = []
    authentication_classes = []
    serializer_class = MyTokenObtainPairSerializer

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)
        

class UpdateUserView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        with transaction.atomic():
            user = serializer.save()  # Save the user instance within the transaction

            # Generate tokens for the created user
            refresh = RefreshToken.for_user(user)
            access = refresh.access_token

            # Return the response with tokens and user data
            return Response({
                'user': serializer.data,
                'access_token': str(access),
                'refresh_token': str(refresh),
            }, status=status.HTTP_200_OK)




class CompleteRegistration(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        company_data = request.data.pop('company', None)  # Expecting a single company object
        user = request.user
        
        if company_data:
            company_data = CompanySerializer(data=company_data)
            if company_data.is_valid(raise_exception=True):
                company_data = company_data.save()
                user.company = company_data
        else:
            company = Company.objects.create(name=f"{user.first_name}\'s Company")
            user.company = company
        
            


        user.is_registration_complete = True
        user.save()

        # Generate tokens for the created user
        refresh = RefreshToken.for_user(user)
        access = refresh.access_token

        # Add custom claims to the token payload
        access['is_registration_complete'] = True
        refresh['is_registration_complete'] = True
        access['is_welcome_complete'] = False
        refresh['is_welwome_complete'] = False

        # Return the response with tokens and user data
        return Response({
            'user': UserSerializer(user).data,
            'access_token': str(access),
            'refresh_token': str(refresh),
        }, status=status.HTTP_200_OK)



class UserCompanyView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def get_object(self):
        user = self.request.user
        company = user.company
        return company

# class UserCompanyView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         user = request.user
#         company = user.company
#         serializer = CompanySerializer(company)
#         return Response(serializer.data)







    
    