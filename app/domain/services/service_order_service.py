
from sqlalchemy.orm import Session
from app.infrastructure.repositories.service_order_repository import ServiceOrderRepository
from app.schemas.service_order import ServiceOrderCreate
from app.domain.entities.service_order import ServiceOrderStateMachine

class ServiceOrderService:
    def __init__(self, db: Session):
        self.repo = ServiceOrderRepository(db)

    def create_service_order(self, service_order: ServiceOrderCreate):
        return self.repo.create_service_order(service_order)

    def update_service_order_state(self, order_id: int, state_transition: str):
        order = self.repo.get_service_order(order_id)
        state_machine = ServiceOrderStateMachine()
        state_machine.__dict__.update(order.__dict__)
        if state_transition == 'start_service':
            state_machine.start_service()
        elif state_transition == 'complete_service':
            state_machine.complete_service()
        order.state = state_machine.state
        self.repo.update_service_order(order)
        return order
    
    def get_service_order(self, order_id: int):
        return self.repo.get_service_order(order_id)

    