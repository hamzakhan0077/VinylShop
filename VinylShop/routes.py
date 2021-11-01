from flask import render_template
from VinylShop import app

# ALL Pages configuration goes in here

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')