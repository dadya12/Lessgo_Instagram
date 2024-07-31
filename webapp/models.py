from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', verbose_name='Author')
    image = models.ImageField(upload_to='posts', verbose_name='Image')
    description = models.TextField(verbose_name='Description', max_length=500, blank=True, null=True)
    likes = models.PositiveIntegerField(default=0, verbose_name='Likes')
    comments = models.PositiveIntegerField(default=0, verbose_name='Comments')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    users_likes = models.ManyToManyField(get_user_model(), related_name='users_likes')

    def __str__(self):
        return self.author.name
