from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

# @app.route('/market')
# def market():
#     return render_template('market.html', item_name='phone')

@app.route('/market')
def market():
    items = [
        {'id':1, 'name':'phone', 'barcode':'89321229897', 'price':500},
        {'id':2, 'name':'laptop', 'barcode':'123985473165', 'price':900},
        {'id':3, 'name':'keyboard', 'barcode':'231985128446', 'price':150},
    ]
    return render_template('market.html', items=items)