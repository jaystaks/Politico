offices=[]
expected_offices = ("Federal", "Legislative", "State", "Local Government")

class PoliticalOffice():

    @staticmethod
    def exists(name):
        """
        Checks if an office with the same name exists
        Returns a boolean
        """
        for office in offices:
            if office["name"] == name:
                return True

        return False

    @staticmethod
    def check_office_type(office_type):
        if office_type not in expected_offices:
            return False
        return True


    def create_political_office(self, name, office_type):
        office= {
        "office_id": len(offices)+1,
        "name": name,
        "type": office_type
        }
        offices.append(office)
        return office

    def get_political_office(self):
        if len(offices) == 0: print('List is empty')
        return offices

    def get_specific_political_office(self, office_id):
        for office in offices:
            if office["office_id"] == office_id:
                return office
