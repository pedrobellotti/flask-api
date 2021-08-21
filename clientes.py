from flask_restful import Resource, marshal_with, reqparse, fields
from flask import request
from banco import banco, ClienteModelo, ClienteSchema

schemaClientes = ClienteSchema(many=True) #Varios clientes
schemaCliente = ClienteSchema() #Um cliente

campos = {
	'codigo': fields.Integer,
	'nome': fields.String,
	'razao_social': fields.String,
	'cnpj': fields.String,
    'data_inclusao': fields.DateTime
}

class Clientes(Resource):

    #GET - lista todos clientes
    def get(self):
        todosClientes = ClienteModelo.query.all()
        clientes = schemaClientes.dump(todosClientes)
        return {'status': 'success', 'data': clientes}, 200

    #POST - Cria um cliente
    @marshal_with(campos)
    def post(self):
        #Recebe os dados
        parse = reqparse.RequestParser()
        parse.add_argument("codigo", type=int, help="Codigo do cliente", required=True)
        parse.add_argument("nome", type=str, help="Nome do cliente", required=True)
        parse.add_argument("razao_social", type=str, help="Razao social do cliente", required=True)
        parse.add_argument("cnpj", type=str, help="CNPJ do cliente", required=True)
        args = parse.parse_args()
        if not args:
            return {'error': 'Sem dados'}, 400
        result = ClienteModelo.query.filter_by(codigo=args['codigo']).first()
        if result:
            return {'error': 'Cliente com código já existente'}, 400
        cliente = ClienteModelo(codigo=args['codigo'],
            nome=args['nome'],
            razao_social=args['razao_social'],
            cnpj=args['cnpj']
            )
        banco.session.add(cliente)
        banco.session.commit()
        return cliente, 201

    #PUT - Edita um cliente
    def put(self):
        return {"clientes": "PUT"}

    #DELETE - Remove um cliente
    def delete(self):
        return {"clientes": "DELETE"}