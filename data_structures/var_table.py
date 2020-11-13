class VarTable:
    def __init__(self):
        self.table = []

    def add(self, var_name, var_type, virtual_address):
        e = None
        # Check if the variable is not in the table already
        for var in self.table:
            if var["name"] == var_name:
                e = "The variable " + var_name + " already exists in the variable table"
                return e

        self.table.append({
            'name': var_name,
            'type': var_type,
            'virtual_address': virtual_address 
        })

        return e

    def search(self, name):
        e = None
        for var in self.table:
            if var["name"] == name:
                return var, e
        
        e = "The variable " + name + " is not declared"
        return None, e

    # todo - check error handling
    def get_variable(self, name):
        for i,var in enumerate(self.table):
            if var["name"] == name:
                return var

    

        

