from django.urls import path
from app3.views import *
app_name='anything'
urlpatterns=[
    path('Sister/',Sister,name='Sister'),
    path('akka/',akka,name='akka'),
]