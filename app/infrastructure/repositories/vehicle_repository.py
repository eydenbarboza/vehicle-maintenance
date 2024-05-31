
from sqlalchemy.orm import Session
from app.domain.entities.vehicle import Vehicle
from app.schemas.vehicle import VehicleCreate

class VehicleRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_vehicle(self, vehicle: VehicleCreate):
        db_vehicle = Vehicle(**vehicle.dict())
        self.db.add(db_vehicle)
        self.db.commit()
        self.db.refresh(db_vehicle)
        return db_vehicle

    def get_vehicle(self, vehicle_id: int):
        return self.db.query(Vehicle).filter(Vehicle.id == vehicle_id).first()
    