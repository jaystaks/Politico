from flask import Blueprint, jsonify, make_response
from flask_jwt_extended import jwt_required

from app.api.v2.models.resultsmodel import ResultsModel

result = Blueprint('results', __name__, url_prefix="/api/v2")


@result.route("/office/<id>/result", methods=['GET'])
@jwt_required
def e_results(id):
    if not isinstance(id, int):
        return make_response(jsonify({"status": 400, "error": "Invalid Office Id"}), 400)
    results = ResultsModel(id).get_results()
    if not isinstance(results, list):
        return make_response(jsonify({"status": 404, "error": "Results Not Found"}), 404)
    return make_response(jsonify({"status": 200,
                                  "data": [{
                                      "office": id,
                                      "candidate": results[0][0],
                                      "results": results[0][1]
                                  }]}), 200)
