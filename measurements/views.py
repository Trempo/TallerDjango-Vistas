import json

from django.shortcuts import render
from .logic.logic_measurements import *
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import QueryDict



def get_measurements(request):
    measurements = get_all_measurements()
    measurements_list = serializers.serialize('json', measurements)
    return HttpResponse(measurements_list, content_type='application/json')


def get_measurement(request, id):
    measurement = get_measurement_id(id)
    measurement_json = serializers.serialize('json', [measurement])
    return HttpResponse(measurement_json, content_type='application/json')


def delete_measurement(request, id):
    delete_measurement_id(id)

@csrf_exempt
def update_measurement(request, id):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    value = body['value']
    measurement = update_measurement_value(id, value)
    measurement_json = serializers.serialize('json', [measurement])
    return HttpResponse(measurement_json, content_type='application/json')





