from typing import List
from src.database.get_db_instance import cursor as db
from src.models.product import ProductModel
from src.models.order import orderModel
import pyodbc


def get_all_product():

    result : List[ProductModel] = []
    db.execute('SELECT * FROM dbo.Product')

    alist = db.fetchall()

    for product in alist:
        product_obj = ProductModel(Id=int(product.Id), ProductName=product.ProductName, 
                                   Price=float(product.Price), BrandCategoryId=0)
        # print(f"{product.Id}\t{product.ProductName}\t{product.Price}")
        result.append(product_obj)

    return result


def update_product_price(id, new_price):
    db.execute('SELECT * FROM dbo.Product WHERE Id = ?', [id])
    obj = db.fetchall()
    print(len(obj))
    if len(obj) == 0:
        print("co in loi khong ?")
        raise ValueError("id not found !")

    db.execute('UPDATE product SET Price = ? WHERE Id = ?', [new_price, id])
    db.commit()








