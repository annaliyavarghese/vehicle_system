from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Vehicle, Booking
from .serializers import VehicleSerializer, BookingSerializer

from django.http import HttpResponse

def home_view(request):
    return HttpResponse("<h1>Welcome to Vehicle System API</h1><p>Use /api/ or /admin/ to proceed.</p>")



class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {'brand':['exact','iexact'], 'fuel_type':['exact','iexact'], 'is_available':['exact']}

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
