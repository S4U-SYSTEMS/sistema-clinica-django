from django.urls import path
from .views import index

app_name = 'base'
urlpatterns = [
    path('', index, name='index')
]
