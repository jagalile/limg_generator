from django.shortcuts import render
from pathlib import Path
import os

def main(request):

  apps = ['Classification', 'Detection', 'Segmentation']
  
  return render(
        request,
        'main.html',
        context={'apps': apps},
    )
