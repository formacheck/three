#pip3 install mysql-connector-python
import mysql.connector
class user_model():
    def __init__(self): #this is a contructor
       # connnection establishment
        try:
            mysql.connector.connect(host="localhost", user="unknown",password="unknowndb",database="flask_tutorial")
            print("connected")
        except:
            print("some error")
    def user_getall_model(self):
        # query execution
        return "this is user signup model"