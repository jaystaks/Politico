from app.api.db.database import Database


class ResultsModel:
    def __init__(self, id):
        self.id = id
        self.db = Database()

    def get_results(self):
        query = """SELECT candidates,COUNT(*) FROM votes WHERE offices = %s GROUP BY candidates ;"""
        cursor = self.conn.cursor()
        cursor.execute(query, (self.id,))
        self.conn.commit()
        tally = cursor.fetchall()
        if len(tally) < 1:
            return 'Empty'
        return tally
