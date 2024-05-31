from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.infrastructure.database import Base
import enum
from transitions import Machine
from pydantic import BaseModel

class ServiceState(enum.Enum):
    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"

class ServiceOrder(Base):
    __tablename__ = "service_orders"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    description = Column(String, index=True)
    state = Column(Enum(ServiceState), default=ServiceState.PENDING)

    vehicle = relationship("Vehicle")

class ServiceOrderStateMachine:
    states = [ServiceState.PENDING, ServiceState.IN_PROGRESS, ServiceState.COMPLETED]

    def __init__(self):
        self.machine = Machine(model=self, states=ServiceOrderStateMachine.states, initial=ServiceState.PENDING)
        self.machine.add_transition(trigger='start_service', source=ServiceState.PENDING, dest=ServiceState.IN_PROGRESS)
        self.machine.add_transition(trigger='complete_service', source=ServiceState.IN_PROGRESS, dest=ServiceState.COMPLETED)

class ServiceOrderCreate(BaseModel):
    description: str
    vehicle_id: int

