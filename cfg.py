import os
basedir = os.path.abspath(os.path.dirname(__file__))
#Banco
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = "postgresql://pedro:pedro1@localhost/prova"