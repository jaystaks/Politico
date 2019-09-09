from flask import Flask, jsonify
#from flask_jwt_extended import JWTManager

from app.api.db.database import Database, init_app
from app.api.v1.views.politicaloffices import politicaloffice
from app.api.v1.views.politicalparty import politicalparty
from app.api.v2.views.candidateviews import candidate
from app.api.v2.views.officeviews import political_office_bp
from app.api.v2.views.partyviews import party
from app.api.v2.views.petitionviews import petition
from app.api.v2.views.resultsviews import result
from app.api.v2.views.userviews import user
from app.api.v2.views.votesview import vote
from instance.config import appConfig


def error_response(status_code, message=None):
    payload = {
        "status": status_code,
        "error": message
    }
    response = jsonify(payload)
    response.status_code = status_code
    return response


def not_found(e):
    return error_response(404, "Invalid url...")


def bad_request(e):
    return error_response(400, "Bad request, invalid json format")


def invalid_method(e):
    return error_response(405, "Sorry...Method not allowed")


def internal_error(e):
    return error_response(500, "Something's not right")


def politico(config_name):
    app = Flask(__name__)

    app.config.from_object(appConfig[config_name])
    app.config["JSON_SORT_KEYS"] = False
    app.config["TRAP_HTTP_EXCEPTIONS"] = True
    app.config['JWT_SECRET_KEY'] = 'SeCrEt'

    app.register_error_handler(404, not_found)
    app.register_error_handler(400, bad_request)
    app.register_error_handler(405, invalid_method)
    app.register_error_handler(500, internal_error)

    app.register_blueprint(politicalparty, url_prefix="/api/v1")
    app.register_blueprint(politicaloffice, url_prefix="/api/v1/")
    app.register_blueprint(user, url_prefix="/api/v2/auth")
    app.register_blueprint(political_office_bp, url_prefix="/api/v2/")
    app.register_blueprint(vote, url_prefix='/api/v2/')
    app.register_blueprint(petition, url_prefix='/api/v2/')
    app.register_blueprint(party, url_prefix='/api/v2/')
    app.register_blueprint(result, url_prefix="/api/v2")
    app.register_blueprint(candidate, url_prefix="/api/v2")

    init_app(app)
    #JWTManager(app)

    return app
