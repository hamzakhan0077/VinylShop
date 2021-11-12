import os, sys
sys.path.insert(0, os.path.abspath(".."))

# from VinylShop import app
from flask import  Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
# run encoder.py and enter the CODE to get the secret key
app.config['SECRET_KEY'] = 'dc694b687086ff4c7275710108efdfeeae2a2e7debb2205421871ce8f588e8a2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

login_manager = LoginManager(app)
login_manager.login_view = 'login'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
from VinylShop import routes
# configure DB here
# create DB APP

