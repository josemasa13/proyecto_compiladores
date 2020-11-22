from .var_table import VarTable

class Function:
    def __init__(self, type):
        self.name = ""
        self.type = type
        self.vars = VarTable()
        self.parameters = [] 
        self.quadruple = -1
        self.int_spaces = 0
        self.float_spaces = 0
        self.temporal_int_spaces = 0
        self.temporal_float_spaces = 0
        self.temporal_bool_spaces = 0

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

    def add_one_dim(self,var_name,dim_one):
        self.vars.add_one_dim(var_name,dim_one)

    def add_two_dim(self,var_name,dim_one,dim_two):
        self.vars.add_two_dim(var_name,dim_one,dim_two)