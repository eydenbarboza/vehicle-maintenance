
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.infrastructure.database import get_db
from app.domain.services.vehicle_service import VehicleService
from app.schemas.vehicle import VehicleCreate, Vehicle

router = APIRouter()

@router.post("/", response_model=Vehicle)
def create_vehicle(vehicle: VehicleCreate, db: Session = Depends(get_db)):
    service = VehicleService(db)
    return service.create_vehicle(vehicle)

@router.get("/{vehicle_id}", response_model=Vehicle)
def read_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    service = VehicleService(db)
    db_vehicle = service.get_vehicle(vehicle_id)
    if db_vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return db_vehicle
    