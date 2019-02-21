from werkzeug.security import generate_password_hash, check_password_hash
from app.api.db.database import Database
import json
from flask import jsonify


class Users():
    def __init__(self,
        firstname=None,
		lastname=None,
        othername=None,
		email=None,
		password=None,
		phonenumber=None,
		passporturl=None,
        isadmin=None):
        self.firstname = firstname
        self.lastname = lastname
        self.othername = othername
        self.email = email
        self.password = generate_password_hash(password)
        self.phonenumber = phonenumber
        self.passporturl = passporturl
        self.isadmin = isadmin

    def registerUser(self):
        user = Database().execute_query(
            ''' INSERT INTO users(firstname,lastname,othername,email,password,phonenumber,passporturl,isadmin)\
                VALUES('{}','{}','{}','{}','{}','{}','{}','{}')\
                RETURNING firstname,lastname,othername,email,password,phonenumber,passporturl,isadmin'''\
            .format(self.firstname,self.lastname,self.othername,self.email,self.password,self.phonenumber,self.passporturl,self.isadmin))
        return user


    def auth_token_encode(self, id):
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=0),
                'iat': datetime.datetime.utcnow(),
                'sub': id
            }
            return jwt.encode(
                payload,
                os.getenv('JWT_SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @classmethod
    def decode_auth_token(cls, auth_token):
        try:
            payload = jwt.decode(auth_token, os.getenv('JWT_SECRET_KEY'))
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired! Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token! Please log in again.'


    def fetchUsers(self):
        user = Database().execute_query(''' SELECT * FROM users''')
        return json.dumps(user, default=str)

    def fetchEmail(self):
        user = Database().execute_query("SELECT * FROM users WHERE email= '" + str(self.email) + "'", True)
        return user

    def fetchPhonenumber(self):
        user = Database().execute_query(''' SELECT * FROM users WHERE phonenumber='''+ str(self.phonenumber))
        return user

    def fetchPassporturl(self):
        user = Database().execute_query(''' SELECT * FROM users WHERE passporturl='''+ str(self.passporturl))
        return user

    def generate_hash(self):
        self.password_hash = generate_password_hash(password)


    def check_hash(self, password):
        return check_password_hash(self.password_hash, password)

    def update(self, data):
        for key, item in data.items():
            if key == 'password':
                self.password = self.generate_hash(value)
                setattr(self, key, item)
                self.modified_at = datetime.datetime.utcnow()
        db.conn.commit()

    def delete(self):
        db.conn.delete(self)
        db.conn.commit()

'''    @staticmethod
    def get_all_users():
      return User.query.all()

    @staticmethod
    def get_one_user(id):
      return User.query.get(id)'''
