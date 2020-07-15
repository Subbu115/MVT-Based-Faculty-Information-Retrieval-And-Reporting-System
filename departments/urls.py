from sys import path

from django.conf.urls import url
from django.urls import include

from departments import admin
from . import views

urlpatterns = [


    url(r'insertdept/$' , views.insert_dept,name='insertdept'),
    ]
