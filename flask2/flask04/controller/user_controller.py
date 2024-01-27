from app import app
from model.user_model import user_model
# this first user_model represent the file name the second represent the classname
from flask import request

obj = user_model()

@app.route("/getall")
# @app.route("/user/getall")
def user_getall_controller():
    return obj.user_getall_model()


@app.route("/adduser", methods=["POST"])
def user_adduser_controller():
    # print(request.form)
    return obj.user_adduser_model(request.form)

@app.route("/updateuser", methods=["PUT"])
def user_updateuser_controller():
    # print(request.form)
    return obj.user_updateuser_model(request.form)

@app.route("/deleteuser/<id>", methods=["DELETE"])
def user_deleteuser_controller(id):
    # print(request.form)
    return obj.user_deleteuser_model(id)