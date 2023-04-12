from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    if request.POST:
        file = request.POST.FILES
        print(file)
    return HttpResponse("Hello World;")
