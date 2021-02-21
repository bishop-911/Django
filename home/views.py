from django.shortcuts import render
from django.http import HttpResponse
from .models import Course

# Create your views here.


def index(request):

    courses = Course.objects.all()
    print("number of courses....", len(courses))
    # return HttpResponse("HOME PAGE")
    return HttpResponse("numnber of courses...", len(courses))