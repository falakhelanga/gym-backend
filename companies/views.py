
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import CompanySerializer

from .models import Company

class CompanyListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer












