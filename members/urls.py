from django.urls import path
from .views import UserProfileSettingsView, UserRegisterView, PasswordsChangeView, ShowProfilePage, EditProfilePageView, CreateProfilePageView
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('profile_settings/', UserProfileSettingsView.as_view(),
         name="profile_settings"),
    path('password/', PasswordsChangeView.as_view(), name="change_password"),
    path('password_success/', views.password_success, name="password_success"),
    path('<int:pk>/profile/', ShowProfilePage.as_view(), name="profile_page"),
    path('<int:pk>/profile_page_edit/', EditProfilePageView.as_view(),
         name="profile_page_edit"),
    path('profile_page_creation', CreateProfilePageView.as_view(),
         name="profile_page_creation")
]
