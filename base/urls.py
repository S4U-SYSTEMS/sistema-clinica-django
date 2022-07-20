from django.urls import path
from base.views import index

app_name = 'base'
urlpatterns = [
    path('', index, name='index')
]
