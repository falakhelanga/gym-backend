from rest_framework import generics
from .models import Exercise
from .serializers import ExerciseSerializer
from rest_framework.permissions import IsAuthenticated



class ExerciseListCreate(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

class ExerciseRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

    

