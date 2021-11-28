from django.urls import path, include
from .views import HomeView, PostView, CreatePostView

urlpatterns = [
  path('', HomeView.as_view(), name="home"),
  path('post/<int:pk>', PostView.as_view(), name="post_details"),
  path('create_post/', CreatePostView.as_view(), name="create_post"),
]