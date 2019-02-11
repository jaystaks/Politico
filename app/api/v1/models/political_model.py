parties = []

class Political():

    @staticmethod
    def exists(name):
        """
        Checks if a party with the same name exists
        Returns a boolean
        """
        for party in parties:
            if party["name"] == name:
                return True

        return False

    def create_political_party(self, name, hqAddress, logoUrl):
        party= {
            "party_id": len(parties)+1,
            "name": name,
            "hqAddress": hqAddress,
            "logoUrl": logoUrl

        }
        parties.append(party)
        return party

    def get_political_parties(self):
        return parties

    def get_specific_political_party(self, party_id):
        if parties:
            for party in parties:
                if party['party_id'] == party_id:
                    return party

    def edit_political_party(self, data, party_id):
        if parties:
            for party in parties:
                if party['party_id'] == party_id:
                    # return party
                    party["name"] = data.get(
                    'name', party["name"])
                    party["hqAddress"] = data.get(
                    'hqAddress', party["hqAddress"])
                    party["logoUrl"] = data.get(
                    'logoUrl', party["logoUrl"])
                    return parties

    def delete_political_party(self, party_id):
        if parties:
            for party in parties:
                if party['party_id'] == party_id:
                    parties.remove(party)
                    return party
        return None
