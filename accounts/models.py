from django.contrib.auth.models import AbstractUser
from django.db import models

GENDER_CHOICES = [
    ('Male', 'Мужчина'),
    ('Female', 'Женщина'),
    ('Other', 'Другое')
]


class MyUser(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="Email", max_length=254)
    avatar = models.ImageField(upload_to='avatars/', verbose_name='Avatar')
    info = models.TextField(verbose_name='Info', max_length=500, blank=True, null=True)
    phone = models.CharField(max_length=20, verbose_name="Phone Number", blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, verbose_name="Gender", blank=True, null=True, max_length=20)
    publication_count = models.PositiveIntegerField(default=0, verbose_name='Publications')
    subscription_count = models.PositiveIntegerField(default=0, verbose_name='Subscriptions')
    following_count = models.PositiveIntegerField(default=0, verbose_name='Following')

    def __str__(self):
        return f'{self.username}{self.gender}'
