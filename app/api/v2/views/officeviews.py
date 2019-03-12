from flask import Blueprint, make_response, jsonify, request
from flask_jwt_extended import jwt_required

from app.api.v2.models.officemodels import OfficesModel

political_office_bp = Blueprint(
  'political_office_bp', __name__, url_prefix='/api/v2/')


class OfficeView():
    """Creating new office"""

    @political_office_bp.route('/office', methods=['POST'])
    @jwt_required
    def create():
        data = request.get_json()
        name = data['name']
        type = data['type']

        response = OfficesModel().save(name, type)
        return jsonify({
            "message": "office created successfully!",
        }), 201

    @political_office_bp.route('/office', methods=['GET'])
    @jwt_required
    def fetchOffices():
        return make_response(jsonify({
            "message": "success! Offices found",
            "offices": json.loads(OfficesModel().get_offices())
        }), 200)

    @political_office_bp.route('/office/<int:id>', methods=['GET'])
    @jwt_required
    def getSpecific(id):
        office = OfficesModel().get_office_by_id(id)
        office = json.loads(office)
        if office:
            return make_response(jsonify({
                "message": "success Office found",
                "office": office
                }), 200)
        return make_response(jsonify({
            "status": "Office not found"
        }), 404)
