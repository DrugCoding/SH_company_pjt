from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class Construction(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = ProcessedImageField(
        blank=False,
        processors=[ResizeToFill(550, 500)],
        format="JPEG",
        options={"quality": 80},
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 시공종목 리스트
    c_list = models.ForeignKey('constructions.C_Category', on_delete=models.CASCADE, null=True)
    # 공사진행 여부
    ing_finish_choice = (
        ('0', '진행중'),
        ('1', '완료'),
    )
    ing_finish = models.CharField(null=True, max_length=3, choices=ing_finish_choice)

class C_Category(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name