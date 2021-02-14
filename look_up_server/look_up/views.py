from django.shortcuts import render
from django.http import HttpResponse
import csv
# Create your views here.


def index(request):
    return HttpResponse("Hello, World. You are at the app look_up")


def welcome(request):
    return HttpResponse("Hello..Welcome to the look up app ...")


def server(request, server_id):
    # read the CSV.
    #with ('../newservers.csv') as phile:
    #    f = phile.read()
    #    data = csv.DictReader(f)

    #    print(data)

        return HttpResponse(f"Processing server id {server_id}....")

