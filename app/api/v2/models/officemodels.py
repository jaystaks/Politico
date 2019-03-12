from app.api.db.database import Database

class OfficesModel(Database):

    def __init__(self, name=None, type=None):
        super().__init__()
        self.name = name
        self.type = type

    def save(self, name, type):
        office = Database().execute_query(
            ''' INSERT INTO offices(name, type)\
            VALUES('{}','{}')\
                RETURNING name, type''' \
                .format(name, type))
        self.conn.commit()
        self.cur.close()
        return office
