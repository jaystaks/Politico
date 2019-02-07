from flask import request, Blueprint, jsonify, make_response
import json
from app.api.v1.models.political_model import Political

politicalparty= Blueprint('politicalparty',__name__,url_prefix='/api/v1')

class Party():
    @politicalparty.route('/parties',methods=['POST'])
    def create_political_party():
        party = request.get_json()
        name = party['name']
        hqAddress = party['hqAddress']
        logoUrl = party['logoUrl']

        feedback = Political().create_political_party(name, hqAddress, logoUrl)
        return make_response(jsonify({
            "message": "Success!! Party Created",
         }))

    @politicalparty.route('/parties',methods=['GET'])
    def get_political_parties():
        parties =[]
        parties =Political().get_political_parties()
        return make_response(jsonify({
            "message": "Success!! Parties Listed",
            "parties" : parties
        }))

    @politicalparty.route('/parties/<int:party_id>',methods=['GET'])
    def get_specific_political_party(party_id):
        party = Political().get_specific_political_party(party_id)
        return make_response(jsonify({
            "message": "Success!! Party found",
            "party":party
        }))

    @politicalparty.route('/parties/<int:party_id>',methods=['PATCH'])
    def edit_political_party(part_id):
        party = Political().edit_political_party(party_id)
        return make_response(jsonify({
            "message": "Success!! Party patched"
        }))

    @politicalparty.route('/parties/<int:id>',methods=['DELETE'])
    def delete_political_party(id):
        pass
