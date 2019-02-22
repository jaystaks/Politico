from flask import make_response, jsonify, request, Blueprint
from app.api.v2.models.usermodels import Users
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import create_access_token


user = Blueprint('user', __name__, url_prefix='/api/v2/auth')

class SignUp():
    """ A user can register their details"""

    @user.route("/signup", methods=['POST'])
    def registerUser():
        data = request.get_json()
        errors = {}

        firstname = data.get('firstname')
        if not firstname:
            errors['firstname'] = 'First Name is Required!'

        lastname = data.get('lastname')
        if not lastname:
            errors['lastname'] = 'Last Name is Required!'

        othername = data.get('othername')
        if not othername:
            errors['othername'] = 'Other Name is Required!'

        email = data.get('email')
        if not email:
            errors['email'] = 'Email is Required!'

        password = data.get('password')
        if password:
            hashed_password = generate_password_hash(password)
        else:
            errors['password'] = 'Password is required'

        phonenumber = data.get('phonenumber')
        if not phonenumber:
            errors['phonenumber'] = 'Phone Number is Required!'

        passporturl = data.get('passporturl')
        if not passporturl:
            errors['passporturl'] = 'Passport URL is Required!'

        isadmin = data.get('isadmin')

        if errors != {}:
            return make_response(jsonify({
                "status": 400,
                "errors": errors
            }))

        user = Users(firstname, lastname, othername, email, hashed_password, phonenumber, passporturl, isadmin).registerUser()
        return make_response(jsonify({
        "status":201,
        "message":"Success!! Account Created",
        "user": data
        }),201)

class Login:
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
            "status":200,
            "message": f"Login Successful {email}",
            "Token": token
            }),200)
        return make_response(jsonify({
            "status": 404,
            "message": "User Not found"
            }), 404)
