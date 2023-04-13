from django.shortcuts import render
from django.http import HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from os.path import join
import os
from datetime import datetime
# Create your views here.

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


@csrf_exempt
def home(request):
    if not request.method == "POST":
        return HttpResponseNotAllowed("POST")
    if request.FILES:
        file = request.FILES["file"]
        timestamp = datetime.fromtimestamp(
            datetime.timestamp(datetime.now())).strftime("%d-%m-%Y_%H-%M-%S")
        with open(f"{join(BASE_DIR, f'uploads/')}{timestamp}_{file.name}", "wb+") as f:
            for chunk in file.chunks():
                f.write(chunk)

    return JsonResponse({})
