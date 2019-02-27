from flask import make_response, jsonify, request, Blueprint
from flask_jwt_extended import jwt_required

from app.api.v2.models.candidatesmodel import CandidatesModel
from app.api.v2.models.officemodels import OfficesModel
from app.api.v2.models.usermodels import Users
from app.api.v2.utils.validations import admin_required

candidate = Blueprint('candidates', __name__)


class Candidates:
    """
    Candidates vying f0r office.
    """

    @candidate.route('/candidates/register', methods=['POST'])
    @jwt_required
    @admin_required
    def post(self):

        error = check_candidates_keys(request)
        if error:
            return raise_error(400, "Invalid {} key".format(', '.join(error)))
        data = request.get_json()
        office = data['office']
        candidate = data['candidate']
        party = data['party']

        if OfficesModel().get_office_by_id(office):
            if Users().get_user_by_id(candidate):
                candidate = CandidatesModel().save(office, candidate, party)
                if "error" in candidate:
                    return raise_error(400, "Please check your input and try again!")
                return make_response(jsonify({"status": 201, "msg": "user promoted"}), 201)
            return make_response(jsonify({"status": 404, "msg": "user does not exist"}), 404)
        return make_response(jsonify({"status": 400, "msg": "office does not exist"}), 400)
