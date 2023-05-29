from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Mother(request):
    return HttpResponse('<center><h1>"A Mother is the truest friend we have"</h1></center>')

def amma(request):
    return render(request,'amma.html')