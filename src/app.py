from flask import Flask ,jsonify ,request , render_template , redirect, url_for, flash
# del modulo flask importar la clase Flask y los métodos jsonify,request
from flask_cors import CORS       # del modulo flask_cors importar CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow





app=Flask(__name__)  # crear el objeto app de la clase Flask
CORS(app) #modulo cors es para que me permita acceder desde el frontend al backend
# configuro la base de datos, con el nombre el usuario y la clave
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://LucianaHPeisina:Winterishere1@LucianaHPeisina.mysql.pythonanywhere-services.com/LucianaHPeisina$ProyectoFinal'
# desde el objeto app configuro la URI de la BBDD    user:clave@localhost/nombreBBDD
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['JSON_AS_ASCII'] = False #Unicode para los acentos 
SECRET_KEY = 'B!1w8NAt1T^%kvhUI*S^'
db= SQLAlchemy(app)
ma=Marshmallow(app)



class Noticia(db.Model):   # la clase Noticia hereda de db.Model    
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    tema=db.Column(db.String(100))
    titulo=db.Column(db.String(100))
    descripción=db.Column(db.String(8000))
    imagen=db.Column(db.String(500))
    def __init__(self,tema,titulo,descripción,imagen):   #crea el  constructor de la clase
        self.tema=tema   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.titulo=titulo
        self.descripción=descripción
        self.imagen=imagen

class User(db.Model):   # la clase User hereda de db.Model    
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    usuario=db.Column(db.String(100))
    mail=db.Column(db.String(100))
    nombre=db.Column(db.String(100))
    password=db.Column(db.String(900))
    def __init__(self,usuario,password,nombre,mail):   #crea el  constructor de la clase
        self.usuario=usuario   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.password=password
        self.nombre=nombre
        self.mail=mail

with app.app_context():
    db.create_all()  # crea las tablas
#  ************************************************************
 
class NoticiaSchema(ma.Schema):
    class Meta:
        fields=('id','tema','titulo','descripción','imagen')
noticia_schema=NoticiaSchema()            # para crear un Noticia
noticias_schema=NoticiaSchema(many=True)  # multiples registros
 
class UserSchema(ma.Schema):
    class Meta:
        fields=('id','usuario','password','nombre','mail')
user_schema=UserSchema()            # para crear un User
users_schema=UserSchema(many=True)  # multiples registros
 




# crea los endpoint o rutas (json)
@app.route('/noticias',methods=['GET'])
def get_Noticias():
    all_noticias=Noticia.query.all()     # query.all() lo hereda de db.Model
    result=noticias_schema.dump(all_noticias)  # .dump() lo hereda de ma.schema
    return jsonify(result)
 
@app.route('/noticias/<id>',methods=['GET'])
def get_noticia(id):
    noticia=Noticia.query.get(id)
    return noticia_schema.jsonify(noticia)

@app.route('/noticias/<id>',methods=['DELETE'])
def delete_noticia(id):
    noticia=Noticia.query.get(id)
    db.session.delete(noticia)
    db.session.commit()
    return noticia_schema.jsonify(noticia)

@app.route('/noticias', methods=['POST']) # crea ruta o endpoint
def create_noticia():
    print(request.json)  # request.json contiene el json que envio el cliente
    tema=request.json['tema']
    titulo=request.json['titulo']
    descripción=request.json['descripción']
    imagen=request.json['imagen']
    new_noticia=Noticia(tema,titulo,descripción,imagen)
    db.session.add(new_noticia)
    db.session.commit()
    return noticia_schema.jsonify(new_noticia)

@app.route('/noticias/<id>' ,methods=['PUT'])
def update_noticia(id):
    noticia=Noticia.query.get(id)
   
    
    tema=request.json['tema']
    titulo=request.json['titulo']
    descripción=request.json['descripción']
    imagen=request.json['imagen']
 
    noticia.tema=tema
    noticia.titulo=titulo
    noticia.descripción=descripción
    noticia.imagen=imagen
    db.session.commit()
    return noticia_schema.jsonify(noticia)


@app.route('/usuarios',methods=['GET'])
def get_Users():
    all_users=User.query.all()     # query.all() lo hereda de db.Model
    result=users_schema.dump(all_users)  # .dump() lo hereda de ma.schema
    return jsonify(result)

# PROGRAMA DE LOGIN Y REGISTRO

 
@app.route('/usuarios/<id>',methods=['GET'])
def get_user(id):
    user=User.query.get(id)
    return user_schema.jsonify(user)

@app.route('/usuarios/<id>',methods=['DELETE'])
def delete_user(id):
    user=User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return user_schema.jsonify(user)

@app.route('/usuarios', methods=['POST']) # crea ruta o endpoint
def create_user():
    print(request.json)  # request.json contiene el json que envio el cliente
    usuario=request.json['usuario']
    mail=request.json['mail']
    nombre=request.json['nombre']
    password=request.json['password']
    new_user=User(usuario,mail,nombre,password)
    db.session.add(new_user)
    db.session.commit()
    return user_schema.jsonify(new_user)

@app.route('/usuarios/<id>' ,methods=['PUT'])
def update_user(id):
    user=User.query.get(id)
   
    
    usuario=request.json['usuario']
    mail=request.json['mail']
    nombre=request.json['nombre']
    password=request.json['password']
 
    user.usuario=usuario
    user.mail=mail
    user.nombre=nombre
    user.password=password
    db.session.commit()
    return user_schema.jsonify(user)

@app.route('/edición')
def edición():
    return render_template('crud.html')


# programa principal *******************************
if __name__=='__main__':
    app.run(debug=True, port=5000)  