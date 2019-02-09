from flask import request, Blueprint, jsonify, make_response
import json
from app.api.v1.models.office import PoliticalOffice

politicaloffice= Blueprint('politicaloffice',__name__,url_prefix='/api/v1/')

class Office():
    @politicaloffice.route('/office',methods=['POST'])
    def create_political_office():
        office = request.get_json()
        name = office['name']
        type = office['type']

        offices = PoliticalOffice().create_political_office(name, type, id)
        return make_response(jsonify({
            "status" : 201,
            "message": "Success!! Office Created",
            "offices" : offices

         }))

    @politicaloffice.route('/office',methods=['GET'])
    def get_political_office():
        offices = PoliticalOffice().get_political_office()
        return make_response(jsonify({
            "status" : 200,
            "message": "Success!!",
            "offices" : offices

         }))

    @politicaloffice.route('/office/<int:id>',methods=['GET'])
    def get_specific_political_office(id):
        offices = PoliticalOffice().get_specific_political_office(id)
        return make_response(jsonify({
            "status" : 200,
            "message": "Success!! Office found",
            "party": offices
        }))
