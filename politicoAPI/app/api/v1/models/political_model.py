parties = []

class Political:
    def __init__(self):
        self.data= parties

    def create_political_party(self, id, name, hqAddress, logoUrl):
        party= {
            "party_id": len(self.data)+1,
            "ID": id,
            "name": name,
            "hqAddress": hqAddress,
            "logoUrl": logoUrl,

        }
        self.data.append(party)
        return party
