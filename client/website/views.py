from django.shortcuts import render
from django.http import HttpResponse
import requests as req
from . import forms
# Create your views here.


def home(request):
    context = {"form": forms.Form}
    return render(request, "website/index.html", context)
