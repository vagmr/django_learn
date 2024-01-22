from urllib.parse import unquote
from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


from util.url_pcs import reverse_url

pages = {
    "index": "index",
    "about": "about",
    "contact": "contact"
}


def index(req):
    return render(req, 'my_app/index.html',
                  {'now': datetime.now(), "list": [1, 4, 5, 6]})

# Create your views here.
