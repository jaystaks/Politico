import json

from app.api.db.database import Database


class PartiesModel(Database):

    def __init__(self, name=None,
                 hqaddress=None,
                 logourl=None):
        super().__init__()
        self.name = name
        self.hqaddress = hqaddress
        self.logourl = logourl


def save(self):
    party = Database().execute_query(
        ''' INSERT INTO parties(name, hqaddress, logourl)\
         VALUES('{}','{}','{}')\
         RETURNING name, hqaddress, logourl''' \
            .format(self.name, self.hqaddress, self.logourl))
    return party


def fetchParties(self):
    Database().execute_query(
        ''' SELECT * FROM parties''')
    parties = Database().fetchall()
    return json.dumps(parties, default=str)


def fetchParty(self, id):
    Database().execute_query(
        """ SELECT * FROM parties WHERE id={}""".format(id))
    party = Database().fetchone()
    return json.dumps(party, default=str)


def fetchName(self, name):
    Database().execute_query(
        ''' SELECT * FROM parties WHERE name=%s''', (name,))
    party = Database().fetchone()
    return party


def fetchhqaddress(self, hqaddress):
    Database().execute_query(
        ''' SELECT * FROM parties WHERE hqaddress=%s''', (hqaddress,))
    party = Database().fetchone()
    return party


def fetchLogourl(self, logourl):
    Database().execute_query(''' SELECT * FROM parties WHERE logourl=%s''', (logourl,))
    party = Database().fetchone()
    return party


def delete(self, id):
    Database().execute_query(
        ''' DELETE FROM parties WHERE id=%s''', (id,))


def editParty(self):
    Database().execute_query(
        """UPDATE parties\
        SET name='{}', hqaddress='{}', logourl='{}'\
        WHERE party_id={} RETURNING name, hqaddress, logourl""" \
            .format(self.party_id, self.name, self.hqaddress, self.logourl))
    party = Database().fetchone()
    return party
