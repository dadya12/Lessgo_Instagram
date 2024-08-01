from django.urls import path
from webapp.views.posts import PostListView, PostCreateView, PostsLikeView, LikePostsUser
from webapp.views.comments import CommentCreateView, CommentDetailView

app_name = 'webapp'

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('posts/', PostCreateView.as_view(), name='post_create'),
    path('posts/like/<int:pk>/', PostsLikeView.as_view(), name='post_like'),
    path('posts/<int:pk>/like/', LikePostsUser.as_view(), name='user_likes'),
    path('comments/<int:pk>/create/', CommentCreateView.as_view(), name='comment_create'),
    path('comments/<int:pk>/posts', CommentDetailView.as_view(), name='comment_detail')
]
