import re

# Data fields for request being recieved from client
from flask_jwt_extended import get_jwt_identity


def data_fields():
    fields = ["firstname", "lastname", "othername", "email", "password", "phonenumber", "passporturl"]
    return fields


# General Validations that is common in all fields
def is_valid(field):
    if any(map(lambda x: len("".join(str(x).split())) < 1, [field])):
        return 'Nice try...but no....we do not accept blanks'

    if any(map(lambda x: len("".join(str(x).split())) < 3, [field])):
        return 'minimum length should be 3 characters long'

    if any(map(lambda x: len("".join(str(x).split())) > 25, [field])):
        return 'maximum length should be 25 characters long'


# Validations for names to ensure only alphabets are used
def is_alphabet(name):
    if any(map(lambda x: "".join(str(x).split()).isalpha() == False, [name])):
        return "Only alphabets allowed in names"


# Validation for email syntax
def invalid_email(email):
    if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+[a-zA-Z0-9-.]+$)", email):
        return "Invalid email format"


# Validation for passport url https only
def invalid_url(pass_url):
    if not re.match(r'https?://(www\.)?[-a-zA-Z0-9@:%._+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_+.~#?&//=]*)',
                    pass_url):
        return "Invalid passport url format"


# Validation for phone no.....Only numbers from kenya
def invalid_phone(phNo):
    if not re.match(r"^(?:254|\+254|0)?(7(?:(?:[12][0-9])|(?:0[0-8])|(9[0-2]))[0-9]{6})$", phNo):
        return "Invalid phone number format...gotta be part of the 254"


def admin_required(func):
    """ Admin Rights."""

    from functools import wraps
    @wraps(func)
    def wrapper_function(*args, **kwargs):
        users = Users().get_users()
        try:
            cur_user = [
                user for user in users if user['email'] == get_jwt_identity()]
            isadmin = cur_user[0]['True']
            if isadmin != 'admin':
                return {
                           'message': 'Admins only'}, 403
            return func(*args, **kwargs)
        except Exception as e:
            return {"message": e}
        return wrapper_function

        '''
        def valid_phone(variable):
           """Check only kenyan numbers"""
           
           if re.match(r"^(?:254|\+254|0)?(7(?:(?:[12][0-9])|(?:0[0-8])|(9[0-2]))[0-9]{6})$",
                       variable):
               return True
        return False
    
    
        def correct_date_format(variable):
           
           if re.match(r"^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[1,3-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$",
                       variable):
               return True
        return False
    
        def valid_email(variable):
           """validate email"""
    
           if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+[a-zA-Z0-9-.]+$)",
                       variable):
               return True
        return False'''
