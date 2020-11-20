from .var_table import VarTable

class Function:
    def __init__(self, type):
        self.name = ""
        self.type = type
        self.vars = VarTable()
        self.parameters = [] 
        self.quadruple = -1

    def add_variable(self, var_name, var_type, virtual_address):
        e = None
        # Check if the variable is not in the table already
        for var in self.vars.table:
            if var["name"] == var_name:
                raise Exception("La variable " + var_name + " ya está declarada en la función")
                
        self.vars.add(var_name,var_type, virtual_address)

    # todo - check error handling

    def get_variable(self, name):
        return self.vars.get_variable(name)

    def register_parameters(self):
        for var in self.vars.table:
            self.parameters.append(var["type"])
    
    def add_quadruple(self,quadruple_index):
        self.quadruple = quadruple_index

