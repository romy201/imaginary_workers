from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.workers_list, name='list-of-workers')
]
