from pydantic import BaseModel

class ProductModel(BaseModel):
    Id : int
    ProductName : str
    BrandCategoryId : int
    Price : float