from django.shortcuts import render
from workers_api_app.models import Worker, Job, Paradigm
# Create your views here.


def workers_list(request):
    workers = Worker.objects.all().order_by('first_name')
    jobs = Job.objects.all()
    paradigms = Paradigm.objects.all()
    return render(request, 'workers_web_app/workers_list.html', {'workers': workers, 'jobs': jobs})

