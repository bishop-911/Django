from django.shortcuts import render
from django.http import HttpResponse
from .models import Course
from rest_framework import viewsets, renderers
from .serializers import CourseSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core import serializers

# Create your views here.


def index(request):

    courses = Course.objects.all()
    print("number of courses....", len(courses))
    return render(request, 'home/index.html')
    # return HttpResponse("numnber of courses...", len(courses))


class CourseApiView(APIView):

    def get(self, request, format=None):
        query = Course.objects.all()
        serializer = CourseSerializer(query, many=True)
        # return Response({'items': serializer.data})
        return Response({'data': serializer.data})
