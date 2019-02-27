from app.api.db.database import Database


class PetitionsModel(Database):

    def __init__(self, createdby=None,
                 office=None,
                 body=None):
        super().__init__()
        self.createdby = createdby
        self.office = office
        self.body = body

    def save(self, createdby, office, body):
        self.cur.execute(
            ''' INSERT INTO petitions(createdby, office, body)\
                VALUES('{}','{}','{}')\
                RETURNING createdby, office, body''' \
                .format(createdby, office, body))
        petition = self.cur.fetchall()
        self.conn.commit()
        self.cur.close()
        return petition
