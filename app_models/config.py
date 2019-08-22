class Configuration(object):
    DEBUG = True
    SECRET_KEY = 'topsecret'
    SQLALCHEMY_DATABASE_URI = 'postgresql://user_pg:5562@localhost/post_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
