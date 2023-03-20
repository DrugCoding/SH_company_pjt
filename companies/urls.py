from django.urls import path
from . import views

app_name = 'companies'

urlpatterns = [
    path('', views.index, name='index'),
    path('greeting/', views.greeting, name='greeting'),
    path('history/', views.history, name='history'),
    path('patent/', views.patent, name='patent'),
    path('come/', views.come, name='come'),
]