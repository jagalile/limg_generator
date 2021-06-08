from django.db import models

# Create your models here.
class SegmentationImage(models.Model):
  id = models.AutoField(primary_key=True)
  img = models.CharField(max_length=200, default=None)
  review = models.BooleanField(default=False)