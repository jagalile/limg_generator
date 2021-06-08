from django.contrib import admin
from .models import *

# Register your models here.
class DetectionImageAdmin(admin.ModelAdmin):
  list_display = ('id', 'img', 'done', 'review')
  list_editable = ('review', )
  #list_filter = ('label', )
  search_fields = ['label']

class DetectionLabelAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'color')
  #list_editable = ('review', )
  list_filter = ('name', )
  search_fields = ['name']

class DetectionAdmin(admin.ModelAdmin):
  list_display = ('id', 'img', 'label')
  #list_editable = ('review', )
  list_filter = ('img', 'label')
  search_fields = ['img', 'label']

class CoordsAdmin(admin.ModelAdmin):
  list_display = ('id', 'detection', 'x1', 'y1', 'x2', 'y2')
  #list_editable = ('review', )
  #list_filter = ('label', )
  #search_fields = ['label']

admin.site.register(DetectionImage, DetectionImageAdmin)
admin.site.register(DetectionLabel, DetectionLabelAdmin)
admin.site.register(Detection, DetectionAdmin)
admin.site.register(Coords, CoordsAdmin)