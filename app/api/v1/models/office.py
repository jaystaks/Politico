offices=[]

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

    def create_political_office(self, name, type):
        office= {
        "office_id": len(offices)+1,
        "name": name,
        "type": type
        }
        offices.append(office)
        return office

    def check_any_for_empty_fields(self):
        message = None
        if "" in offices.values():
            message = False
        elif (
                offices["name"].isspace() or
                offices["type"].isspace()
        ):
            message = False
        else:
            message = True
        return message

    def check_for_only_expected_value_types(self):
        message = None
        if (
                isinstance(offices["name"], str) and
                isinstance(offices["type"], str)
        ):
            message = True
        else:
            message = False
        return message

    def get_political_office(self):
        return offices

    def get_specific_political_office(self, office_id):
        for office in offices:
            if office["office_id"] == office_id:
                return office
