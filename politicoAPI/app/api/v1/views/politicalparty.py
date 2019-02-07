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

    @politicalparty.route('/parties/<int:party_id>',methods=['PATCH'])
    def edit_political_party(party_id):
        parties = request.get_json()
        party = Political().edit_political_party(party_id, parties)
        return make_response(jsonify({
            "message": "Success!! Party patched",
            "data": party
        }))
