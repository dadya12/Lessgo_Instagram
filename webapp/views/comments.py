from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView, CreateView, ListView
from webapp.models import Comment, Post
from webapp.forms import CommentForm


class CommentCreateView(LoginRequiredMixin, CreateView):
    template_name = 'Comments/comment_create.html'
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs.get('pk'))
        comment = form.save(commit=False)
        comment.post = post
        comment.author = self.request.user
        comment.save()
        return redirect('webapp:home')


class CommentDetailView(LoginRequiredMixin, ListView):
    model = Comment
    template_name = 'Comments/comment_detail.html'
    context_object_name = 'comments'

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('pk'))
        return Comment.objects.filter(post=post)


