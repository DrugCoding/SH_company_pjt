from django.urls import path
from . import views

app_name = 'performances'

urlpatterns = [
    path('example', views.example, name='example'),
    path('result', views.result, name='result'),
]
