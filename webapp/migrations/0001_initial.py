# Generated by Django 5.0.6 on 2024-07-30 06:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='posts', verbose_name='Image')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='Description')),
                ('likes', models.PositiveIntegerField(default=0, verbose_name='Likes')),
                ('comments', models.PositiveIntegerField(default=0, verbose_name='Comments')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
        ),
    ]
