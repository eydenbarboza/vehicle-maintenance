import pytest
from app.infrastructure.repositories.vehicle_repository import VehicleRepository
from app.schemas.vehicle import VehicleCreate

def test_create_vehicle(test_db):
    repo = VehicleRepository(test_db)
    
    new_vehicle = VehicleCreate(license_plate="ABC123", make="Toyota", model="Corolla", year=2021)
    created_vehicle = repo.create_vehicle(new_vehicle)
    
    assert created_vehicle.license_plate == "ABC123"
    assert created_vehicle.make == "Toyota"
    assert created_vehicle.model == "Corolla"
    assert created_vehicle.year == 2021

def test_get_vehicle(test_db):
    repo = VehicleRepository(test_db)
    
    new_vehicle = VehicleCreate(license_plate="ABC123", make="Toyota", model="Corolla", year=2021)
    created_vehicle = repo.create_vehicle(new_vehicle)
    
    fetched_vehicle = repo.get_vehicle(created_vehicle.id)
    
    assert fetched_vehicle.license_plate == "ABC123"
    assert fetched_vehicle.make == "Toyota"
    assert fetched_vehicle.model == "Corolla"
    assert fetched_vehicle.year == 2021
