from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# Simple http response
def index(request):
    return HttpResponse("This is a simple response at simple_poll index")
    