
from fastapi import FastAPI
from sqlalchemy import create_engine
from app.infrastructure.database import engine, Base
from app.api.endpoints import vehicles, service_orders

import os

if os.getenv('TESTING') == 'True':
    DATABASE_URL = "sqlite:///./test.db"
    engine = create_engine(DATABASE_URL)
else:
    DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://user:password@localhost/transport_db')
    engine = create_engine(DATABASE_URL)

app = FastAPI()



Base.metadata.create_all(bind=engine)

app.include_router(vehicles.router, prefix="/vehicles", tags=["vehicles"])
app.include_router(service_orders.router, prefix="/service_orders", tags=["service_orders"])
    






