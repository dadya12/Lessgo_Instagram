from django.contrib.auth import login, get_user_model
from django.shortcuts import redirect, reverse
from django.views.generic import CreateView, DetailView, UpdateView, ListView
from accounts.forms import MyUserCreationForm, MyUserChangeForm, SearchForm
from django.contrib.auth.views import PasswordChangeView
from django.db.models import Q


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


class UserDetailView(DetailView):
    template_name = 'user_detail.html'
    model = get_user_model()
    context_object_name = 'user_obj'


class UserUpdateView(UpdateView):
    template_name = 'user_change.html'
    model = get_user_model()
    context_object_name = 'user_obj'
    form_class = MyUserChangeForm

    def get_queryset(self):
        return super().get_queryset().filter(id=self.request.user.id)

    def get_success_url(self):
        return reverse('accounts:user_detail', kwargs={'pk': self.object.pk})


class UserPasswordChangeView(PasswordChangeView):
    template_name = 'user_password_change.html'

    def get_success_url(self):
        return reverse('accounts:user_detail', kwargs={'pk': self.request.user.pk})


class UserSearchView(ListView):
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
