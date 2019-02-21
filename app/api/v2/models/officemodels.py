import json
from app.api.db.database import Database
from flask_jwt_extended import jwt_required

class OfficesModel(Database):

    def __init__(self, name=None, type=None):
        self.name = name
        self.type = type

    def save(self, name, type):
        self.curr.execute(
            ''' INSERT INTO offices(name, type)\
            VALUES('{}','{}')\
                RETURNING name, type'''\
            .format(name, type))
        office = self.curr.fetchall()
        self.conn.commit()
        self.curr.close()
        return office
