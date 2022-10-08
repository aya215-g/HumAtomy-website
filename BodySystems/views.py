from django.shortcuts import render

# Create your views here.
from http.client import HTTPResponse
from inspect import formatargspec
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import System

def retrievesystems(request):
   x = System.objects.all()

   return render(request, 'BodySystems/aboutus.html',{'systems':x})



from .forms import SystemForm, DiseaseForm
from django.shortcuts import redirect






def AddNewSystem(request):
   form = SystemForm(request.POST or None, request.FILES or None)
   if form.is_valid():
      form.save()
      return redirect('aboutus')


   return render(request, 'BodySystems/new_system.html', {'form': form})





def SystemDisplay(request, sys_id):
    sys = System.objects.get(pk=sys_id)
    return render(request, 'BodySystems/System.html', {'System':sys})




def AddNewDisease(request, sys_id):
    sys = System.objects.get(pk=sys_id)

    form = DiseaseForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form = form.save(commit=False) #hya tmam bs mt7fzha4 dlw2ty 8er lma django yd5l el system
        form.sys = sys
        form.save()  #5las kda y7fzha
        return redirect('display_system', sys_id=sys_id)



    return render(request, 'BodySystems/new_disease.html', {'System':sys, 'form':form })













#LOGIN

from django.contrib import messages
from django.contrib.auth import authenticate , login ,logout
def loginPage(request):
    
    if request.method == 'POST' :
        username =request.POST.get('username')
        password =request.POST.get('password')
        user = authenticate(request, username=username , password =password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else :
            messages.info(request,'Username OR Password is Incorrect')
            
            


    context = {}
    return render(request,'BodySystems/login.html',context)






#SIGNUP


from django.contrib.auth import login
from .forms import MySignUpForm
def singmeUP(request):
    form = MySignUpForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        user = form.save()
        login(request,user)
        return redirect('home')
        
    return render(request,'BodySystems/sign.html',{'form':form})







#API OF NEWS

from django.shortcuts import render
import requests
from newsapi import NewsApiClient
import pandas as pd

def index(request):
    newsapi = NewsApiClient(api_key='8ffea00249a84f83a04a8afd43913361')
    top_headlines = newsapi.get_top_headlines(category='health', language='en', country='in')
    articles = top_headlines['articles']
    df=pd.DataFrame(articles)

    return render(request,'BodySystems/index3.html', {'data':df})










#COMMENTS

from .models import Department
def retrieveddepartment(request):
    x = Department.objects.all()
    return render(request, 'BodySystems/listallcomments.html', {'departments':x})



from .forms import DepartmentForm
from django.shortcuts import redirect
def AddNewDepartment(request):

    form = DepartmentForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('list_all_department')

    return render(request, 'BodySystems/new_comment.html', {'form':form})

















def respiratory(request):
    return render(request, 'BodySystems/respiratory.html', {})




def digestive(request):
    return render(request, 'BodySystems/digestive.html', {})




def nervous(request):
    return render(request, 'BodySystems/nervous.html', {})








def home(request):
    return render(request, 'BodySystems/home.html', {})







