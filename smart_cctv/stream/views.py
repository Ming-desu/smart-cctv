from django.http import HttpResponse, StreamingHttpResponse
from django.shortcuts import render
from django.views.decorators import gzip
from django.contrib.auth.decorators import login_required

from cameras.models import Camera

import cv2
import threading
from timeit import default_timer as timer

from win10toast import ToastNotifier

class VideoCamera(object):
  def __init__(self, source = 0, camera = 'Camera 1'):
    self.camera = camera
    self.net = cv2.dnn_DetectionModel('yolov4-tiny-cctv.cfg', 'yolov4-tiny-cctv_best.weights')
    self.net.setInputSize(416, 416)
    self.net.setInputScale(1.0 / 255)
    self.net.setInputSwapRB(True)
    self.source = source
    self.video = cv2.VideoCapture(self.source)
    (self.grabbed, self.frame) = self.video.read() 
    self.classes = []
    self.confidences = []
    self.boxes = []
    self.names = ['knife', 'pistol']
    self.toast = ToastNotifier()

    self.thread = threading.Thread(target=self.update, args=())
    self.thread.start()

    self.notification_thread = threading.Thread(target=self.notify, args=())
    self.notification_thread.start()

    self.last_notification = None

  def __del__(self):
    self.video.release()
    self.thread.stop()
    self.notification_thread.stop()

  def notify(self):
    while True:
      if len(self.classes) > 0:
        print("Attention!", "A " + str(self.names[self.classes[0]]) + " found by the system at " + self.camera + ".")
        current_time = timer()
        if self.last_notification is None or current_time - self.last_notification > 3 and (len(self.confidences) > 0 and self.confidences[0] >= 0.5):
          self.toast.show_toast("Attention!", "A " + str(self.names[self.classes[0]]) + " found by the system at " + self.camera + ".")
          self.last_notification = current_time

        if self.last_notification is None:
          self.last_notification = timer()

  def update(self):
    while self.video.isOpened():
      (self.grabbed, self.frame) = self.video.read()

  def get_frame(self):
    # _, jpg = cv2.imencode('.jpg', self.frame)

    # return jpg.tobytes()

    if self.grabbed and int(self.video.get(cv2.CAP_PROP_POS_FRAMES)) % 12 == 0:
      classes, confidences, boxes = self.detect(self.frame)
      self.classes = classes
      self.confidences = confidences
      self.boxes = boxes

    if self.grabbed:
      current_frame = self.draw(self.frame)
      _, jpeg = cv2.imencode('.jpg', current_frame)
      
      return jpeg.tobytes()
    
    self.video.release()

  def detect(self, image):
    return self.net.detect(image, confThreshold=0.3, nmsThreshold=0.4)

  def draw(self, image):
    for i in range(len(self.classes)):
      class_name = self.names[self.classes[i]]
      confidence = self.confidences[i]
      box = self.boxes[i]

      label = '%.2f' % confidence
      label = '%s: %s' % (class_name, label)
      labelSize, baseLine = cv2.getTextSize(label, cv2.FONT_HERSHEY_COMPLEX, 0.5, 1)
      left, top, width, height = box
      top = max(top, labelSize[1])
      cv2.rectangle(image, box, color=(0, 255, 0), thickness=5)
      cv2.rectangle(image, (left, top - labelSize[1]), (left + labelSize[0], top + baseLine), (255, 255, 255), cv2.FILLED)
      cv2.putText(image, label, (left, top), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0))

    return image

def gen(camera: VideoCamera):
  while True:
    frame = camera.get_frame()
    yield(b'--frame\r\n'
          b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def my_yielder(frame):
  yield(b'--frame\r\n'
          b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@login_required
@gzip.gzip_page
# Create your views here.
def index(request):
  cameras = Camera.objects.all()[:15]
  return render(request, 'stream/index.html', { 'cameras': cameras })

def video_feed(request):
  cam = VideoCamera(request.GET['url'], request.GET['camera'])

  if cam is not None:
    while True:
      return StreamingHttpResponse(gen(cam), content_type='multipart/x-mixed-replace; boundary=frame')