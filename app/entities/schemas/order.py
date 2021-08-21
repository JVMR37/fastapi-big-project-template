import datetime
from typing import List, Optional

from pydantic import BaseModel, Field

from app.entities.schemas.order_item import OrderItem


class OrderBase(BaseModel):
    customer: str
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
    done: bool = False


class OrderCreate(OrderBase):
    pass


class Order(OrderBase):
    id: int
    done_at: Optional[datetime.datetime] = None
    items: List[OrderItem] = []

    class Config:
        orm_mode = True
