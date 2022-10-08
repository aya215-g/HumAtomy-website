"""HumAtomy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from BodySystems.views import retrievesystems
from BodySystems.views import AddNewSystem
from BodySystems.views import SystemDisplay
from BodySystems.views import AddNewDisease
from BodySystems.views import singmeUP
from BodySystems.views import  loginPage
from BodySystems.views import index
from BodySystems.views import retrieveddepartment
from BodySystems.views import AddNewDepartment
from BodySystems.views import respiratory, digestive, nervous,  home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about', retrievesystems , name='about'),
    path('NewSystem', AddNewSystem, name='add_new_system'),
    path('System/<int:sys_id>', SystemDisplay, name='display_system'),
    path('System/<int:sys_id>/NewDisease', AddNewDisease, name='add_new_disease'),
    path('signup', singmeUP , name='sign up to library'),
    path('signin', loginPage , name='sign in to library'),
    path('news', index, name='latest_news'),
    path('AllComments', retrieveddepartment, name='list_all_department'),
    path('NewComment', AddNewDepartment, name='add_new_department'),
    path('resp', respiratory, name='respiratory'),
    path('nervous.html', nervous, name='nervous'),
    path('home', home, name='home'),
    path('dig', digestive, name='digestive'),

 
]
