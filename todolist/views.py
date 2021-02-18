from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

todos=[]

class TodoForm(forms.Form):
    todo=forms.CharField(label="New Todo")
# Create your views here.

def index(request):
    if "todos"not in request.session:
        request.session["todos"]=[]
    return render(request,"todo/index.html",{
        "todos":request.session["todos"]
    })

def add(request):
    if request.method=="POST":
        form=TodoForm(request.POST)
        if form.is_valid():
            todo=form.cleaned_data["todo"]
            request.session["todos"]+=[todo]
            return HttpResponseRedirect(reverse("todos:index"))
        else:
            return render(request,"todo/add.html",{
                "form":form
            })

    return render(request,"todo/add.html",{
        "form":TodoForm()
    })