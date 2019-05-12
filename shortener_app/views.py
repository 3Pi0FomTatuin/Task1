from django.http import HttpResponse
import short_url
from django.shortcuts import render


def index(request):
    return render(request, 'polls/index.html')


def shorten(request):
    url = short_url.encode_url(12)
    return HttpResponse(url)
