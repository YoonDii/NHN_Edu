import json
import requests

from django.shortcuts import render
from .models import Searchlist
from django.http import HttpRequest , JsonResponse
from bs4 import BeautifulSoup

# Create your views here.

def index(request):

    return render (request,"blog/index.html")