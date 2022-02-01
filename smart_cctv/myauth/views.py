from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from rest_framework.decorators import api_view

# Create your views here.
def index(request):
  return render(request, 'auth/index.html')

@api_view(['POST'])
def login_user(request):
  body = request.data

  user = authenticate(request, username=body['username'], password=body['password'])

  if user is not None:
    login(request, user)
    
    return JsonResponse({
      'message': 'ok'
    }, safe=False)

  return JsonResponse({
    'message': 'Invalid username or password.'
  }, safe=False, status=400)

def logout_user(request):
  logout(request)
  return HttpResponseRedirect(reverse('auth.index'))
