from django.urls import path
from .views import UserProfileView, UserRegisterView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('profile_page/', UserProfileView.as_view(), name="profile_page"),
]
