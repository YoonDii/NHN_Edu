import json
import requests

from django.shortcuts import render
from .models import Searchlist
from django.http import HttpResponse , JsonResponse
from bs4 import BeautifulSoup

# Create your views here.

def index(request):
    data = Searchlist.objects.order_by("-pk")
    context = {
        "data" : data,
    }
    return render (request,"blog/index.html",context)

