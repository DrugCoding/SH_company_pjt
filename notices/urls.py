from django.urls import path
from . import views

app_name = 'notices'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'), # create라는 주소로 요청하면, create라는 VIEW 함수를 응답
    path('<int:pk>/', views.detail, name='detail')
]