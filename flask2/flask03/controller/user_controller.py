from app import app

from model.user_model import user_model
# this first user_model represent the file name the second represent the classname
obj = user_model()

@app.route("/getall")
# @app.route("/user/getall")
def user_getall_controller():
    return obj.user_getall_model()