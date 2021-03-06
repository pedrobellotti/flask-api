from flask_restful import Resource, reqparse
from banco import banco, ClienteModelo, ClienteSchema

schemaClientes = ClienteSchema(many=True) #Varios clientes
schemaCliente = ClienteSchema() #Um cliente

class Clientes(Resource):

    #Le os dados
    def parse(self, req):
        parse = reqparse.RequestParser()
        parse.add_argument("codigo", type=int, help="Codigo do cliente", required=True)
        parse.add_argument("nome", type=str, help="Nome do cliente", required=req)
        parse.add_argument("razao_social", type=str, help="Razao social do cliente", required=req)
        parse.add_argument("cnpj", type=str, help="CNPJ do cliente", required=req)
        args = parse.parse_args()
        return args

    #GET - lista todos clientes
    def get(self):
        try:
            todosClientes = ClienteModelo.query.all()
            clientes = schemaClientes.dump(todosClientes)
            return {'status': '200', 'data': clientes}, 200
        except:
            return {'status': '204', 'message': 'Algum erro aconteceu', 'error': 'Erro na listagem dos clientes'}, 204

    #POST - Cria um cliente
    def post(self):
        #Recebe os dados
        args = self.parse(req=True)
        if not args:
            return {'status': '400', 'message': 'Algum erro aconteceu', 'error': 'Sem dados'}, 400
        result = ClienteModelo.query.filter_by(codigo=args['codigo']).first()
        if result:
            return {'status': '400', 'message': 'Algum erro aconteceu', 'error': 'Cliente com código já existente'}, 400
        try:
            cliente = ClienteModelo(codigo=args['codigo'],
                nome=args['nome'],
                razao_social=args['razao_social'],
                cnpj=args['cnpj']
                )
            banco.session.add(cliente)
            banco.session.commit()
            return {'status': '201', 'message': 'Cliente criado com sucesso', 'error': 'null'}, 201
        except:
            return {'status': '400', 'message': 'Algum erro aconteceu', 'error': 'Erro na criação do cliente'}, 400

    #PUT - Edita um cliente
    def put(self):
        #Recebe os dados
        args = self.parse(req=False)
        if not args:
            return {'status': '400', 'message': 'Algum erro aconteceu', 'error': 'Sem dados'}, 400
        result = ClienteModelo.query.filter_by(codigo=args['codigo']).first()
        if not result:
            return {'status': '404', 'message': 'Algum erro aconteceu', 'error': 'Cliente não existe'}, 404
        try:
            if args['nome']:
                result.nome = args['nome']
            if args['razao_social']:
                result.razao_social = args['razao_social']
            if args['cnpj']:
                result.cnpj = args['cnpj']
            banco.session.commit()
            return {'status': '200', 'message': 'Cliente editado com sucesso', 'error': 'null'}, 200 
        except:
            return {'status': '400', 'message': 'Algum erro aconteceu', 'error': 'Erro ao editar cliente'}, 400

    #DELETE - Remove um cliente
    def delete(self):
        #Recebe os dados
        args = self.parse(req=False)
        if not args:
            return {'status': '400', 'message': 'Algum erro aconteceu', 'error': 'Sem dados'}, 400
        result = ClienteModelo.query.filter_by(codigo=args['codigo']).first()
        if not result:
            return {'status': '404', 'message': 'Algum erro aconteceu', 'error': 'Cliente não existe'}, 404
        try:
            ClienteModelo.query.filter_by(codigo=args['codigo']).delete()
            banco.session.commit()
            return {'status': '200', 'message': 'Cliente removido com sucesso', 'error': 'null'}, 200
        except:
            return {'status': '400', 'message': 'Algum erro aconteceu', 'error': 'Erro na criação do cliente'}, 400