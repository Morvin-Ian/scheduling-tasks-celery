from django.shortcuts import render
from django.http import HttpResponse
from .tasks import func_test
def index(request):
    func_test.delay()
    return HttpResponse("Done")
