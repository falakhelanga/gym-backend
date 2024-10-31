from rest_framework import generics, permissions
from .models import ExerciseCategory
from .serializers import ExerciseCategorySerializer


class ExerciseCategoryView(generics.ListCreateAPIView):
    queryset = ExerciseCategory.objects.all()
    serializer_class = ExerciseCategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class ExerciseCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExerciseCategory.objects.all()
    serializer_class = ExerciseCategorySerializer
    permission_classes = [permissions.IsAuthenticated]







