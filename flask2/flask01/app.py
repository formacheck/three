from flask import Flask
app = Flask(__name__)

@app.route("/")
def welcome():
    return "hello world"

@app.route("/home")
def home():
    return "welcome to home page"

# import controller.user_controller as user_controller
# import controller.product_controller as product_controller
  # oR
# from controller import product_controller, user_controller
  # oR
 # you will add __init__.py file in the controller folder or any other folder you have 
 # code inside that you want to import and use this command to import everything on that folder
from controller import *

