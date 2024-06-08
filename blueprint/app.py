from flask import Flask
from blueprints.main import main_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Register Blueprints
    app.register_blueprint(main_blueprint)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
