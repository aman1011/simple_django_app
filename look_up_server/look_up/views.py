from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("Hello, World. You are at the app look_up")


def welcome(request):
    return HttpResponse("Hello..Welcome to the look up app ...")
