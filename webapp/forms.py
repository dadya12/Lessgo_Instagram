from django import forms
from webapp.models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'description']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
