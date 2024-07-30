from django.urls import path, include
from webapp.views import index

app_name = 'webapp'

urlpatterns = [
    path('', index, name='home'),
]
