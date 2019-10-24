from rest_framework import serializers
from .models import Paradigm, Job, Worker


class ParadigmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paradigm
        fields = ('id', 'url', 'name')


class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job
        fields = ('id', 'url', 'name', 'paradigms')


class WorkerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Worker
        fields = ('id', 'url', 'worker_id', 'first_name', 'last_name', 'phone', 'salary', 'jobs', 'image')


