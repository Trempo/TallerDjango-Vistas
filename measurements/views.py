from django.shortcuts import render
from .logic.logic_measurements import get_all_measurements, get_measurement_id
from django.http import HttpResponse
from django.core import serializers


def get_measurements(request):
    measurements = get_all_measurements()
    measurements_list = serializers.serialize('json', measurements)
    return HttpResponse(measurements_list, content_type='application/json')


def get_measurement(request, id):
    measurement = get_measurement_id(id)
    measurement_json = serializers.serialize('json', [measurement])
    return HttpResponse(measurement_json, content_type='application/json')


def delete_measurement(request, id):
    measurement = delete_measurement(id)
