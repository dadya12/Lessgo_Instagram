from django.shortcuts import reverse, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from webapp.models import Post
from webapp.forms import PostForm
from django.http import JsonResponse


class LikePostsUser(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        public = get_object_or_404(Post, pk=pk)
        if request.user in public.users_likes.all():
            public.users_likes.remove(request.user)
        else:
            public.users_likes.add(request.user)
        return redirect('webapp:home')


class PostListView(ListView, LoginRequiredMixin):
    template_name = 'home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all()


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'Posts/post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
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
