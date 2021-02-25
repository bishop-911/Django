from django.shortcuts import render
from django.http import HttpResponse
from .models  import Detail
from .models  import Parent_Detail
from rest_framework import viewsets, renderers
from .serializers import DetailSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core import serializers
from .serializers import Parent_DetailSerializer
from .forms import MyForm, MyForm1

# Create your views here.

# def index(request):
#     return render(request, 'students/index.html')
#     # return HttpResponse("STUDENTS PAGE")


def my_form(request):
  if request.method == "POST":
    form = MyForm(request.POST)
    form1 = MyForm1(request.POST)
    if form.is_valid() and form1.is_valid():
      form.save()
      form1.save()
  else:
      form = MyForm()
      form1 = MyForm1()
  return render(request, 'students/index.html', {'form': form, 'form1':form1})

# def my_form1(request):
#   if request.method == "POST":
#     form = MyForm1(request.POST)
#     if form.is_valid():
#       form.save()
#   else:
#       form = MyForm1()
#   return render(request, 'students/index.html', {'form': form})


class DetailApiView(APIView):

    def get(self, request, format=None):
        query = Detail.objects.all()
        serializer = DetailSerializer(query, many=True)
        # return Response({'items': serializer.data})
        return Response({'data': serializer.data})


class Parent_DetailApiView(APIView):

    def get(self, request, format=None):
        query = Parent_Detail.objects.all()
        serializer = Parent_DetailSerializer(query, many=True)
        # return Response({'items': serializer.data})
        return Response({'parent_data': serializer.data})
