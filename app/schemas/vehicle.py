
from pydantic import BaseModel

class VehicleBase(BaseModel):
    license_plate: str
    make: str
    model: str
    year: int

class VehicleCreate(VehicleBase):
    pass

class Vehicle(VehicleBase):
    id: int

    class Config:
        orm_mode = True
    