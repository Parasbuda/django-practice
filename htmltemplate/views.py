from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"html/index.html")

def greet(request,name):
    return render(request,"html/greet.html",{"name":name})