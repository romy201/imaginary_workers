from django.shortcuts import render
from rest_framework import viewsets
from .models import Paradigm, Job, Worker
from .serializers import ParadigmSerializer, JobSerializer, WorkerSerializer

# Create your views here.


class ParadigmView(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer


class JobView(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class WorkerView(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
