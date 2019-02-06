parties = []

class Political():
    def __init__(self):
        self.parties= parties

    def create_political_party(self, name, hqAddress, logoUrl):
        party= {
            "party_id": len(self.parties)+1,
            "name": name,
            "hqAddress": hqAddress,
            "logoUrl": logoUrl

        }
        self.parties.append(party)
        return party

    def get_political_parties(self):
        return self.parties

    def get_specific_political_party(self, party_id):
        if self.parties:
            for party in self.parties:
                if party['party_id'] == party_id:
                    return party

    def edit_political_party():
        self.parties.append(party)
        return party
