from flask import Flask
from app_models.config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from flask_security import SQLAlchemyUserDatastore
from flask_security import Security

app = Flask(__name__)

app.config.from_object(Configuration)

# Соединяем нашу базу данных
# app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres1@localhost/DataCollector'
app.config['SQLALCHEMY_DATABASE_URI'] = Configuration.SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


# ADMIN
from models import *
admin = Admin(app)
admin.add_view(ModelView(Task, db.session))
admin.add_view(ModelView(Tag, db.session))

# FLASK security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)