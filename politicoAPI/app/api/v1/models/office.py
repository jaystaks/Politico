offices=[]

class PoliticalOffice():
    def __init__(self):
        self.offices = offices

    def create_political_office(self, name, type, id):
        office= {
        "id": len(self.offices)+1,
        "name": name,
        "type": type
        }
        self.offices.append(office)
        return office

    def get_political_office(self):
        return self.offices

    def get_specific_political_office(self, id):
        for office in offices:
            if office.id == id:
                return office
