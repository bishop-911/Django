from django import forms
from .models import Detail, Parent_Detail, Login_Detail
 
class MyForm(forms.ModelForm):
  class Meta:

    model = Detail
    fields = ["name", "roll_number", "class_standard",]
    labels = {'name': "Name", 'roll_number': "Roll Number", 'class_standard':"Class",}



class MyForm1(forms.ModelForm):
  class Meta:  

    model = Parent_Detail
    fields = ["parent_name", "age", "occupation",]
    labels = {'parent_name': "Father's Name", 'age': "Age", 'occupation':"Occupation",}


class LoginForm(forms.ModelForm):
  class Meta:

    model = Login_Detail
    fields = ["username", "password",]
    labels = {'username': "username", 'password': "password",}