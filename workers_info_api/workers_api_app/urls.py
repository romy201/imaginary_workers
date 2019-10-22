from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register('workers', views.WorkerView)
router.register('jobs', views.JobView)
router.register('paradigms', views.ParadigmView)

urlpatterns = [
    path('', include(router.urls))
]
