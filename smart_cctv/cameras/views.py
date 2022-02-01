from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

from .models import Camera

import json

@login_required
# Create your views here.
def index(request):
  cameras = Camera.objects.all()[:15]
  context= {
    'cameras': cameras
  }

  return render(request, 'cameras/index.html', context)

@login_required
def create(request):
  return render(request, 'cameras/create.html')

@login_required
def edit(request, id):
  camera = get_object_or_404(Camera, pk=id)
  return render(request, 'cameras/edit.html', { 'camera': camera })

@login_required
def search(request):
  q = request.GET['q']
  cameras = Camera.objects.filter(description__contains=q).values('description', 'url')

  return JsonResponse({
    'cameras': json.dumps(list(cameras))
  }, safe=False)


@login_required
@api_view(['POST'])
def store(request):
  try:
    body = request.data
    camera = Camera.objects.create(description=body['description'], url=body['url'])

    return JsonResponse({
      'message': 'Successfully created a camera.'
    }, safe=False) 
  except Exception as e:
    return JsonResponse({
      'message': str(e)
    }, safe=False, status=400)

@login_required
@api_view(['PATCH'])
def update(request, id):
  try:
    body = request.data
    camera = Camera.objects.get(pk=id)
    camera.url = body['url']
    camera.description = body['description']
    camera.save()

    return JsonResponse({
      'message': 'Successfully updated a camera.'
    }, safe=False)
  except Camera.DoesNotExist:
    return JsonResponse({
      'message': 'Camera does not exists.'
    }, safe=False, status=400)
  except Exception as e:
    return JsonResponse({
      'message': str(e)
    }, safe=False, status=400)

@login_required
@api_view(['DELETE'])
def delete(request, id):
  try:
    camera = Camera.objects.get(pk=id)
    camera.delete()

    return JsonResponse({
      'message': 'Successfully deleted a camera.'
    })
  except Camera.DoesNotExist:
    return JsonResponse({
      'message': 'Camera does not exists.'
    }, safe=False, status=400)
  except Exception as e:
    return JsonResponse({
      'message': str(e)
    }, safe=False, status=400)