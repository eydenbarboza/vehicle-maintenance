import pytest
from app.domain.entities.service_order import ServiceOrderCreate, ServiceState
from app.domain.services.service_order_service import ServiceOrderService

def test_create_service_order(test_db):
    service = ServiceOrderService(test_db)
    
    new_order = ServiceOrderCreate(description="Cambio de aceite", vehicle_id=1)
    created_order = service.create_service_order(new_order)
    
    assert created_order.description == "Cambio de aceite"
    assert created_order.vehicle_id == 1

def test_update_service_order_state(test_db):
    service = ServiceOrderService(test_db)

    new_order = ServiceOrderCreate(description="Cambio de aceite", vehicle_id=1)
    created_order = service.create_service_order(new_order)

    updated_order = service.update_service_order_state(created_order.id, "start_service")

    assert updated_order.state == ServiceState.IN_PROGRESS
