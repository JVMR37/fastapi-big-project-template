from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import items, orders, order_items
from app.entities.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(orders.router)
app.include_router(items.router)
app.include_router(order_items.router)
