from flask import request, Blueprint, jsonify, make_response
import json
from app.api.v1.models.political_model import Political

politicalparty= Blueprint('politicalparty',__name__,url_prefix='/api/politicalparty')

class Party():
    @politicalparty.route('/parties',methods=['POST'])
    def create_political_party():
        party = request.get_json()
        name = party['name']
        hqAddress = party['hqAddress']
        logoUrl = party['logoUrl']

        feedback = Political().create_political_party('id', 'name', 'hqAddress', 'logoUrl')
        return make_response(jsonify({
            "message": "Success!! Party Created"
        }))



    @politicalparty.route('/parties',methods=['GET'])
    def get_political_parties():
        pass

    @politicalparty.route('/parties/<int:id>',methods=['GET'])
    def get_specific_political_party(id):
        pass

    @politicalparty.route('/parties/<int:id>',methods=['PATCH'])
    def edit_political_party(id):
        pass

    @politicalparty.route('/parties/<int:id>',methods=['DELETE'])
    def delete_political_party(id):
        pass
