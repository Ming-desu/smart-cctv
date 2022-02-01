from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='users.index'),
  path('create/', views.create, name='users.create'),
  path('store/', views.store, name='users.store'),
  path('search/', views.search, name='users.search'),
  path('<int:id>/edit', views.edit, name='users.edit'),
  path('<int:id>/update', views.update, name='users.update'),
  path('<int:id>/delete', views.delete, name='users.delete')
]
