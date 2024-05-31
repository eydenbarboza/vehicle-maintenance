
from pydantic import BaseModel
from app.domain.entities.service_order import ServiceState

class ServiceOrderBase(BaseModel):
    vehicle_id: int
    description: str

class ServiceOrderCreate(ServiceOrderBase):
    pass

class ServiceOrder(ServiceOrderBase):
    id: int
    state: ServiceState

    class Config:
        orm_mode = True

class ServiceOrderUpdate(BaseModel):
    transition: str
    