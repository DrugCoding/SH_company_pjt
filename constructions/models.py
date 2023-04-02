from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class Constructions(models.Model):
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
    c_list = models.ForeignKey('constructions:C_Category', on_delete=models.CASCADE,)

class C_Category(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name