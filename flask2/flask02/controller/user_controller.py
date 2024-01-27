from app import app

from model.user_model import user_model
# this first user_model represent the file name the second represent the classname
obj = user_model()

@app.route("/signup")
# @app.route("/user/signup")
def user_signup_controller():
    return obj.user_signup_model()