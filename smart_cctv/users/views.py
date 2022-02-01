from django.http.response import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

from django.contrib.auth.models import User
from .models import Profile

import json

@login_required
# Create your views here.
def index(request):
  users = User.objects.all().select_related('profile')[:15]
  return render(request, 'users/index.html', { 'users': users })

@login_required
def create(request):
  if request.user.profile.role != 'Admin':
    return HttpResponseRedirect(reverse('users.index')) 

  return render(request, 'users/create.html')

@login_required
def edit(request, id):
  if request.user.profile.role != 'Admin':
    return HttpResponseRedirect(reverse('users.index')) 

  users = User.objects.filter(pk=id).select_related('profile')

  if len(users) <= 0:
    raise Http404('User does not exists.')

  return render(request, 'users/edit.html', { 'mUser': users[0] })

@login_required
@api_view(['GET'])
def search(request):
  q = request.GET['q']
  users = User.objects.filter(username__contains=q).select_related('profile').values('username', 'first_name', 'last_name', 'profile__role', 'profile__sex')

  return JsonResponse({
    'users': json.dumps(list(users))
  }, safe=False)

@login_required
@api_view(['POST'])
def store(request):
  try:
    if request.user.profile.role != 'Admin':
      raise Exception('You do not have permsision to make this operation.')

    body = request.data
    user = User.objects.create(username=body['username'], first_name=body['first_name'], last_name=body['last_name'])
    user.set_password(body['password'])
    user.profile.sex = body['sex']
    user.profile.role = body['role']
    user.save()

    return JsonResponse({
      'message': 'Successfully created a user.'
    }, safe=False)
  except Exception as e:
    return JsonResponse({
      'message': str(e)
    }, safe=False, status=400) 

@login_required
@api_view(['PATCH'])
def update(request, id):
  try:
    if request.user.profile.role != 'Admin':
      raise Exception('You do not have permsision to make this operation.')

    body = request.data
    user = User.objects.get(pk=id)

    user.username = body['username']
    user.first_name = body['first_name']
    user.last_name = body['last_name']

    if body['password']:
      user.set_password(body['password'])

    profile = Profile(user=user, sex=body['sex'], role=body['role'])
    
    user.save()
    profile.save()

    return JsonResponse({
      'message': 'Successfully updated a user.'
    }, safe=False)
  except User.DoesNotExist:
    return JsonResponse({
      'message': 'User does not exists.'
    }, safe=False, status=400)
  except Exception as e:
    return JsonResponse({
      'message': str(e)
    }, safe=False, status=400)

@login_required
@api_view(['DELETE'])
def delete(request, id):
  try:
    if request.user.profile.role != 'Admin':
      raise Exception('You do not have permsision to make this operation.')

    user = User.objects.get(pk=id)

    if user.is_staff:
      raise Exception('You do not have permsision to make this operation.')

    user.delete()

    return JsonResponse({
      'message': 'Successfully deleted a user.'
    })
  except User.DoesNotExist:
    return JsonResponse({
      'message': 'User does not exists.'
    }, safe=False, status=400)
  except Exception as e:
    return JsonResponse({
      'message': str(e)
    }, safe=False, status=400)