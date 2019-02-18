from flask import Flask, Blueprint
from app.api.v1.views.politicalparty import politicalparty
from app.api.v1.views.politicaloffices import politicaloffice
from app.api.db.dbconnect import init_app
from instance.config import appConfig

def politico(config_name):
    app= Flask(__name__)

    app.config.from_object(appConfig[config_name])
    app.config.from_pyfile('config.py')
    app.config["JSON_SORT_KEYS"] = False


    app.register_blueprint(politicalparty, url_prefix="/api/v1")
    app.register_blueprint(politicaloffice, url_prefix="/api/v1/")


    init_app(app)

    return app
