from django.urls import path, include
from .views import HomeView, PostView, CreatePostView, UpdatePostView, DeletePostView, CreateCategoryView, CategoryView, CategoryListView, LikeView, AddCommentView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('post/<int:pk>', PostView.as_view(), name="post_details"),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name="post_delete"),
    path('post_create/', CreatePostView.as_view(), name="post_create"),
    path('post/update/<int:pk>', UpdatePostView.as_view(), name="post_update"),
    path('category_create/', CreateCategoryView.as_view(), name="category_create"),
    path('category/<str:category_name>/', CategoryView, name='category'),
    path('category_list/', CategoryListView, name='category_list'),
    path('like/<int:pk>', LikeView, name='post_like'),
    path('post/<int:pk>/add_comment/',
         AddCommentView.as_view(), name="add_comment"),
]
