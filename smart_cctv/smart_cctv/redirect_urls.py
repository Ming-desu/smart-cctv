from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import path, reverse

def check(request):
  if request.user.is_authenticated:
    return HttpResponseRedirect(reverse('stream.index'))
  else:
    return HttpResponseRedirect(reverse('auth.index'))

urlpatterns = [
  path('', check)
]