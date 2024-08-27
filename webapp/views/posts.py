from django.shortcuts import reverse, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from webapp.models import Post
from webapp.forms import PostForm
from django.http import JsonResponse


class PostListView(ListView, LoginRequiredMixin):
    template_name = 'home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            subscribed_users = self.request.user.subscription_users.all()
            subscribed_posts = Post.objects.filter(author__in=subscribed_users).order_by('-created')
            return subscribed_posts
        else:
            return Post.objects.none()


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'Posts/post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        self.request.user.publication_count += 1
        self.request.user.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accounts:user_detail', kwargs={'pk': self.request.user.pk})


class PostsLikeView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        if request.user in post.users_likes.all():
            post.users_likes.remove(request.user)
            liked = False
        else:
            post.users_likes.add(request.user)
            liked = True
        post.likes_count = post.users_likes.count()
        post.save()
        return JsonResponse({'count': post.likes_count, 'liked': liked})
