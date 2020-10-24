from .var_table import VarTable

class Function:
    def __init__(self, type):
        self.name = ""
        self.type = type
        self.vars = VarTable()

    def add_variable(self, var_name, var_type):
        e = None
        # Check if the variable is not in the table already
        for var in self.vars.table:
            if var["name"] == var_name:
                e = "The variable " + var_name + " already exists in the function's variable table"
                return e

        self.vars.table.append({
            'name': var_name,
            'type': var_type
        })

        return e

    

            