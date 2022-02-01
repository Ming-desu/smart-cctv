from django.db import models

# Create your models here.
class Camera(models.Model):
  url = models.CharField(max_length=256)
  description = models.CharField(max_length=256)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)