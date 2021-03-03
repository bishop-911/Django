from django.shortcuts import render
from django.http import HttpResponse
from .models  import Detail, Parent_Detail, Login_Detail
from rest_framework import viewsets, renderers
from .serializers import DetailSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core import serializers
from .serializers import Parent_DetailSerializer
from .forms import MyForm, MyForm1, LoginForm

# Create your views here.

def index(request):
    if request.method == "GET":
        all_data = Detail.objects.all()
        details = {
            'data':all_data
        }
        return render(request, 'students/display.html', details)

    # return HttpResponse("STUDENTS PAGE")

# def display(request):
#     if request.method == "GET":
#         all_data = Detail.objects.all()
#         details = {
#             'data':all_data
#         }
#         return render(request, 'students/display.html', details)

    # return HttpResponse("STUDENTS PAGE")


def my_form(request):

  if request.method == "POST":
    form1 = MyForm(request.POST)
    form2 = MyForm1(request.POST)
    if form1.is_valid() and form2.is_valid():
      form1.save()
      form2.save()
    #   return render(request, 'students/index.html', {'form': form, 'form1':form1})
    # return render(request, 'students/index.html', {'form': form, 'form1':form1})
  
  else:
      form1 = MyForm()
      form2 = MyForm1()
  return render(request, 'students/index.html', {'form1': form1, 'form2':form2})


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


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
    
        name = request.POST.get('username')
        pswd = request.POST.get('password')
        all_data = Login_Detail.objects.all()
        details = {
            'data': all_data
        }
        # ctr = sum(map(len, data.values("username")))

        form_data = {
            'username': name,
            'password': pswd,
        }

        name_d = all_data.values("username")
        pswd_d = all_data.values("password")
        print(name, pswd, name_d, pswd_d)
        # str1 = str(name_d)
        print(type(name_d))
        print(type(name))
        print(details, form_data)
        # print(str1)

        # for key, value in details.iteritems():
        #     if name in value:
        #         print (key)
        # for key in all_data:
        #     print (all_data[key])    

        if (details == form_data):
            print("hello")
            # return HttpResponse("welcome user")    
    
        
        # form.save()

        
    else:
        form = LoginForm()
     
    return render(request, 'students/login.html', {'form': form})