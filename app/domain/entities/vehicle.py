
from sqlalchemy import Column, Integer, String
from app.infrastructure.database import Base

class Vehicle(Base):
    __tablename__ = "vehicles"
    
    id = Column(Integer, primary_key=True, index=True)
    license_plate = Column(String, index=True)
    make = Column(String, index=True)
    model = Column(String, index=True)
    year = Column(Integer)
    