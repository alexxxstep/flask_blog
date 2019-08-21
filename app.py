from flask import Flask
from app_models.config import Configuration
from posts.blueprint import posts
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Configuration)

app.register_blueprint(posts, url_prefix='/blog')

#Соединяем нашу базу данных
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:5562@localhost/test1'
db = SQLAlchemy(app)

