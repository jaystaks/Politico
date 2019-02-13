from flask import request, Blueprint, jsonify, make_response
from app.api.v1.models.office import PoliticalOffice

politicaloffice= Blueprint('politicaloffice',__name__,url_prefix='/api/v1/')

class Office():
    @politicaloffice.route('/office',methods=['POST'])
    def create_political_office():
        office = request.get_json()
        name = office['name']
        office_type = office['office_type']

        if PoliticalOffice().check_office_type(office_type) is False:
            return make_response(jsonify({
            "status" : 404,
            "error" : "Office type does not exist"
            }), 404)

        if not PoliticalOffice().exists(name):
            offices = PoliticalOffice().create_political_office(name, office_type)
            # Return office data with status code 201: Created
            return make_response(jsonify({
            "status" : 201,
            'message': 'Success!! Office Created',
            'office' : offices

         }))
        else:
            return make_response(jsonify({
                'error': 'Office already Exists!'
                }), 409)

    @politicaloffice.route('/office',methods=['GET'])
    def get_political_office():
        offices = PoliticalOffice().get_political_office()
        if len(offices) == 0: 
            return make_response(jsonify({
                "status" : 404,
                "message" : "List is empty"
                }), 404)
        else:
            return make_response(jsonify({
                "status" : 200,
                'message': 'Success!! offices Found!!',
                'offices' : offices

             }))    

    @politicaloffice.route('/office/<int:office_id>',methods=['GET'])
    def get_specific_political_office(office_id):
        offices = PoliticalOffice().get_specific_political_office(office_id)
        return make_response(jsonify({
            "status" : 200,
            'message': 'Success!! Office found',
            'office': offices
        }))
