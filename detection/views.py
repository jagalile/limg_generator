from django.shortcuts import render, redirect
from pathlib import Path
from .models import *
from classification.models import *
from segmentation.models import *
from resume.models import *
from django.db.models import Count
from django.views.decorators.csrf import csrf_exempt

import os, pathlib, random, json
from PIL import Image

# Create your views here.
def detection(request):

  #labels = ClassificationImage.objects.all().values('label').annotate(total=Count('label'))
  #image = DetectionImage.objects.filter(label__isnull=True).values_list('img', flat=True).first()
  #images_left = ClassificationImage.objects.filter(label__isnull=True).count()
  images_with_detections = DetectionImage.objects.filter(done=True)
  image = DetectionImage.objects.all().exclude(id__in=images_with_detections).first()
  images_left = DetectionImage.objects.all().exclude(id__in=images_with_detections).count()
  labels = DetectionLabel.objects.all().values('name', 'color').annotate(total=Count('name'))

  if image is not None:
    url = image
    absolute_url = str(pathlib.Path(__file__).parent.absolute()).split('detection')[0]
    image_path = os.path.join(absolute_url, str(url))
    im = Image.open(image_path)
    width, height = im.size
  else:
    url = 0

  return render(
    request,
    'detection/detection.html',
    #context={'labels':labels, 'url':url, 'images_left':images_left},
    context={'labels':labels,'url':url, 'images_left':images_left, 'img_width':im.size[0], 'img_height':im.size[1]},
  )

## CAMBIAR
@csrf_exempt
def createDetection(request):
  if request.method == 'POST':
    data = request.POST
    print()
    print()
    print(data['url'])
    print(data['label'])
    print(json.loads(data['boundingboxes']))
    print()
    print()

    img = DetectionImage.objects.get(img=data['url'])
    label = DetectionLabel.objects.get(name=data['label'])

    if Detection.objects.filter(label=label, img=img).exists():
      objDetection = Detection.objects.get(label=label, img=img)
    else:
      objDetection = Detection.objects.create(img=img, label=label)
      objDetection.refresh_from_db()

    for boxes in json.loads(data['boundingboxes']):
      x1 = boxes['x']
      y1 = boxes['y']
      x2 = boxes['x'] + boxes['width']
      y2 = boxes['y'] + boxes['height']
      Coords.objects.create(detection=objDetection, x1=x1, y1=y1, x2=x2, y2=y2)

    return redirect('detection')

def reload_form_detection(request):
  return redirect('detection')

@csrf_exempt
def createDetectionLabel(request):
  if request.method == 'POST':
    data = request.POST

    try:
      labels = DetectionLabel.objects.get(name=data['label'])
    except:
      obj = DetectionLabel.objects.create(name=data['label'], color=randomColor())
      obj.refresh_from_db()

    return redirect('detection')

@csrf_exempt
def nextImage(request):
  if request.method == 'POST':
    data = request.POST

    DetectionImage.objects.filter(img=data['url']).update(done=True)

    return redirect('detection')

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

    return redirect('detection')

def randomColor():
  r = lambda: random.randint(0,255)
  color = '#%02X%02X%02X' % (r(),r(),r())
  print(color)
  return color