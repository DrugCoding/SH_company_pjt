from django.urls import path
from . import views

app_name = 'notices'

urlpatterns = [
    path('', views.index, name='index')
]