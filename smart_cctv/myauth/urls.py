from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='auth.index'),
  path('login/', views.login_user, name='auth.login'),
  path('logout/', views.logout_user, name='auth.logout')
]
