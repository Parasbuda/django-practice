from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello")

def paras(request):
    return HttpResponse("Hello, Paras")

def yuvi(request):
    return HttpResponse("Hello Yuviii")

def greet(request,name):
    return HttpResponse(f"Hello {name.capitalize()}")