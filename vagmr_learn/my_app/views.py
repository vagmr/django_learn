from urllib.parse import unquote
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

pages = {
    "index": "index",
    "about": "about",
    "contact": "contact"
}


def index(req):
    return HttpResponse("Hello, world. You're at the polls index.")


def mulpattern(req, path_p):
    try:
        return HttpResponse(pages[path_p])
    except:
        return HttpResponseNotFound("404")

# Create your views here.
