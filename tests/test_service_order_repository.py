import pytest
from app.infrastructure.repositories.service_order_repository import ServiceOrderRepository
from app.schemas.service_order import ServiceOrderCreate

def test_create_service_order(test_db):
    repo = ServiceOrderRepository(test_db)
    
    new_order = ServiceOrderCreate(description="Cambio de aceite", vehicle_id=1)
    created_order = repo.create_service_order(new_order)
    
    assert created_order.description == "Cambio de aceite"
    assert created_order.vehicle_id == 1

def test_get_service_order(test_db):
    repo = ServiceOrderRepository(test_db)
    
    new_order = ServiceOrderCreate(description="Cambio de aceite", vehicle_id=1)
    created_order = repo.create_service_order(new_order)
    
    fetched_order = repo.get_service_order(created_order.id)
    
    assert fetched_order.description == "Cambio de aceite"
    assert fetched_order.vehicle_id == 1
