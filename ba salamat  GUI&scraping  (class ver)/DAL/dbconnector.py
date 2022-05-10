###########################################requirments
from mysql.connector import connect,Error
############################################# main code
def dbconnect():
    try:
        return connect(host="localhost",user="root",password="rezA13751996",database="Ba_salam") # first step
    except Exception as error:
        return False