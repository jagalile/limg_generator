from django.db import models

# Create your models here.
class ClassificationImage(models.Model):
  id = models.AutoField(primary_key=True)
  img = models.CharField(max_length=200, default=None)
  label = models.CharField(max_length=100, null=True, blank=True)
  review = models.BooleanField(default=False)