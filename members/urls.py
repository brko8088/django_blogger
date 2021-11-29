from django.urls import path
from .views import UserProfileView, UserRegisterView, PasswordsChangeView
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('profile_page/', UserProfileView.as_view(), name="profile_page"),
    path('password/', PasswordsChangeView.as_view(), name="change_password"),
    path('password_success/', views.password_success, name="password_success"),
]
