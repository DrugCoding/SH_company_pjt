from django.urls import path
from . import views

app_name = 'performances'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:p_pk>/', views.detail, name='detail'),
    path('<int:p_pk>/update/', views.update, name='update'),
    path('<int:p_pk>/delete/', views.delete, name='delete'),
]
