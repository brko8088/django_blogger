from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category, Post
from .forms import CreatePostForm, UpdatePostForm

class HomeView(ListView):
  model = Post
  template_name = 'home.html'
  ordering=['-post_date']
  # ordering=['-id']

class PostView(DetailView):
  model = Post
  template_name = 'post_details.html'

class CreatePostView(CreateView):
  model = Post
  form_class = CreatePostForm
  template_name = 'post_create.html'

class UpdatePostView(UpdateView):
  model = Post
  form_class = UpdatePostForm
  template_name = 'post_update.html'

class DeletePostView(DeleteView):
  model = Post
  template_name = 'post_delete.html'
  success_url = reverse_lazy('home')

class CreateCategoryView(CreateView):
  model = Category
  fields = '__all__'
  template_name = 'category_create.html'