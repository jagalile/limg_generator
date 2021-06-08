from django.contrib import admin
from .models import *

# Register your models here.
class SegmentationImageAdmin(admin.ModelAdmin):
  list_display = ('id', 'img', 'review')
  list_editable = ('review', )
  #list_filter = ('label', )
  search_fields = ['label']

admin.site.register(SegmentationImage, SegmentationImageAdmin)