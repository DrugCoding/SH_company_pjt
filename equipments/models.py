from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings

# Create your models here.
class Equipment(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = ProcessedImageField(upload_to='media/images/', blank=True,
                            processors=[ResizeToFill(1200, 960)],
                            format='JPEG',
                            options={'quality': 80})
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class EquipImage(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    equip_img = models.ImageField('사진등록', upload_to='media/images/', blank=True, null=True) # 이미지 생략 가능