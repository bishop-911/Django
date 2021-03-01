from django.urls import path
from . import views

urlpatterns=[
    path('', views.my_form),
    path('display', views.index),
    path('api_student', views.DetailApiView.as_view()),
    path('api_parent', views.Parent_DetailApiView.as_view()),
]