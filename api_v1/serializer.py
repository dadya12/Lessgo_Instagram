from rest_framework import serializers
from webapp.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'author', 'image', 'description', 'comments', 'created', 'users_likes']
        read_only_fields = ('id', 'users_likes', 'author')
