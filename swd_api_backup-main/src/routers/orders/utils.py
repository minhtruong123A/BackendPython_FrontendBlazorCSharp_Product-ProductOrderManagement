from typing import List
from src.database.get_db_instance import cursor as db
from src.models.product import ProductModel
from src.models.order import orderModel
import pyodbc

def get_all_order():

    result : List[orderModel] = []


    query_string = ("SELECT a.Id, a.OrderId, a.ProductId, b.CreateDate, b.TotalPrice, "+
                    " a.ProductQuantity, a.ProductTotalPrice, c.ProductName, c.Price "+
                    " FROM ProductOrder a "+
                    " JOIN [Order] b ON a.OrderId = b.Id "+
                    " JOIN Product c ON a.ProductId = c.Id "+
                    " ORDER BY b.CreateDate DESC; ")
    
    
    
    db.execute(query_string)

    alist = db.fetchall()

    for order in alist:
        current_order = orderModel(Id=order.Id, 
                                   OrderId=order.OrderId,
                                   ProductId=order.ProductId,
                                   CreateDate=order.CreateDate,
                                   TotalPrice=order.TotalPrice,
                                   ProductQuantity=order.ProductQuantity,
                                   ProductName=order.ProductName,
                                   Price=order.Price,
                                   ProductTotalPrice=order.ProductTotalPrice)
        
        result.append(current_order)

    return result