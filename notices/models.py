from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
from django.conf import settings


# Create your models here.
class Notice(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = ProcessedImageField(blank=True,
        processors=[Thumbnail(1920, 1080)],  
        format="JPEG", 
        options={"quality": 100},)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hit = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)