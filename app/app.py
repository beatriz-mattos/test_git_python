from flask import Flask
from routes import main

def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')
    
    # Importa e registra o blueprint 'main', definido em routes.py
    app.register_blueprint(main)

    return app

if __name__ == '__main__':
    # Cria uma instância do aplicativo e inicia o servidor
    app = create_app()
    app.run()
