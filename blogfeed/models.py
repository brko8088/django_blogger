from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
  title = models.CharField(max_length=255)
  title_tag = models.CharField(max_length=255, default="the blogger")
  # header_image = models.ImageField(null=True, blank=True, upload_to="images/")
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  body = models.TextField()
  date_added = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title + ' | ' + str(self.author)

  def get_absolute_url(self):
    return reverse("home")