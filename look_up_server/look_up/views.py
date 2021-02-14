from django.shortcuts import render
from django.http import JsonResponse
import csv
import os
import json

# Create your views here.


def index(request):
    return HttpResponse("Hello, World. You are at the app look_up")


def welcome(request):
    return HttpResponse("Hello..Welcome to the look up app ...")



def read_csv_file():
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'newservers.csv')
    list_of_dicts = []
    try:
        with open(file_path) as phile:
            data = csv.DictReader(phile, delimiter=',')
            for row in data:
                list_of_dicts.append(row)

            return list_of_dicts
    except (FileNotFoundError, Exception) as error:
        print(error)


def server(request, server_id):
    # read the CSV.
    data = read_csv_file()
    for row in data:
        if row['serial'] == server_id:
            return JsonResponse(row)

    return JsonResponse({"response": "No records found"})


