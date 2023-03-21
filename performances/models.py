from django.db import models
from django.conf import settings

# Create your models here.
class Performance(models.Model):
    title = models.CharField(max_length=50)
    start = models.DateField() # 공사 시작 날짜
    finish = models.DateField() # 공사 종료 날짜
    customer = models.CharField(max_length=50) # 발주처
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hit = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)