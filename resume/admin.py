from django.contrib import admin
from .models import *

# Register your models here.
class ResumeImageAdmin(admin.ModelAdmin):
  list_display = ('id', 'img')

admin.site.register(ResumeImage, ResumeImageAdmin)