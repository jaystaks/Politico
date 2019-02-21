from flask import request, jsonify, make_response
from app.api.db.base_model import BaseModel

class BaseView(BaseModel):

    def __init__(self):
        self.allowed_fields = None
        self.name = None
        BaseModel = None

    def create_endpoint(self):
        data = request.get_json()
        data_fields = list(data.keys())
        field_values = list(data.values())

        if self.allowed_fields:
            if not set(data_fields) == set(self.allowed_fields):
                return jsonify({
                    "status": 400,
                    "error": "Missing or Extra Data Fields Passed!"
                }), 400

        if BaseModel().check_exists(data):
            return jsonify({
                "status": 409,
                "error": self.name + " Already Exists!"
            }), 409

        constraint_result = BaseModel.check_constraints(data)
        if constraint_result:
            return jsonify({
                "status": 400,
                "error": constraint_result
            }), 400

        created_id = BaseModel.insert_data(data_fields, field_values)
        created_data = BaseModel.select_specific(
            "ID", str(created_id[0]['id']))
        return jsonify({
            "status": 201,
            "data": created_data
        }), 201

    def view_endpoint(self):
        data_list = BaseModel.select_all(self)

        return jsonify({
            "status": 200,
            "data": data_list
        }), 200

    def view_specific_endpoint(self, id):
        data_list = BaseModel.select_specific('ID', str(id))

        return jsonify({
            "status": 200,
            "data": data_list
        }), 200

    def delete_endpoint(self, id):
        BaseModel.delete_specific(id)

        return jsonify({
            "status": 200,
            "message": self.name + " Deleted!"
        }), 200

    def update_endpoint(self, id):
        data = request.get_json()
        data_fields = list(data.keys())
        data_values = list(data.values())

        if self.allowed_fields:
            if not set(data_fields).issubset(set(self.allowed_fields)):
                return jsonify({
                    "status": 400,
                    "error": "Invalid data passed in!"
                }), 400

        constraint_result = BaseModel.check_constraints(data)
        if constraint_result:
            return jsonify({
                "status": 400,
                "error": constraint_result
            })

        BaseModel.update_specific(data_fields, data_values, id)
        data = BaseModel.select_specific('ID', str(id))
        return jsonify({
            "status": 200,
            "data": data
        })
