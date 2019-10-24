from django.contrib import admin
from django.urls import path
from . import views

app_name = 'workers_web_app'
urlpatterns = [
    path('', views.workers_list, name='list-of-workers')
]
