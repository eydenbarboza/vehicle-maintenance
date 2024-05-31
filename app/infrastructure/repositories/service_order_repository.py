
from sqlalchemy.orm import Session
from app.domain.entities.service_order import ServiceOrder
from app.schemas.service_order import ServiceOrderCreate

class ServiceOrderRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_service_order(self, service_order: ServiceOrderCreate):
        db_order = ServiceOrder(**service_order.dict())
        self.db.add(db_order)
        self.db.commit()
        self.db.refresh(db_order)
        return db_order

    def get_service_order(self, order_id: int):
        return self.db.query(ServiceOrder).filter(ServiceOrder.id == order_id).first()

    def update_service_order(self, service_order: ServiceOrder):
        self.db.commit()
        self.db.refresh(service_order)
        return service_order
    