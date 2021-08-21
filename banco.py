from marshmallow import fields
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

ma = Marshmallow()
banco = SQLAlchemy()

#Modelo da classe cliente no banco
class ClienteModelo(banco.Model):
    __tablename__ = 'cliente'
    codigo = banco.Column(banco.Integer, primary_key=True)
    nome = banco.Column(banco.String(250), nullable=False)
    razao_social = banco.Column(banco.String(250), nullable=False)
    cnpj = banco.Column(banco.String(18), nullable=False)
    data_inclusao = banco.Column(banco.TIMESTAMP, server_default=banco.func.current_timestamp(), nullable=False)

    def __init__(self, codigo, nome, razao_social, cnpj):
        self.codigo = codigo
        self.nome = nome
        self.razao_social = razao_social
        self.cnpj = cnpj
        self.data_inclusao = datetime.now()

#Schema
class ClienteSchema(ma.Schema):
    codigo = fields.Integer()
    nome = fields.String(required=True)
    razao_social = fields.String(required=True)
    cnpj = fields.String(required=True)
    data_inclusao = fields.DateTime()
