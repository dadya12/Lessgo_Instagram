from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from webapp.models import Post
from .serializer import PostSerializer
from rest_framework.decorators import action
from api_v1.castom_perms.perms import IsOwnerOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(methods=['POST'], detail=True)
    def like(self, request, pk=None):
        post = self.get_object()
        post.users_likes.add(request.user)
        post.save()
        return Response({"post_liked": pk})

    @action(methods=['POST'], detail=True)
    def unlike(self, request, pk=None):
        post = self.get_object()
        post.users_likes.remove(request.user)
        post.save()
        return Response({"post_unliked": pk})
