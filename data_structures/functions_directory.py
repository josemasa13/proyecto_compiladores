from .function import Function

class FunctionsDirectory:
    def __init__(self):
        self.directory = []
        self.curr_function = None
        self.types_parameter = []
        self.number_quadruple = []
        self.names = []
        self.size = []

    def add_quadruple(self,index):
        self.number_quadruple.append(index)
        return None

    def add_function_to_global(self, name, type, vaddr):
        self.directory[0].add_variable(name, type, vaddr)

    def search_global(self, var_name):
        global_func = self.directory[0]
        return global_func.get_variable(var_name)




    def search_function(self, name):
        for function in self.directory:
            if function.name == name:
                return function

        return None

    def search_quad(self, name):
        for i in range(len(self.names)):
            if self.names[i] == name:
                return self.number_quadruple[i-1]
        return None

    def add_function(self, type):
        e = None
        # Creating the new function to append
        new_func = Function(type)
        self.curr_function = new_func
        self.directory.append(new_func)
        return e
    
    def add_typesofparameter(self,parameters_type):
        e = None
        self.types_parameter.append(parameters_type)
        return e

    def search_existing_name(self,name):
        for i in range(len(self.names)):
            if self.names[i] == name:
                return self.types_parameter[i-1]
        return -1

    def update_curr_function_name(self, name):
        e = None
        for func in self.directory:
            if func.name == name:
                e = "The function " + name + " was previously declared"
                return e

        self.curr_function.name = name
        self.names.append(name)
        self.directory[len(self.directory) - 1].name = name
        return e

    def append_variable_to_curr_function(self, name, type, virtual_address):
        self.curr_function.add_variable(name, type, virtual_address)

    def add_dim_one(self,name,dim_one):
        self.curr_function.add_one_dim(name,dim_one)

    def add_dim_two(self,name,dim_one,dim_two):
        self.curr_function.add_two_dim(name,dim_one,dim_two)

    def print_var_tables(self):
        for func in self.directory:
            print(func.name)
            for item in func.vars.table:
                print(item["name"], item["type"], item["virtual_address"])

    def print_memory_spaces(self):
        for func in self.directory:
            print(func.name)
            print("Enteros: " + str(func.int_spaces))
            print("Flotantes: " + str(func.float_spaces))
            print("Temporales Enteros: " + str(func.temporal_int_spaces))
            print("Temporales Flotantes: " + str(func.temporal_float_spaces))
            print("Temporales Booleanos: " + str(func.temporal_bool_spaces))
    
    def print_funcs_params(self):
        for func in self.directory:
            print(func.parameters)

    # todo - check error handling
    # si no encuentro en la curr_function, me voy a global
    def get_variable(self, var_name):
        var = None
        for i,func in enumerate(self.directory):
            if func.name == self.curr_function.name:
                var = self.curr_function.get_variable(var_name)

        if var is None:
            global_func = self.directory[0]
            var = global_func.get_variable(var_name)

        return var