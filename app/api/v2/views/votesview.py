from flask import make_response, jsonify, request, Blueprint
from app.api.v2.models.votesmodel import VotesModel
from flask_jwt_extended import jwt_required, get_jwt_identity


vote = Blueprint('votes', __name__)

class Vote():
    @vote.route('/votes', methods=['POST'])
    @jwt_required
    def castVote():
        data = request.get_json()
        createdby = data['createdby']
        office = data['office']
        candidate = data['candidate']

        voter = VotesModel().save(createdby, office, candidate)
        return on_success(201, "successfully voted")