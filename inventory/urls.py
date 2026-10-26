from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VehicleViewSet, BookingViewSet
from .views import home_view  


router = DefaultRouter()
router.register(r'vehicles', VehicleViewSet, basename='vehicle')
router.register(r'bookings', BookingViewSet, basename='booking')

urlpatterns = [
    path('user/', home_view, name='user'), 

    path('', include(router.urls)),

]
