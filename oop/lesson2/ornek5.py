import socket
from datetime import datetime

class CoreEntity():
    
    def __init__(self):
        self.CreatedDate = datetime.now()
        self.CreatedComputerName = socket.gethostname()
        self.CreatedIP =socket.gethostbyname("")


class Category(CoreEntity):
    CategoryName = ""
    Description = ""

class Product(CoreEntity):
    ProductName = ""
    UnitPrice = 0
    UnitInStock = 0

product = Product()
print(product.CreatedDate)