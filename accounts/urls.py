from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import RegistrationView, UserDetailView, UserUpdateView, UserPasswordChangeView, UserSearchView, \
    UserSubscriptionView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('<int:pk>', UserDetailView.as_view(), name='user_detail'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    path('<int:pk>/password/change/', UserPasswordChangeView.as_view(), name='password'),
    path('users/search/', UserSearchView.as_view(), name='search'),
    path('users/subscription/<int:pk>/', UserSubscriptionView.as_view(), name='subscription'),
]
