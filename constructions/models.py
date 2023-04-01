from django.db import models

# Create your models here.
class Constructions(models.Model):
    title = models.CharField(max_length=50) 