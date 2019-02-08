from flask import Flask, Blueprint
from app.api.v1.views.politicalparty import politicalparty
from app.api.v1.views.politicaloffices import politicaloffice
from instance.config import appConfig

def politico():
    app= Flask(__name__)

    app.config.from_object(appConfig)

    app.register_blueprint(politicalparty, url_prefix="/api/v1")

    app.register_blueprint(politicaloffice, url_prefix="/api/v1")

    return app
