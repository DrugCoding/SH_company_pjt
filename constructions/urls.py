from django.urls import path
from . import views

app_name = 'constructions'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:c_pk>/', views.detail, name='detail'),
    path('<int:c_pk>/update/', views.update, name='update'),
    path('<int:c_pk>/delete/', views.delete, name='delete'),
    path('<int:c_category_pk>/category/', views.c_category, name='c_category'),
]
