from flask import request, Blueprint, jsonify, make_response
import json
from app.api.v1.models.political_model import Political

politicalparty= Blueprint('politicalparty',__name__,url_prefix='/api/v1')

class Party():
    @politicalparty.route('/parties',methods=['POST'])
    def create_political_party():
        # Add validation for when the Party with same name exists
        # Return 416
        party = request.get_json()
        name = party['name']
        hqAddress = party['hqAddress']
        logoUrl = party['logoUrl']

        if not Political().exists(name):
            feedback = Political().create_political_party(
            name, hqAddress, logoUrl)
            # Return Party Data with status code 201: Created
            return make_response(jsonify({
            'id': feedback["party_id"],
            'name': feedback["name"]
            }), 201)
        else:
<<<<<<< HEAD
            return make_response(
            jsonify({'error': 'Party already exists!'}),
            416)

=======
            return make_response(jsonify({
            "status" : 409,
            'error': 'Party already exists!',
            "Party": party
            }), 409)
>>>>>>> ch-LFA-Feedback-Implemented-163944167

    @politicalparty.route('/parties/<int:party_id>',methods=['PATCH'])
    def edit_political_party(party_id):
        party_data = request.get_json()
        party = Political().edit_political_party(party_data, party_id)
<<<<<<< HEAD
        return make_response(jsonify({
            "message": "Success!! Party patched",
            "data": party
        }))
=======
        if party:
            return make_response(jsonify({
            "status" : 200,
            "message": "Success!! Party updated",
            "Party": party
            }),200)
        else:
            return make_response(jsonify({
            "status":404,
            "error":"Party Not Found!",
            }),404)
>>>>>>> ch-LFA-Feedback-Implemented-163944167


    @politicalparty.route('/parties/<int:party_id>',methods=['DELETE'])
    def delete_political_party(party_id):
        party = Political().delete_political_party(party_id)
        if party:
<<<<<<< HEAD
            return jsonify({
            "message" : "Success!! Party Deleted",
            "party":party
            })
        return jsonify({
            "message": "Error!! Not Deleted"
        })
=======
            return make_response(jsonify({
            "status" : 200,
            "message" : "Success!! Party Deleted",
            "party":party
            }),200)
        else:
            return make_response(jsonify({
            "status":404,
            "error":"Party Not Found!",
            }),404)
>>>>>>> ch-LFA-Feedback-Implemented-163944167

    @politicalparty.route('/parties/<int:party_id>',methods=['GET'])
    def get_specific_political_party(party_id):
        party = Political().get_specific_political_party(party_id)
<<<<<<< HEAD
        return make_response(jsonify({
            "message": "Success!! Party found",
            "party":party
        }))
=======
        if party:
            return make_response(jsonify({
            "status" : 200,
            "message": "Success!! Party found",
            "party":party
            }),200)
        else:
            return make_response(jsonify({
            "status":404,
            "error":"Party Does not exists!",
            }),404)
>>>>>>> ch-LFA-Feedback-Implemented-163944167

    @politicalparty.route('/parties',methods=['GET'])
    def get_political_parties():
        parties =[]
        parties =Political().get_political_parties()
<<<<<<< HEAD
        return make_response(jsonify({
            "message": "Success!! Parties Listed",
            "parties" : parties
        }))
=======
        if len(parties) == 0:
            return make_response(jsonify({
                "status" : 200,
                "messager" : "List is empty"
                }),200)
        else:
            return make_response(jsonify({
                "status" : 200,
                "message": "Success!! Parties Listed",
                "Parties" : parties
            }),200)
>>>>>>> ch-LFA-Feedback-Implemented-163944167
