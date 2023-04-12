from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests as req
from . import forms
# Create your views here.


def home(request):
    if request.POST:
        form = forms.Form(request.POST, request.FILES)
        if form.is_valid():
            print(request.FILES['file'])
            context = {"form": forms.Form}
            return render(request, "website/index.html", context)

        return redirect("https://kevinriexinger.de")
    context = {"form": forms.Form()}
    return render(request, "website/index.html", context)
