from django.urls import path
from app1.views import *
app_name='nothing'
urlpatterns=[
    path('Father/',Father,name='Father'),
    path('nanna/',nanna,name='nanna'),
]