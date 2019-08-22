from flask import Flask
from app_models.config import Configuration
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(Configuration)



# Соединяем нашу базу данных
# app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres1@localhost/DataCollector'
app.config['SQLALCHEMY_DATABASE_URI'] = Configuration.SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app)
