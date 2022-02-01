from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='cameras.index'),
  path('create', views.create, name='cameras.create'),
  path('store', views.store, name='cameras.store'),
  path('search', views.search, name='cameras.search'),
  path('<int:id>/edit', views.edit, name='cameras.edit'),
  path('<int:id>/update', views.update, name='cameras.update'),
  path('<int:id>/delete', views.delete, name='cameras.delete')
]