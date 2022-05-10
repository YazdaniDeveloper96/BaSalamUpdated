##################################### import requirment ##################################
import sys
sys.path.insert(0,'C:/Users/MohammadReza/Desktop/webscraping/BaSalamUpdated')
##################################### external module#####################################
from DAL.product import product
from DAL.dbmanager import Database_manager
from PL.Web_Scrap import scraping
from UI.gui import User_interface
#####################
from tkinter import *
import re
##################################### optional module ####################################
import os
os.system("cls")
####################################
db=Database_manager()
#--------------------------------get products from site (not database)-------------------------------
# products=scraping('https://basalam.com/search?sort=6&minP=10000000&maxP=105560000&ready=true&namedTags=73270&rating=1&hasDelivery=true&type=products&literal=true')
# products=products.get_data()
#--------------------------------get products from database-------------------------------------------
Product=Database_manager()
products=Product.get_all_products()
#-------------------------------show products in user interface---------------------------------------
form=User_interface(products)



   

# db.delete_1_record('price_after=285000')  # delete 1 record from table
# db.delete_all_record()           # delete all record from table
