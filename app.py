from flask import Flask
from clientes import Clientes
from flask_restful import Api
from flask import Blueprint
from flask_migrate import Migrate
from banco import banco

bpApi = Blueprint('api', __name__)
api = Api(bpApi)

# Route
api.add_resource(Clientes, '/clientes')

def create_app():
    app = Flask(__name__)
    app.config.from_object("cfg")
    app.register_blueprint(bpApi, url_prefix='/api')
    banco.init_app(app)
    migrate = Migrate(app, banco) #Migraçao do banco (flask db init, migrate, upgrade)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
