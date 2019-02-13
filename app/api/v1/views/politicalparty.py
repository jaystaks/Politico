from flask import request, Blueprint, jsonify, make_response
import json
from app.api.v1.models.political_model import Political

politicalparty= Blueprint('politicalparty',__name__,url_prefix='/api/v1')

class Party():
    @politicalparty.route('/parties',methods=['POST'])
    def create_political_party():
        # Add validation for when the Party with same name exists
        # Return 409
        party = request.get_json()
        name = party['name']
        hqAddress = party['hqAddress']
        logoUrl = party['logoUrl']

        if not Political().exists(name):
            feedback = Political().create_political_party(
            name, hqAddress, logoUrl)

            # Return Party Data with status code 201: Created
            return make_response(jsonify({"Party":[{"message":"Success!! Party Created","code":201,"data": [{
                'id': feedback["party_id"],
                'name': feedback["name"]
            }]}]}),201)
        else:
            return make_response(jsonify({"error":"Party exists","code":409,"data":[party]}),409)

    @politicalparty.route('/parties/<int:party_id>',methods=['PATCH'])
    def edit_political_party(party_id):
        party_data = request.get_json()
        party = Political().edit_political_party(party_data, party_id)
        return make_response(jsonify({"Party":[{"message":"Success!! Party Updated","code":200,"data":[party]}]}),200)

    @politicalparty.route('/parties/<int:party_id>',methods=['DELETE'])
    def delete_political_party(party_id):
        party = Political().delete_political_party(party_id)
        if party:
            return jsonify({"message":"Success!! Party Deleted","code":200,"data":[party]},200)
        else:
            return jsonify({"message":"Forbidden!! Party Not Deleted","code":403,"data":[party]},403)

    @politicalparty.route('/parties/<int:party_id>',methods=['GET'])
    def get_specific_political_party(party_id):
        party = Political().get_specific_political_party(party_id)
        return make_response(jsonify({"Party":[{"message":"Success!! Party found","code":200,"data":[party]}]}),200)

    @politicalparty.route('/parties',methods=['GET'])
    def get_political_parties():
        parties =Political().get_political_parties()
        if len(parties) == 0:
            return make_response(jsonify({"Parties":[{"message":"Sorry, List is Empty","code":404}]}),404)

        else:
            return make_response(jsonify({"Parties":[{"message":"Success!! Parties Found","code":200,"data" : [parties]}]}),200)

