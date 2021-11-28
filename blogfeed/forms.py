from django import forms
from .models import Category, Post

choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
  choice_list.append(item)

class CreatePostForm(forms.ModelForm):
  class Meta:
    model=Post
    fields=('title', 'title_tag', 'category', 'author', 'body')
    widgets = {
      'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is Title Placeholder'}),
      'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
      'category': forms.Select(choices=choice_list, attrs={'class': 'form-control', 'placeholder': choices}),
      'author': forms.Select(attrs={'class': 'form-control'}),
      'body': forms.Textarea(attrs={'class': 'form-control'}),
    }

class UpdatePostForm(forms.ModelForm):
  class Meta:
    model=Post
    fields=('title', 'title_tag', 'category', 'author', 'body')
    widgets = {
      'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is Title Placeholder'}),
      'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
      'category': forms.Select(choices=choice_list, attrs={'class': 'form-control', 'placeholder': choices}),
      'author': forms.Select(attrs={'class': 'form-control'}),
      'body': forms.Textarea(attrs={'class': 'form-control'}),
    }