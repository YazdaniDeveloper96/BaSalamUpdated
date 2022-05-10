import sys
sys.path.insert(0,'C:/Users/MohammadReza/Desktop/webscraping/BaSalamUpdated')
#---------------------------------------------------------------------
from DAL.dbconnector import dbconnect
#---------------------------------------------------------------------
class Database_manager:
    def __init__(self) -> None:
        self.db=dbconnect()
        self.myCursor=self.db.cursor()
        #----insert product
    def insert_into_type1(self,product):
        self.myCursor.execute(f"Insert INTO product(image,title,score,city,price_before,discount_percent,price_after) Values('{product.img}','{product.title}','{product.score}','{product.city}','{product.pricebefor}','{product.discount}','{product.priceafter}')")
        self.db.commit()
        #----delete 1 product
    def delete_1_record(self,value=str):
        self.myCursor.execute(f"delete From product where {value}")
        self.db.commit()
        #----delete all product
    def delete_all_record(self):
        self.myCursor.execute(f"delete From product ")
        self.db.commit()
        #----update product
    def update_type1(self):
        pass
        #----get 1 product
    def get_product(self):
        pass
        #----get all product
    def get_all_products(self):
        self.myCursor.execute("Select * From product ")
        product=self.myCursor.fetchall() 
        return product
