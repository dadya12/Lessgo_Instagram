from django.urls import path
from webapp.views.posts import PostListView, PostCreateView, PostsLikeView, LikePostsUser

app_name = 'webapp'

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('posts/', PostCreateView.as_view(), name='post_create'),
    path('posts/like/<int:pk>/', PostsLikeView.as_view(), name='post_like'),
    path('posts/<int:pk>/like/', LikePostsUser.as_view(), name='user_likes'),
]
