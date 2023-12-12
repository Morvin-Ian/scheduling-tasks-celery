from django.shortcuts import render
from django.http import HttpResponse
from core.tasks import func_test
from django_celery_beat.models import PeriodicTask,IntervalSchedule


def index(request):
    func_test.delay()
    return HttpResponse("Done")


def schedule_reminder(request):
    interval,created = IntervalSchedule.objects.get_or_create(
        every=30,
        period=IntervalSchedule.SECONDS
    )
    
    PeriodicTask.objects.create(
        interval=interval,
        name="my_schedule",
        task="core.tasks.func_test"
    )
    
    return HttpResponse("Task Scheduled")
