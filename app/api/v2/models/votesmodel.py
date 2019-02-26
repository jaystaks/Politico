from app.api.db.database import Database
import json


class VotesModel(Database):

    def __init__(self,createdby=None,
        office=None,
        candidate=None):
        self.createdby = createdby
        self.office = office
        self.candidate = candidate

    def save(self, createdby, office, candidate):
        self.curr.execute(
            ''' INSERT INTO voters(createdby, office, candidate)\
                VALUES('{}','{}','{}')\
                RETURNING createdby, office, candidate'''\
            .format(createdby, office, candidate))
        voter = self.curr.fetchall()
        self.conn.commit()
        self.curr.close()
        return votes
