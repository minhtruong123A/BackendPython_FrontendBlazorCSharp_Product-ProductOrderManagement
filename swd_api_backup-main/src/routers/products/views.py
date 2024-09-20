from fastapi import APIRouter
from src.routers.products.utils import get_all_product, update_product_price
from src.schemas.response_body_schemas import ResponseBodySchemas

product_router = APIRouter(prefix="/api/products", tags=["Product"])

@product_router.get("", response_model=ResponseBodySchemas)
async def do_get_all_product():
    return {"data" : get_all_product()}

@product_router.post("/{id}/price={new_price}", response_model=ResponseBodySchemas)
async def do_update_product_price(id : int, new_price : float):
    try:
        update_product_price(id=id, new_price=new_price)
        return {"data" : []}
    except Exception as e:
        print(str(e))
        return {"success" : False, 
                "error" : str(e)}
    


