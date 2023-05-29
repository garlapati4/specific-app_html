from django.urls import path
from app2.views import *
app_name='something'
urlpatterns=[
    path('Mother/',Mother,name='Mother'),
    path('amma/', amma,name='amma'),
]