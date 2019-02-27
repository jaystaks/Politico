import json

import psycopg2

from app.api.db.database import Database


class CandidatesModel(Database):

    def __init__(self, office=None, candidate=None, party=None):
        super().__init__()
        self.office = office
        self.candidate = candidate

    def save(self, office, candidate, party):
        """Create a new candidate."""

        try:
            self.cur.execute(
                ''' INSERT INTO candidates(office, candidate, party)\
                VALUES('{}','{}','{}')\
                 RETURNING office, candidate, party''' \
                    .format(office, candidate, party))

            candidate = self.curr.fetchone()
            self.conn.commit()
            self.cur.close()
            return candidate

            query = """
					SELECT offices.name, parties.name, users.email FROM candidates\
					INNER JOIN offices ON candidates.office=offices.id\
					INNER JOIN users ON candidates.candidate=users.id\
					INNER JOIN parties ON candidates.party=parties.id;
					"""

            candidate = self.cur.fetchall()

            self.cur.execute_query(query)
            self.conn.commit()
            self.cur.close()

            return json.dumps(candidate, default=str)
        except psycopg2.IntegrityError:
            return "error"

    def get_candidate_by_id(self, candidate_id):
        """Get candidate with specific id."""

        self.cur.execute(''' SELECT * FROM candidates WHERE id=%s''', (id,))
        candidate = self.cur.fetchone()
        self.conn.commit()
        self.cur.close()
        return json.dumps(candidate, default=str)

    def get_candidates(self):
        """Fetch all candidates."""

        query = "SELECT * from candidates"
        candidates = Database().execute_query(query)
        return json.dumps(candidates, default=str)
