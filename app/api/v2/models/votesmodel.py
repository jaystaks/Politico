from app.api.db.database import Database


class VotesModel(Database):

    def __init__(self, createdby=None,
                 office=None,
                 candidate=None):
        super().__init__()
        self.createdby = createdby
        self.office = office
        self.candidate = candidate

    def save(self, createdby, office, candidate):
        self.cur.execute(
            ''' INSERT INTO voters(createdby, office, candidate)\
                VALUES('{}','{}','{}')\
                RETURNING createdby, office, candidate''' \
                .format(createdby, office, candidate))
        votes = self.cur.fetchall()
        self.conn.commit()
        self.cur.close()
        return votes
