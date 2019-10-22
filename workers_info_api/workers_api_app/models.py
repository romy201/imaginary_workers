from django.db import models

# Create your models here.


class Paradigm(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Job(models.Model):
    name = models.CharField(max_length=50)
    paradigms = models.ManyToManyField(Paradigm)

    def __str__(self):
        return self.name


class Worker(models.Model):
    worker_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    salary = models.CharField(max_length=50)
    jobs = models.ManyToManyField(Job)

    def __str__(self):
        return self.name
