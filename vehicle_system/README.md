## Vehicle Rental API

## Project Description
A Django REST Framework API for managing vehicles and bookings.

## Requirements
- Python
- Django
- Django REST Framework
- django-filter

## Installation

pip install -r requirements.txt


## Database Migration


python manage.py makemigrations
python manage.py migrate


## Run the Project


python manage.py runserver


## API Endpoints

### Vehicles
- GET /api/vehicles/
- POST /api/vehicles/
- GET /api/vehicles/{id}/
- PUT /api/vehicles/{id}/
- DELETE /api/vehicles/{id}/

### Bookings
- GET /api/bookings/
- POST /api/bookings/
- GET /api/bookings/{id}/

## Vehicle Filtering

-/api/vehicles/?brand=Toyota
- /api/vehicles/?fuel_type=Electric
- /api/vehicles/?is_available=true

## Sample Booking JSON

json
{
  "vehicle": 1
}

