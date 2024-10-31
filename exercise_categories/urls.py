from .views import ExerciseCategoryView, ExerciseCategoryDetail
from django.urls import path

urlpatterns = [
    path('exercise_categories/', ExerciseCategoryView.as_view(), name='exercise_categories'),
    path('exercise_categories/<int:pk>/', ExerciseCategoryDetail.as_view(), name='exercise_category'),
]
