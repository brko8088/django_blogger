from django.urls import path
from .views import UserProfileView, UserRegisterView, PasswordsChangeView, ShowProfilePage, EditProfilePageView
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('profile_edit/', UserProfileView.as_view(), name="profile_edit"),
    path('password/', PasswordsChangeView.as_view(), name="change_password"),
    path('password_success/', views.password_success, name="password_success"),
    path('<int:pk>/profile/', ShowProfilePage.as_view(), name="profile_page"),
    path('<int:pk>/edit_profile_page/',
         EditProfilePageView.as_view(), name="edit_profile_page"),
]
