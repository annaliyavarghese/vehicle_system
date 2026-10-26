
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VehicleViewSet, BookingViewSet, home_view
from django.http import HttpResponse 
def home_placeholder(request):
    return HttpResponse("Vehicle System API is running.")

router = DefaultRouter()

router.register(r'vehicles', VehicleViewSet, basename='vehicle')
router.register(r'bookings', BookingViewSet, basename='booking')

urlpatterns = [
    path('user/', home_view, name='user'),
    path('', include(router.urls)),
    path('', home_placeholder, name='home'),

]
