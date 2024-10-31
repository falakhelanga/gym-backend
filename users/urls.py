from django.urls import path
from .views import UserCreateView, UserListView,TokenObtainPairView,UpdateUserView,ProfileView,CompleteRegistration,UserCompanyView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # path('', UserListView.as_view(), name='users-list'),
    path('', UserCreateView.as_view(), name='users-create'),
    path('<int:pk>', UpdateUserView.as_view(), name='users-update'),
    path('profile', ProfileView.as_view(), name='users-profile'),
    path('complete-registration',CompleteRegistration.as_view(), name='complete-registration'),
    path('sign-in', TokenObtainPairView.as_view(), name='signin'),
    path('company',UserCompanyView.as_view(),name='user-company'),
    path('refresh', TokenRefreshView.as_view(), name='refresh'),
]