from flask import Flask, Blueprint
from app.api.v1.views.politicalparty import politicalparty

def politico():
    app= Flask(__name__)
    app.register_blueprint(politicalparty, url_prefix="/api/v1")

    return app
