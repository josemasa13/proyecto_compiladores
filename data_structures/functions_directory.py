from .function import Function

class FunctionsDirectory:
    def __init__(self):
        self.directory = []
        self.curr_function = None


    def search_function(self, name):
        for function in self.directory:
            if function.name == name:
                return function

        return None

    def add_function(self, type):
        e = None
        
        # Creating the new function to append
        new_func = Function(type)
        self.curr_function = new_func
        self.directory.append(new_func)

        return e

    def update_curr_function_name(self, name):
        e = None

        for func in self.directory:
            if func.name == name:
                e = "The function " + name + " was previously declared"
                return e

        self.curr_function.name = name
        self.directory[len(self.directory) - 1].name = name
        return e

    def append_variable_to_curr_function(self, name, type, virtual_address):
        self.curr_function.add_variable(name, type, virtual_address)


    def print_var_tables(self):
        for func in self.directory:
            print(func.name)
            for item in func.vars.table:
                print(item["name"], item["type"], item["virtual_address"])
    
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


            