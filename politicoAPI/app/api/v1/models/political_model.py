data = []


class Political():
    def __init__(self):
        self.data = data

    def create_political_party(self, name, hqAddress, logoUrl):
        party = {
            "party_id": len(self.data)+1,
            "name": name,
            "hqAddress": hqAddress,
            "logoUrl": logoUrl

        }
        data.append(self.data)
        message = {
            "status": 201,
            "data": [{
                "party_id": self.data["party_id"],
                "name": self.data["name"]
            }]
        }
        return message

    def get_data(self):
        party= data
        message = None

        if data == []:
            message = {
                "status": 200,
                "data": "The Party list is empty"
            }

        else:
            message = {
                "status": 200,
                "data": data
            }
        return message

    def check_for_valid_party_name(name):
        if isinstance(name, str):
            return len(name.strip()) < 1
        else:
            return False

    def get_specific_political_party(self, party_id):
        if self.data:
            for party in self.data:
                if party['party_id'] == party_id:
                    return party

    def edit_political_party(self, data, party_id):
        part = data
        for party in data:
            if party['party_id'] == pid:
                party['name'] = user_data["name"]

                return [{"party_id": pid, "name": user_data["name"]}]

    def delete_political_party(self, party_id):
        if self.data:
            for party in self.data:
                if party.get('party_id') == party_id:
                    self.data.remove(party)
                    return party

    def get_specific_political_party(self, party_id):
        if self.parties:
            for party in self.parties:
                if party['party_id'] == party_id:
                    return party

    def get_political_parties(self):
        return self.parties

