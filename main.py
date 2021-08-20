from flask import Flask
from clientes import bpClientes

app = Flask(__name__)

#Blueprint para parte de clientes
app.register_blueprint(bpClientes, url_prefix='/clientes')

#Home
@app.route('/', methods=['GET', 'POST'])
def home():
    return "Hello home!"

if __name__ == '__main__':
    app.run()
