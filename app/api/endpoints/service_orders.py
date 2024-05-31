
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.infrastructure.database import get_db
from app.domain.services.service_order_service import ServiceOrderService
from app.schemas.service_order import ServiceOrderCreate, ServiceOrder, ServiceOrderUpdate

router = APIRouter()

@router.post("/", response_model=ServiceOrder)
def create_service_order(service_order: ServiceOrderCreate, db: Session = Depends(get_db)):
    service = ServiceOrderService(db)
    return service.create_service_order(service_order)

@router.patch("/{order_id}", response_model=ServiceOrder)
def update_service_order(order_id: int, update: ServiceOrderUpdate, db: Session = Depends(get_db)):
    service = ServiceOrderService(db)
    return service.update_service_order_state(order_id, update.transition)

@router.get("/{order_id}", response_model=ServiceOrder)
def get_service_order(order_id: int, db: Session = Depends(get_db)):
    service = ServiceOrderService(db)
    order = service.get_service_order(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Service order not found")
    return order