from app import app

@app.route("/signup")
# @app.route("/user/signup")
def signup():
    return "this is signup page"