from django.shortcuts import render, redirect
from pathlib import Path
from .models import *
from detection.models import *
from segmentation.models import *
from resume.models import *
from django.db.models import Count
from django.views.decorators.csrf import csrf_exempt

import os

# Create your views here.
def classification(request):

  labels = ClassificationImage.objects.all().values('label').annotate(total=Count('label'))
  image = ClassificationImage.objects.filter(label__isnull=True).values_list('img', flat=True).first()
  images_left = ClassificationImage.objects.filter(label__isnull=True).count()

  if image is not None:
    url = image
  else:
    url = 0

  return render(
    request,
    'classification/classification.html',
    context={'labels':labels, 'url':url, 'images_left':images_left},
  )

@csrf_exempt
def createLabel(request):
  if request.method == 'POST':
    data = request.POST

    ClassificationImage.objects.filter(img=data['url']).update(label=data['label'])

    return redirect('classification')

def reload_form(request):
  return redirect('classification')

@csrf_exempt
def uploadImages(request):
  if request.method == 'POST' and request.FILES['myfile']:
    files = request.FILES.getlist('myfile')
    for file in files:
      obj = ResumeImage.objects.create(img=file)
      obj.save()
      filename = str(getattr(obj, 'img'))
      obj = ClassificationImage.objects.create(label=None, img=os.path.join('media', filename))
      obj.save()
      obj = DetectionImage.objects.create(img=os.path.join('media', filename))
      obj.save()
      obj = SegmentationImage.objects.create(img=os.path.join('media', filename))
      obj.save()

    return redirect('classification')