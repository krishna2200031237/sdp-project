from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('hello/', hello, name='hello'),
    path('', newhomepage, name='newhomepage1'),
    path('travel/', travelpackage, name='travelpackage1'),
    path('print_to_console/', print_to_console, name='print_to_console'),
    path('p/',print1 , name = 'print1'),

    path('randomcall/',randomcall,name = 'randomcall'),
    path('randomlogic/', randomlogic, name='randomotpgenerator'),
    path('get_date/', get_date, name='getdate1'),
    path('getmain/',get_date,name = 'getmain'),
    path('register/',registercall,name = 'register'),
    path('pie_chart/',pie_chart,name = 'pie_chart'),
    path('weather/',pie_chart,name = 'weather'),
    path('login/',login,name='login'),
    path('signup/',signup,name='signup'),
    path('login1/',login1,name='login1'),
    path('signup1/',signup1,name='signup1'),
    path('logout/',logout,name='logout'),
    ]