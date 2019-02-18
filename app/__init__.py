from flask import Flask, Blueprint
from app.api.v1.views.politicalparty import politicalparty
from app.api.v1.views.politicaloffices import politicaloffice
from instance.config import appConfig
from werkzeug.exceptions import HTTPException


def method_not_json(e):
	"""
    Capture Not Found error.
    """

	return make_response(jsonify({
		"status" : "bad request",
		"message" : "method not allowed, invalid json format"
        }), 400)

def page_not_found(e):
	"""
    Capture Not Found error.
    """

	return make_response(jsonify({
		"status" : "not found",
		"message" : "url does not exist"
        }), 404)

def politico(config_name):
    app= Flask(__name__)

    app.config.from_object(appConfig[config_name])

    app.register_blueprint(politicalparty, url_prefix="/api/v1")
    app.register_blueprint(politicaloffice, url_prefix="/api/v1/")

    app.register_blueprint(politicaloffice, url_prefix="/api/v1")

    return app
