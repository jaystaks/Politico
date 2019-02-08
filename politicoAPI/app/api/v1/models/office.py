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
        custom_msg = None
        if "" in self.offices.values():
            custom_msg = False
        elif (
                self.offices["name"].isspace() or
                self.offices["type"].isspace()
        ):
            custom_msg = False
        else:
            custom_msg = True
        return custom_msg

    def check_for_only_expected_value_types(self):
        custom_msg = None
        if (
                isinstance(self.offices["name"], str) and
                isinstance(self.offices["type"], str)
        ):
            custom_msg = True
        else:
            custom_msg = False
        return custom_msg

    @staticmethod
    def check_whether_office_exists(office_name):
        office_is_present = False
        for each_office in offices:
            if each_office["name"] == name:
                office_is_present = True

        return office_is_present

    @staticmethod
    def get_political_office():
        global offices
        custom_msg = None

        if offices == []:
            custom_msg = {
                "status": 200,
                "data": "The Office list is empty"
            }

        else:
            custom_msg = {
                "status": 200,
                "data": offices
            }
        return custom_msg

    @staticmethod
    def check_id_exists(pid):
        global offices

        if pid in [office["id"] for office in offices]:
            return True
        else:
            return False

    @staticmethod
    def get_an_office(pid):
        global offices
        return [office for office in offices if office['id'] == pid]