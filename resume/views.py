from django.shortcuts import render, redirect
from classification.models import *
from detection.models import *
from django.db.models import Count
from django.views.decorators.csrf import csrf_exempt
import zipfile, json

# Create your views here.
def resume(request):

  total_images = ClassificationImage.objects.all().count()
  total_review_images = ClassificationImage.objects.filter(review=True).count()
  total_labels_class = ClassificationImage.objects.filter(label__isnull=False).count()
  total_labels_detect = DetectionLabel.objects.all().count()
  total_labels = total_labels_class + total_labels_detect
  class_labels = ClassificationImage.objects.all().values('label').annotate(total=Count('label'))
  class_labels_reviwed = ClassificationImage.objects.filter(review=True).values('label').annotate(total=Count('label'))

  detection_labels = []
  total_done_detections = DetectionImage.objects.filter(done=True)
  total_label_detections_id = Detection.objects.filter(img__in=total_done_detections)
  total_label_detections = total_label_detections_id.values_list('label')
  total_label_names = DetectionLabel.objects.filter(id__in=total_label_detections).values_list('name', flat=True)
  for label in total_label_names:
    bounding_boxes_detections = total_label_detections_id.filter(label__name=label)
    bounding_boxes = Coords.objects.filter(detection__in=bounding_boxes_detections).count()
    detection_labels.append([label, bounding_boxes])

  return render(
    request,
    'resume/resume.html',
    context={'class_labels':class_labels, 'class_labels_reviwed':class_labels_reviwed, 'total_images':total_images, 'total_review_images':total_review_images, 'total_labels':total_labels, 'detection_labels':detection_labels},
  )

@csrf_exempt
def downloadData(request):
  if request.method == 'POST':
    data = request.POST

    if data['type'] == 'class':
      images = ClassificationImage.objects.filter(label=data['label']).values_list('img', flat=True)

      file_compress(images, 'datastet_classification.zip')
    
    elif data['type'] == 'detect':
      images = Detection.objects.filter(label__name=data['label']).values_list('img', flat=True)
      images_url = DetectionImage.objects.filter(id__in=images).values_list('img', flat=True)

      dataset_info = {}
      for image in images_url:
        images = Detection.objects.filter(label__name=data['label'], img__img=image)
        coords = Coords.objects.filter(detection__in=images).values_list('x1', 'y1', 'x2', 'y2')
        dataset_info[image] = {}
        dataset_info[image][data['label']] = []
        for coord in coords:
          dataset_info[image][data['label']].append(coord)

        a_file = open("data.json", "w")
        a_file = json.dump(dataset_info, a_file)

      file_compress(images_url, 'dataset_detection.zip')

    return redirect('resume')

def file_compress(inp_file_names, out_zip_file):
  """
  function : file_compress
  args : inp_file_names : list of filenames to be zipped
  out_zip_file : output zip file
  return : none
  assumption : Input file paths and this code is in same directory.
  """
  # Select the compression mode ZIP_DEFLATED for compression
  # or zipfile.ZIP_STORED to just store the file
  compression = zipfile.ZIP_DEFLATED
  print(f" *** Input File name passed for zipping - {inp_file_names}")

  # create the zip file first parameter path/name, second mode
  print(f' *** out_zip_file is - {out_zip_file}')
  zf = zipfile.ZipFile(out_zip_file, mode="w")

  try:
    for file_to_write in inp_file_names:
      # Add file to the zip file
      # first parameter file to zip, second filename in zip
      print(' *** Processing file', file_to_write)
      zf.write(file_to_write, file_to_write, compress_type=compression)

  except FileNotFoundError as e:
    print(' *** Exception occurred during zip process', e)

  finally:
    # Don't forget to close the file!
    zf.close()