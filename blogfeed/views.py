from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post


class HomeView(ListView):
  model = Post
  template_name = 'home.html'

class PostView(DetailView):
  model = Post
  template_name = 'post_details.html'

class CreatePostView(CreateView):
  model = Post
  template_name = 'create_post.html'
  fields = '__all__'