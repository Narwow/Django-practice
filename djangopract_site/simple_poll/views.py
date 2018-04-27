from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# Simple http response
def index(request):
    return HttpResponse("This is a simple response at simple_poll index")

def detail(request, question_id):
    return HttpResponse("You are looking at question %s." %question_id)

def results(request, question_id):
    response = "You are looking at the results of questions %s."
    return HttpResponse(response %question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s." %question_id)    