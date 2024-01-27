from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>flask</h1>"

@app.route("/about")
def about():
    return "<h1>about page</h1>"

@app.route("/profile/<username>")
def profile(username):
    return f"<h1>this is the profile page of {username}</h1>"