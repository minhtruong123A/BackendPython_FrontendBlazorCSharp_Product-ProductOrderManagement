from datetime import datetime
from pydantic import BaseModel

class orderModel(BaseModel):
    Id : int
    OrderId : int
    ProductId : int
    CreateDate : datetime
    TotalPrice : float
    ProductQuantity : int
    ProductTotalPrice : float
    ProductName : str
    Price : float