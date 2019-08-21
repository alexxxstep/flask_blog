from app import db

class Post(db.Model):


class Data(db.Model):
    #create a table
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key = True)
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    shoesize = db.Column(db.Integer)
    sex = db.Column(db.String)

    def __init__(self, height, weight, shoesize, sex):
        self.height = height
        self.weight = weight
        self.shoesize = shoesize
        self.sex = sex
