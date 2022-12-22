from werkzeug.security import check_password_hash
from flask_login import UserMixin


class User(UserMixin):

    def __init__(self, id, usuario, mail, password, nombre="") -> None:
        self.id = id
        self.usuario = usuario
        self.mail = mail
        self.nombre = nombre
        self.password = password
        
    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)
