from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Vehicle, Booking
from .serializers import VehicleSerializer, BookingSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {'brand':['exact','iexact'], 'fuel_type':['exact','iexact'], 'is_available':['exact']}

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
