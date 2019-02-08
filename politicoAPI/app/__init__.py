from flask import Flask, Blueprint
from app.api.v1.views.politicalparty import politicalparty
from app.api.v1.views.politicaloffices import politicaloffice
from instance.config import appConfig

def politico(config_name):
    app= Flask(__name__)

    app.config.from_object(appConfig[config_name])

    app.register_blueprint(politicalparty, url_prefix="/api/v1")
    app.register_blueprint(politicaloffice, url_prefix="/api/v1/")

    app.register_blueprint(politicaloffice, url_prefix="/api/v1")

    return app
