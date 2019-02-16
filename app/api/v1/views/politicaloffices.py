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
<<<<<<< HEAD

        offices = PoliticalOffice().create_political_office(name, type)
        return make_response(jsonify({
            "status" : 201,
            'message': 'Success!! Office Created',
            'offices' : offices

         }))
=======
        if PoliticalOffice().check_office_type(type) is False:
            return make_response(jsonify({
            "status" : 404,
            "error" : "Office type does not exist"
            }), 404)
        if not PoliticalOffice().exists(name):
            offices = PoliticalOffice().create_political_office(name, type)
            # Return office data with status code 201: Created
            return make_response(jsonify({"status":201,
            "message":"Success!! Office Created",
            "Office":[offices]}),201)
        else:
            return make_response(jsonify({"status":409,
            "error":"Office exists!",
            "office":[office]}),409)
>>>>>>> ch-LFA-Feedback-Implemented-163944167

    @politicaloffice.route('/office',methods=['GET'])
    def get_political_office():
        offices = PoliticalOffice().get_political_office()
<<<<<<< HEAD
        return make_response(jsonify({
            "status" : 200,
            'message': 'Success!!',
            'offices' : offices

         }))
=======
        if len(offices) == 0:
            return make_response(jsonify({"status":200,
            "message":"Sorry! List is Empty"}),200)
        else:
            return make_response(jsonify({"status":200,
            "message":"Success!! Offices Found",
            "Offices" :[offices]}),200)
>>>>>>> ch-LFA-Feedback-Implemented-163944167

    @politicaloffice.route('/office/<int:office_id>',methods=['GET'])
    def get_specific_political_office(office_id):
        offices = PoliticalOffice().get_specific_political_office(office_id)
<<<<<<< HEAD
        return make_response(jsonify({
            "status" : 200,
            'message': 'Success!! Office found',
            'party': offices
        }))
=======
        if offices:
            return make_response(jsonify({"status":200,
            "message":"Success!! Office found",
            "Office":[offices]}),200)
        else:
            return make_response(jsonify({"status":404,
            "error":"Office Does Not exists!",
            "office":[office]}),404)
>>>>>>> ch-LFA-Feedback-Implemented-163944167
