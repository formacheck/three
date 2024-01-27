#pip3 install mysql-connector-python
import mysql.connector
import json

class user_model():
    def __init__(self): #this is a contructor
       # connnection establishment
        try:
            self.con=mysql.connector.connect(host="localhost", user="unknown",password="unknowndb",database="flask_tutorial")
            self.con.autocommit=True
            self.cur=self.con.cursor(dictionary=True)
            print("connected")
        except:
            print("some error")


    def user_getall_model(self):
        # query execution
        self.cur.execute("SELECT * FROM users")
        result = self.cur.fetchall()
        # print(result)
        if len(result)>0:
            return json.dumps(result)
        else:
            return "no data found"
        
        
    def user_adduser_model(self, data):
         # print(data)
        # print(data['email'])
        self.cur.execute(f"INSERT INTO users(name,email,role,password) VALUES('{data['name']}', '{data['email']}', '{data['role']}', '{data['password']}')")
        return "user created successfull"
    
    def user_updateuser_model(self, data):
        self.cur.execute(f"UPDATE users SET name='{data['name']}',email='{data['email']}',role='{data['role']}',password='{data['password']}'  WHERE id={data['id']}")
        if self.cur.rowcount>0:
            return "user updated successfully"
        else:
            return "nothing to update"
        
    def user_deleteuser_model(self, id):
        self.cur.execute(f"DELETE FROM users WHERE id={id}")
        if self.cur.rowcount>0:
            return "user deleted successfully"
        else:
            return "nothing to delete"