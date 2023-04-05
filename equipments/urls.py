from django.urls import path
from . import views

app_name = 'equipments'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:equipment_pk>/', views.detail, name='detail'),
    path('<int:equipment_pk>/update/', views.update, name='update'),
    path('<int:equipment_pk>/delete/', views.delete, name='delete')
]
