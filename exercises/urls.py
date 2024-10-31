from .views import ExerciseListCreate,ExerciseRetrieveUpdateDestroy
from django.urls import path

urlpatterns = [
    path('', ExerciseListCreate.as_view(), name='exercise-list-create'),
    path('<int:pk>', ExerciseRetrieveUpdateDestroy.as_view(), name='exercise-retrieve-update-destroy'),
]