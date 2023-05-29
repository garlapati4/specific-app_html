from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Sister(request):
    return HttpResponse('<center><h1>"Sisters are connected throughout their lives by a Special Bond"</h1></center>')

def akka(request):
    return render(request,'akka.html')