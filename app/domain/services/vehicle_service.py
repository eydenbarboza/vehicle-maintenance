
from sqlalchemy.orm import Session
from app.infrastructure.repositories.vehicle_repository import VehicleRepository
from app.schemas.vehicle import VehicleCreate

class VehicleService:
    def __init__(self, db: Session):
        self.repo = VehicleRepository(db)

    def create_vehicle(self, vehicle: VehicleCreate):
        return self.repo.create_vehicle(vehicle)

    def get_vehicle(self, vehicle_id: int):
        return self.repo.get_vehicle(vehicle_id)
    