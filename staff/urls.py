from sys import path

from django.conf.urls import url
from django.urls import include

from staff import admin
from . import views

urlpatterns = [
    url(r'^$' , views.hp, name='homepage'),

    url(r'back/$' , views.backk,name='back'),
    url(r'logout/$',views.log,name='logout'),
    url(r'logout2/$',views.log2,name='logout2'),
    url(r'logout3/$',views.log3,name='logout3'),
    url(r'logout4/$', views.log4, name='logout4'),
    url(r'homee/$',views.homes,name='homee'),
    url(r'viewww/$',views.seens,name='viewww'),
    url(r'vieww/$',views.seen,name='vieww'),
    url(r'faculty/$',views.seener,name='faculty'),
    url(r'adddept/$' , views.insert_department,name='adddept'),
    url(r'addhod/$', views.insert_hod, name='addhod'),
    url(r'deptview/$' , views.depttview,name='deptview'),
    url(r'deptdelete/$' , views.dept_delete,name='deptdelete'),
    url(r'facultyhome/$' , views.faculty_home,name='facultyhome'),
    url(r'addpersonal/$' , views.insert_personal,name='addpersonal'),

    url(r'viewpersonal/$', views.view_personal, name='viewpersonal'),
    url(r'viewFaculty/$', views.view_Faculty, name='viewFaculty'),
    url(r'viewcourse/$', views.view_course, name='viewcourse'),
    url(r'viewReport/$', views.view_Report, name='viewReport'),
    url(r'addbachelor/$' , views.add_bachelor,name='addbachelor'),
    url(r'addmaster/$' , views.add_master,name='addmaster'),
    url(r'addphd/$' , views.add_phd,name='addphd'),
    url(r'addpublication/$' , views.add_publication,name='addpublication'),
    url(r'addhome/$' , views.add_home,name='addhome'),
    url(r'hoddashboard/$' , views.hod_dashboard,name='hoddashboard'),
    url(r'changepassword/$' , views.change_password,name='changepassword'),

    url(r'addworkshop/$' , views.add_workshop,name='addworkshop'),
    url(r'addbank/$' , views.add_bank,name='addbank'),
    url(r'addexperience/$' , views.add_experience,name='addexperience'),
    url(r'addpatents/$' , views.add_patents,name='addpatents'),
    url(r'addgrantsfetched/$' , views.add_grantsfetched,name='addgrantsfetched'),
    url(r'addgrantsapplied/$' , views.add_grantsapplied,name='addgrantsapplied'),
    url(r'addawards/$' , views.add_awards,name='addawards'),
    url(r'addCourses/$' , views.add_Course,name='addCourses'),
    url(r'addFaculty/$', views.add_Faculty, name='addFaculty'),

    url(r'viewhod/$', views.view_hod, name='viewhod'),




]