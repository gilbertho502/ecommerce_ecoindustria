from flask import Flask
from app import config
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app= Flask(__name__)
cors = CORS(app)
app.secret_key = os.urandom(24)
app.config['CORS_HEADERS']= 'Content-Type'

#conexion a la bd

app.config.from_object(config.Config)
db = SQLAlchemy(app)

from app import routers, models
