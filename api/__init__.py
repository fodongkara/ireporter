from flask import Flask, Blueprint
from api.views.red_flag_routes import red_flag_blueprint


def create_app():
    app = Flask(__name__)
    app.register_blueprint(red_flag_blueprint, url_prefix="/api/v1")

    return app
