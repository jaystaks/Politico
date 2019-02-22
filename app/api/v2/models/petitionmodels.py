from app.api.db.database import Database
import json


class PetitionsModel(Database):

    def __init__(self,createdby=None,
        office=None,
        body=None):
        self.createdby = createdby
        self.office = office
        self.body = body

    def save(self, createdby, office, body):
        self.curr.execute(
            ''' INSERT INTO petitions(createdby, office, body)\
                VALUES('{}','{}','{}')\
                RETURNING createdby, office, body'''\
            .format(createdby, office, body))
        petition = self.curr.fetchall()
        self.conn.commit()
        self.curr.close()
        return petition
