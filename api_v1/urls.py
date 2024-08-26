from rest_framework import routers
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from .views import PostViewSet


router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)


app_name = 'api_v1'

urlpatterns = [
    path('', include(router.urls)),
    path('login/', obtain_auth_token, name='login'),
]
