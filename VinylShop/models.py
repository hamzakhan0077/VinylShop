# database stuff goes in here

import os, sys
sys.path.insert(0, os.path.abspath(".."))
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from datetime import datetime
from VinylShop  import db,app,login_manager
from flask_login import UserMixin





@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User (db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key =True)
    username = db.Column(db.String(17), unique = True, nullable = False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120),nullable=False)
    playlist = db.relationship('VinylPlaylist', backref= 'author', lazy = True)






    def __repr__(self): # how our object is printed when we print it out
        return f"User('{self.username}',{self.email})"


class VinylPlaylist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    playlist_name = db.Column(db.String(120),nullable=False)
    date_created= db.Column(db.DateTime,nullable=False,default = datetime.utcnow)
    content = db.Column(db.Text ,nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable = False)

    def __repr__(self):  # how our object is printed when we print it out
        return f"Playlist ('{self.playlist_name}',{self.date_created})"























if __name__ == '__main__':
    pass