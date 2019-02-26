from app.api.db.database import Database
from werkzeug.security import generate_password_hash
import json
from flask import jsonify


class PartiesModel(Database):

	def __init__(self,name=None,
		hqaddress=None,
		logourl=None):
		self.name = name
		self.hqaddress = hqaddress
		self.logourl = logourl

	def save(self, name, hqaddress, logourl):
		self.curr.execute(
            ''' INSERT INTO parties(name, hqaddress, logourl)\
             VALUES('{}','{}','{}')\
             RETURNING name, hqaddress, logourl'''\
            .format(name, hqaddress, logourl))
		party = self.curr.fetchall()
		self.conn.commit()
		self.curr.close()
		return party

	def fetchParties(self):
		self.curr.execute(
            ''' SELECT * FROM parties''')
		parties = self.curr.fetchall()
		self.conn.commit()
		self.curr.close()
		return json.dumps(parties, default=str)

	def fetchParty(self, party_id):
		self.curr.execute(
            """ SELECT * FROM parties WHERE id={}""".format(id ))
		party = self.curr.fetchone()
		self.conn.commit()
		self.curr.close()
		return json.dumps(party, default=str)

	def fetchName(self, name):
		self.curr.execute(
            ''' SELECT * FROM parties WHERE name=%s''',(name, ))
		party = self.curr.fetchone()
		self.conn.commit()
		self.curr.close()
		return party

	def fetchhqaddress(self, hqaddress):
		self.curr.execute(
            ''' SELECT * FROM parties WHERE hqaddress=%s''',(hqaddress, ))
		party = self.curr.fetchone()
		self.conn.commit()
		self.curr.close()
		return party

	def fetchLogourl(self, logourl):
		self.curr.execute(''' SELECT * FROM parties WHERE logourl=%s''',(logourl, ))
		party = self.curr.fetchone()
		self.conn.commit()
		self.curr.close()
		return party

	def delete(self, id):
		self.curr.execute(
            ''' DELETE FROM parties WHERE id=%s''',(id, ))
		self.conn.commit()
		self.curr.close()

	def editParty(self, party_id, name, hqaddress, logourl):
		self.curr.execute(
            """UPDATE parties\
			SET name='{}', hqaddress='{}', logourl='{}'\
			WHERE party_id={} RETURNING name, hqaddress, logourl"""\
			.format(party_id,name,hqaddress,logourl))
		party = self.curr.fetchone()
		self.conn.commit()
		self.curr.close()
		return party
