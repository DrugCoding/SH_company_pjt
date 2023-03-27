from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings

# Create your models here.
class Equipment(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = ProcessedImageField(upload_to='images/', blank=True,
                            processors=[ResizeToFill(1200, 960)],
                            format='JPEG',
                            options={'quality': 80})
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)