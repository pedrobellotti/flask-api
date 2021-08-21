from flask_restful import Resource

class Clientes(Resource):

    #GET - lista todos clientes
    def get(self):
        return {"clientes": "GET"}

    #POST - Cria um cliente
    def post(self):
        return {"clientes": "POST"}

    #PUT - Edita um cliente
    def put(self):
        return {"clientes": "PUT"}

    #DELETE - Remove um cliente
    def delete(self):
        return {"clientes": "DELETE"}