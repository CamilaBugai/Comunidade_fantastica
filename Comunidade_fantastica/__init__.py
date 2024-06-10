# pip install flask
# Gerar senha,no terminal,python,import secrets,secrets.token_hex(16)
#pip install email_validator
# No formulario html,colocou <form,tem que colocar um token.
#Criar banco dados: instalar; pip install flask-sqlalchemy
# pip install flask-bcrypt
# pip install flask-login


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'e0a2b2c9c200a2ad1a3466da64695e18'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.fantastica'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-danger'


from Comunidade_fantastica import routes