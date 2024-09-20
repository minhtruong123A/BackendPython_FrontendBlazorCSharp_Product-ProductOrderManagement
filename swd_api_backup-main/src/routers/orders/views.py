from fastapi import APIRouter
from src.routers.orders.utils import get_all_order
from src.schemas.response_body_schemas import ResponseBodySchemas

order_router = APIRouter(prefix="/api/orders", tags=["Order"])

@order_router.get("", response_model=ResponseBodySchemas)
async def do_get_all_order():
    return {"data" : get_all_order()}
