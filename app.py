from flask import Flask
from clientes import Clientes
from flask_restful import Api
from flask import Blueprint
from flask_migrate import Migrate
from banco import banco

#Api e blueprint
bpApi = Blueprint('api', __name__)
api = Api(bpApi)

#Rota /api/clientes
api.add_resource(Clientes, '/clientes')

#Cria o app com a cfg.py
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
