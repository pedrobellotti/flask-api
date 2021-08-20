from flask import Blueprint

bpClientes = Blueprint('clientes', __name__)

@bpClientes.route('/', methods=['GET', 'POST'])
def clientes():
    return {"teste": "hello clientes!"}
