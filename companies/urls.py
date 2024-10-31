from django.urls import path
from . import views

urlpatterns = [
path("",view=views.CompanyListCreateView.as_view(),name="company-list-create"),
path("<int:pk>/",view=views.CompanyRetrieveUpdateDestroyView.as_view(),name="company-retrieve-update-destroy"),
]
