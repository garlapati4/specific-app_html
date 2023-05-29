from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Father(request):
    return HttpResponse('<center><h1>Behind Every Great Daughter is a Truly Amazing DAD</h1></center>')

def nanna(request):
    return render(request,'nanna.html')