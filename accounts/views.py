from django.contrib.auth import login, get_user_model
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, reverse, get_object_or_404
from django.views.generic import CreateView, DetailView, UpdateView, ListView, View
from accounts.forms import MyUserCreationForm, MyUserChangeForm, SearchForm
from django.contrib.auth.views import PasswordChangeView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin


class RegistrationView(CreateView):
    model = get_user_model()
    form_class = MyUserCreationForm
    template_name = 'registration.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_page = self.request.GET.get('next')
        if not next_page:
            next_page = self.request.POST.get('next')
        if not next_page:
            next_page = reverse('webapp:home')
        return next_page


class UserDetailView(LoginRequiredMixin, DetailView):
    template_name = 'user_detail.html'
    model = get_user_model()
    context_object_name = 'user_obj'


class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'user_change.html'
    model = get_user_model()
    context_object_name = 'user_obj'
    form_class = MyUserChangeForm

    def get_queryset(self):
        return super().get_queryset().filter(id=self.request.user.id)

    def get_success_url(self):
        return reverse('accounts:user_detail', kwargs={'pk': self.object.pk})


class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'user_password_change.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.pk != self.kwargs.get('pk'):
            return HttpResponseForbidden()
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('accounts:user_detail', kwargs={'pk': self.request.user.pk})


class UserSearchView(LoginRequiredMixin, ListView):
    template_name = 'users_search.html'
    model = get_user_model()
    context_object_name = 'users'

    def get_queryset(self):
        queryset = super().get_queryset()
        form = SearchForm(self.request.GET)
        if form.is_valid():
            queryset = queryset.filter(Q(first_name__icontains=form.cleaned_data['search']) |
                                       Q(email__icontains=form.cleaned_data['search']) |
                                       Q(username__icontains=form.cleaned_data['search']))
        return queryset


class UserSubscriptionView(View):
    def post(self, request, pk, *args, **kwargs):
        user = get_object_or_404(get_user_model(), pk=pk)
        if user in request.user.subscription_users.all():
            request.user.subscription_users.remove(user)
        else:
            request.user.subscription_users.add(user)
        request.user.following_count = request.user.subscription_users.count()
        user.subscription_count = user.sub_users.count()
        request.user.save()
        user.save()
        return redirect('accounts:user_detail', pk=pk)
