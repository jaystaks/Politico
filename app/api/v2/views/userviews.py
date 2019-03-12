from flask import make_response, jsonify, request, Blueprint
from flask_jwt_extended import create_access_token

from app.api.v2.models.usermodels import Users
from app.api.v2.utils.validations import is_valid, data_fields, is_alphabet, invalid_email, invalid_phone, invalid_url

user = Blueprint('user', __name__, url_prefix='/api/v2/auth')


class SignUp():
    """ A user can register their details"""

    @user.route("/signup", methods=['POST'])
    def registerUser():
        data = request.get_json()
        errors = {}

        fields = data_fields()

        for field in fields:
            data_field = data.get(field)
            invalid = is_valid(data_field)
            if not data_field:
                errors[field] = '%s is Required!' % (field)
            elif invalid:
                errors[field] = invalid

        for i in range(0, len(fields)):
            field = fields[i]
            if i <= 2:
                invalid = is_alphabet(data.get(field))
                if invalid:
                    errors[field] = invalid
            elif i == 3:
                invalid = invalid_email(data.get(field))
                if invalid:
                    errors[field] = invalid
            elif i == 5:
                invalid = invalid_phone(data.get(field))
                if invalid:
                    errors[field] = invalid
            elif i == 6:
                invalid = invalid_url(data.get(field))
                if invalid:
                    errors[field] = invalid
            '''elif i == 7:
                invalid = data.get(field)
                if invalid :
                    errors[field] = invalid'''

        if errors != {}:
            return make_response(jsonify({
                "status": 400,
                "errors": errors
            }), 400)

        Users(fields[0], fields[1], fields[2], fields[3], fields[4], fields[5], fields[6]).registerUser()

        return make_response(jsonify({
            "status": 201,
            "message": "Success!! Account Created",
            "user": data
        }), 201)


class Login():
    """A user can sign in to their account."""

    @user.route("/login", methods=['POST'])
    def loginUser():
        data = request.get_json()

        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return make_response(jsonify({
                'status': 400,
                'message': 'Credentials not passed in!'
            }))

        user = Users(None, None, None, email, password).fetchEmail()
        if user:
            token = create_access_token(identity=email)
            return make_response(jsonify({
                "status": 200,
                "message": f"Login Successful {email}",
                "Token": token
            }), 200)
        return make_response(jsonify({
            "status": 404,
            "message": "User Not found"
        }), 404)
