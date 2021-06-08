from django.shortcuts import render
from classification.models import *
from django.db.models import Count

# Create your views here.
def resume(request):

  total_images = ClassificationImage.objects.all().count()
  total_review_images = ClassificationImage.objects.filter(review=True).count()
  total_labels = ClassificationImage.objects.filter(label__isnull=False).count()
  class_labels = ClassificationImage.objects.all().values('label').annotate(total=Count('label'))
  class_labels_reviwed = ClassificationImage.objects.filter(review=True).values('label').annotate(total=Count('label'))

  print()
  print()
  print(class_labels_reviwed)
  print()
  print()

  return render(
    request,
    'resume/resume.html',
    context={'class_labels':class_labels, 'class_labels_reviwed':class_labels_reviwed, 'total_images':total_images, 'total_review_images':total_review_images, 'total_labels':total_labels},
  )