from django import forms
from webapp.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'description']
