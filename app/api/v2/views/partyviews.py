from flask import make_response, jsonify, request, Blueprint, json
from flask_jwt_extended import jwt_required

from app.api.v2.models.partymodels import PartiesModel

party = Blueprint('party', __name__, url_prefix='/api/v2')


class PartyView():
    @party.route('/parties', methods=['POST'])
    @jwt_required
    def create(self):
        data = request.get_json()
        name = data['name']
        hqaddress = data['hqaddress']
        logourl = data['logourl']

        response = PartiesModel().sav(name, hqaddress, logourl)
        return jsonify({
            "message": "party created successfully!"
        }), 201

    @party.route('/parties', methods=['GET'])
    @jwt_required
    def fetchParties(self):
        return make_response(jsonify({
            "message": "Success Parties found",
            "parties": json.loads(PartiesModel().fetchParty(self))
        }), 200)

    @party.route('/parties/<int:id>', methods=['PATCH'])
    @jwt_required
    def fetchParty(self, id):
        party = PartiesModel().get_party(id)
        party = json.loads(party)
        if party:
            return make_response(jsonify({
                "message": "success party found",
                "party": party
            }), 200)
        return make_response(jsonify({
            "status": "Party not found"
        }), 404)

    @party.route('/parties/<int:id>/delete', methods=['DELETE'])
    @jwt_required
    def delete(self, id):
        data = request.get_json()
        party = PartiesModel().fetchParty(id)
        if party:
            PartiesModel().delete(id)
            return on_success(200, "party deleted")
        return raise_error(404, "party not found")

    @party.route('/parties/<int:id>/edit', methods=['PATCH'])
    def editParty(id):
        data = request.get_json()
        name = data['name']
        hqaddress = data['hqaddress']
        logourl = data['logourl']
        party = PartiesModel().editParty(data, id)
        if party:
            return make_response(jsonify({
                "status": 200,
                "message": "Success!! Party updated",
                "Party": party
            }), 200)
        else:
            return make_response(jsonify({
                "status": 404,
                "error": "Party Not Found!",
            }), 404)
