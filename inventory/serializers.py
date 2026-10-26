from rest_framework import serializers
from .models import Vehicle, Booking
from datetime import date

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    total_amount = serializers.ReadOnlyField()

    class Meta:
        model = Booking
        fields = '__all__'

    def validate(self, data):
        if len(data['customer_phone']) != 10:
            raise serializers.ValidationError("Phone number must be 10 digits.")

        if data['start_date'] < date.today() or data['end_date'] <= data['start_date']:
            raise serializers.ValidationError("Check your dates.")

        if not data['vehicle'].is_available:
            raise serializers.ValidationError("Vehicle is not available.")

        return data

    def create(self, validated_data):
        booking = super().create(validated_data)
        booking.vehicle.is_available = False
        booking.vehicle.save()
        return booking
