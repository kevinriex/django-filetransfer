from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests as req
from . import forms
# Create your views here.


def home(request):
    if request.POST:
        form = forms.Form(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            print(file)
            context = {"form": forms.Form}
            req.post("http://localhost:8000/api/", files={'file': file})
            return render(request, "website/index.html", context)
        
    context = {"form": forms.Form()}
    return render(request, "website/index.html", context)
