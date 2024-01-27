from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'

# so now you have to enter into the python shell on other to create the the database file with is the market.db file
# python3 hit enter
# from market import db hit enter
# db.create_all()

db = SQLAlchemy(app)


# models
class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(1024), nullable=False)





# routes
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')



@app.route('/market')
def market_page():
    items = [
        {'id':1, 'name':'phone', 'barcode':'89321229897', 'price':500},
        {'id':2, 'name':'laptop', 'barcode':'123985473165', 'price':900},
        {'id':3, 'name':'keyboard', 'barcode':'231985128446', 'price':150},
    ]
    return render_template('market.html', items=items)








# This block ensures an application context is created before running the script
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)