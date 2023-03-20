from django.urls import path
from . import views

app_name = 'equipments'

urlpatterns = [
    path('', views.index, name='index'),
]
