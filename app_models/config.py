class Configuration(object):
    DEBUG = True
    SECRET_KEY = 'topsecret'
    SQLALCHEMY_DATABASE_URI = 'postgresql://user_pg:5562@localhost/post_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Flask security
    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'

