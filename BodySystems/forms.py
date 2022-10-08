from dataclasses import fields
from django import forms

from .models import System, Disease


#ADD NEW SYSTEM FORM

class SystemForm(forms.ModelForm):
    class Meta:
        model = System
        fields = '__all__'




#ADD NEW DISEASE FORM

class DiseaseForm(forms.ModelForm):
    class Meta:
        model = Disease
        exclude = ['sys']









#SIGNUP FORM

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class MySignUpForm(UserCreationForm) :
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField()
    phone = forms.IntegerField()

    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','phone','password1','password2')





#COMMENTS

from .models import Department

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        exclude = ['code']

