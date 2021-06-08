from django.db import models

# Create your models here.
class ResumeImage(models.Model):
  id = models.AutoField(primary_key=True)
  img = models.ImageField(upload_to='images', default=None)