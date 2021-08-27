from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.get_measurements, name='measurementList'),
    path('id/<int:id>/', views.get_measurement, name='measurementId')
]