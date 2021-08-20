from flask_restful import Resource

class Clientes(Resource):
    def get(self):
        return {"clientes": "GET"}

    def post(self):
        return {"clientes": "POST"}

    def put(self):
        return {"clientes": "PUT"}

    def delete(self):
        return {"clientes": "DELETE"}