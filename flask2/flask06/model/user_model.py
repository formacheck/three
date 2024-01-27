#pip3 install mysql-connector-python
import mysql.connector
import json
from flask import make_response

class user_model():
    def __init__(self):
        try:
            self.con=mysql.connector.connect(host="localhost", user="unknown",password="unknowndb",database="flask_tutorial")
            self.con.autocommit=True
            self.cur=self.con.cursor(dictionary=True)
            print("connected")
        except:
            print("some error")


    def user_getall_model(self):
        self.cur.execute("SELECT * FROM users")
        result = self.cur.fetchall()
        if len(result)>0:
            return make_response({"payload":result}, 200)
        else:
            return make_response({"message":"no data found"}, 204)
        
        
    def user_adduser_model(self, data):
        self.cur.execute(f"INSERT INTO users(name,email,role,password) VALUES('{data['name']}', '{data['email']}', '{data['role']}', '{data['password']}')")
        return make_response({"message":"user created succesful"}, 201)
    
    def user_updateuser_model(self, data):
        self.cur.execute(f"UPDATE users SET name='{data['name']}',email='{data['email']}',role='{data['role']}',password='{data['password']}'  WHERE id={data['id']}")
        if self.cur.rowcount>0:
            return make_response({"message":"user updated successful"},201)
        else:
            return make_response({"message":"nothing to update"},204)
        
    def user_deleteuser_model(self, id):
        self.cur.execute(f"DELETE FROM users WHERE id={id}")
        if self.cur.rowcount>0:
            return make_response({"message":"user deleted"},200)
        else:
            return make_response({"message":"nothing to delete"},202)