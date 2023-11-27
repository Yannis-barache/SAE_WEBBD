import yaml, os.path
from .app import db, login_manager
from flask_login import UserMixin


Festivals = yaml.safe_load(
    open(
        os.path.join(
            os.path.dirname(__file__),
            "data.yml"
        )
    )
)

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(64))
    __mapper_args__ = {
        'polymorphic_identity':'user',
        'polymorphic_on':username
    }
    def get_id(self):
        return self.username

    def __repr__(self):
        return "<User (%d) %s>" % (self.id, self.username)

class Client(User,db.Model):
    idClient = db.Column(db.Integer, primary_key=True)
    nomClient = db.Column(db.String(50), nullable=False)
    prenomClient = db.Column(db.String(50), nullable=False)
    emailClient = db.Column(db.String(50), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity':'user',
    }
    def __repr__(self):
        return "<Client (%d) %s>" % (self.id, self.username)

class Groupe(User,db.Model):
    idGroupe = db.Column(db.Integer, primary_key=True)
    nomGroupe = db.Column(db.String(50), nullable=False)
    emailGroupe = db.Column(db.String(50), nullable=False)
    __mapper_args__ = {
        'polymorphic_identity':'user',
    }
    def __repr__(self):
        return "<Groupe (%d) %s>" % (self.id, self.username)


class Types(db.Model):
    idType = db.Column(db.Integer, primary_key=True)
    nomType = db.Column(db.String(50), nullable=False)
    def __repr__(self):
        return "<Types (%d) %s>" % (self.idType, self.nomType)


class Style(db.Model):
    idStyle = db.Column(db.Integer, primary_key=True)
    nomStyle = db.Column(db.String(50), nullable=False)
    def __repr__(self):
        return "<Style (%d) %s>" % (self.idStyle, self.nomStyle)

class Ressemble(db.Model):
    idStyle1 = db.Column(db.Integer, db.ForeignKey('style.idStyle'), primary_key=True)
    idStyle2 = db.Column(db.Integer, db.ForeignKey('style.idStyle'), primary_key=True)
    def __repr__(self):
        return "<Ressemble (%d) %d>" % (self.idStyle1, self.idStyle2)




@login_manager.user_loader
def load_user(id : int):
    return User.query.get(int(id))

