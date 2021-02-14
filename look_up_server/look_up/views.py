from django.shortcuts import render
from django.http import JsonResponse
import csv
import os
import json
import ipaddress

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


def validate_the_response(json_object):

    # check validity for the IP address.
    try:
        ip = ipaddress.ip_address(json_object["ip"])
    except ValueError as error:
        return {
            "is_valid": False,
            "error_message": "Issue in IP address" + str(error)
        }

    # check if the ip and netmask is valid.
    try:
        ip_network = ipaddress.IPv4Network(json_object["ip"] + "/" + json_object["netmask"], strict=False)
    except ValueError as  value_error:
        return {
            "is_valid": False,
            "error_message": "Issue in IP addr and Netmask network config:- " + str(value_error),
        }
    except Exception as error:
        return {
            "is_valid": False,
            "error_message": "Issue in IP/Netmask combination:- " + str(error),
        }

    # check if the gateway is proper.
    try:
        ip_address = ipaddress.ip_address(json_object["gateway"])
    except ValueError as error:
        return {
            "is_valid": False,
            "error_message": "Issue in Gateway Address:- " + str(error)
        }

    # check if the gateway would be included in the
    # list of valid IP address.
    available_host = list(ip_network.hosts())
    if ipaddress.ip_address(json_object["gateway"]) not in list(ip_network.hosts()):
        return {
            "is_valid": False,
            "error_message": "Gateway not present in the list of valid hosts "
        }

    # After all the validations, lets format the output.
    json_object['hostname'] = json_object['hostname'].strip()
    return {
        "response": json_object,
        "is_valid": True,
    }


def server(request, server_id):
    # read the CSV.
    data = read_csv_file()
    for row in data:
        if row['serial'] == server_id:

            # make validations here for the row
            # and return the json response.
            validated_data = validate_the_response(row)
            if not validated_data["is_valid"]:
                return JsonResponse({"error": validated_data["error_message"]})
            else:

                return JsonResponse(validated_data["response"])

    return JsonResponse({"response": "No records found"})


