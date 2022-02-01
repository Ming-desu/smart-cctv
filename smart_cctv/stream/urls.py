from django.http.response import StreamingHttpResponse
from django.urls import path

from . import views

from .views import VideoCamera, gen

urlpatterns = [
  path('', views.index, name='stream.index'),
  path('video_feed/', views.video_feed, name="stream.video")
]