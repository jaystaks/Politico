from flask import make_response, jsonify, request, abort, Blueprint
from app.api.v2.models.petitionmodels import PetitionsModel
from flask_jwt_extended import jwt_required, get_jwt_identity


petition = Blueprint('petitions', __name__)

class Petition:
    @petition.route('/petitions', methods=['POST'])
    @jwt_required
    def create():
        data = request.get_json()
        createdby = data['createdby']
        office = data['office']
        body = data['body']

        petition = PetitionsModel().save(createdby, office, body)
        return on_success(201, "Success! Petition submitted")