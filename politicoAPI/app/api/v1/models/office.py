offices=[]

class PoliticalOffice():
    def __init__(self):
        self.offices = offices
        
    def create_political_office(self, name, type):
        office= {
        "office.id": len(self.offices)+1,
        "name": name,
        "type": type
        }
        self.offices.append(office)
        return office
      
    def get_specific_political_office(self):
        for office in offices:
            if office.id == id:
                return office

    def check_any_for_empty_fields(self):
        message = None
        if "" in self.offices.values():
            message = False
        elif (
                self.offices["name"].isspace() or
                self.offices["type"].isspace()
        ):
            message = False
        else:
            message = True
        return message

    def check_for_only_expected_value_types(self):
        message = None
        if (
                isinstance(self.offices["name"], str) and
                isinstance(self.offices["type"], str)
        ):
            message = True
        else:
            message = False
        return message
      
    def get_political_office(self):
        return self.offices

    def get_specific_political_office(self, id):
        for office in offices:
            if office.id == id:
                return office
