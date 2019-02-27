class BaseModel():

    def __init__(self):
        self.table_name = "Base"
        self.exist_check_field = None
        self.db = None

    def select_all(self):
        query = "SELECT * FROM " + self.table_name + " ;"
        result = self.db.execute_query(query, True)
        return result

    def select_specific(self, select_field, select_data):
        query = "SELECT * FROM " \
                + self.table_name + " WHERE " + select_field + "='" + select_data \
                + "' ;"
        result = self.db.execute_query(query, True)
        return result

    def insert_data(self, col, data):
        query = "INSERT INTO " + self.table_name + " " + str(
            tuple(col)).replace("'", "") + " VALUES " + str(
            tuple(data)) + " RETURNING ID ;"

        result = self.db.execute_query(query, True)
        return result

    def update_specific(self, col, data, id):
        count = 0
        update_data = []

        for x in col:
            update_data.append(x + "= '" + data[count] + "'")
            count = count + 1

        set_string = str(
            tuple(update_data)
        ).replace(")", "").replace("(", "").replace('"', "")

        if len(col) == 1:
            set_string = set_string.replace(",", "")

        query = "UPDATE " + self.table_name + " SET " + set_string \
                + " WHERE ID=" + str(id) + ";"
        self.db.execute_query(query)

    def delete_specific(self, id):
        query = "DELETE FROM " + self.table_name \
                + " WHERE id='" + str(id) + "';"
        self.db.execute_query(query)

    def check_exists(self, data):

        if self.exist_check_field:
            result = self.select_specific(self.exist_check_field, data[self.exist_check_field])
            if len(result) > 0:
                return True
            else:
                return False
        else:
            return True

    def check_constraints(self, data):
        return None
