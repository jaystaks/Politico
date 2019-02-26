from flask import Flask, Blueprint
from app.api.v1.views.politicalparty import politicalparty
from app.api.v1.views.politicaloffices import politicaloffice
from app.api.db.database import init_app
from instance.config import appConfig
from app.api.v2.views.userviews import user
from app.api.v1.views.politicalparty import politicalparty
from app.api.v2.views.officeviews import political_office_bp
from app.api.v2.views.votesview import vote
from app.api.v2.views.petitionviews import petition
from app.api.v2.views.partyviews import party
from flask_jwt_extended import JWTManager

def politico(config_name):
    app= Flask(__name__)

    app.config.from_object(appConfig[config_name])
    app.config["JSON_SORT_KEYS"] = False
    app.config["TRAP_HTTP_EXCEPTIONS"] = True
    app.config['JWT_SECRET_KEY'] = 'SeCrEt'


    app.register_blueprint(politicalparty, url_prefix="/api/v1")
    app.register_blueprint(politicaloffice, url_prefix="/api/v1/")
    app.register_blueprint(user, url_prefix="/api/v2/auth")
    app.register_blueprint(political_office_bp, url_prefix="/api/v2/")
    app.register_blueprint(vote, url_prefix='/api/v2/')
    app.register_blueprint(petition, url_prefix='/api/v2/')
    app.register_blueprint(party, url_prefix='/api/v2/')

    init_app(app)
    jwt = JWTManager(app)

    return app
