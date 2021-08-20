from flask import Flask
from clientes import Clientes
from flask_restful import Api
from flask import Blueprint

app = Flask(__name__)

bpApi = Blueprint('api', __name__)
api = Api(bpApi)

# Route
api.add_resource(Clientes, '/clientes')

#Home
@app.route('/', methods=['GET', 'POST'])
def home():
    return "Hello home!"

def main(app):
    app.config.from_object("cfg")
    app.register_blueprint(bpApi, url_prefix='/api')
    app.run(debug=True)

if __name__ == '__main__':
    main(app)
