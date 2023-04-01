from django.urls import path
from . import views

app_name = 'constructions'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('part01/', views.part01, name='part01'),
    path('part02/', views.part02, name='part02'),
    path('part03/', views.part03, name='part03'),
    path('part04/', views.part04, name='part04'),
    path('part05/', views.part05, name='part05'),
    path('part06/', views.part06, name='part06'),
    path('part07/', views.part07, name='part07'),
    path('part08/', views.part08, name='part08'),
    path('part09/', views.part09, name='part09'),
]
