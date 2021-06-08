from django.db import models
from colorfield.fields import ColorField

# Create your models here.
class DetectionImage(models.Model):
  id = models.AutoField(primary_key=True)
  img = models.CharField(max_length=200, default=None)
  done = models.BooleanField(default=False)
  review = models.BooleanField(default=False)

  def __str__(self):
    return self.img

class DetectionLabel(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100, default=None)
  color = ColorField(default='#FF0000', null=True, blank = True)

  def __str__(self):
    return self.name


class Detection(models.Model):
  id = models.AutoField(primary_key=True)
  img = models.ForeignKey(DetectionImage, on_delete=models.CASCADE)
  label = models.ForeignKey(DetectionLabel, on_delete=models.CASCADE)

  def __str__(self):
    complete_name = str(self.img) + ' - ' + str(self.label)
    return complete_name


class Coords(models.Model):
  id = models.AutoField(primary_key=True)
  detection = models.ForeignKey(Detection, on_delete=models.CASCADE)
  x1 = models.FloatField()
  y1 = models.FloatField()
  x2 = models.FloatField()
  y2 = models.FloatField()