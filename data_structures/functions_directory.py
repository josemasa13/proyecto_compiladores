from .function import Function

class FunctionsDirectory:
    def __init__(self):
        self.directory = []
        self.curr_function = None
        self.global_mem = 1000
        self.local_mem = 8000
        self.constant_mem = 15000
        self.temporal_mem = 20000


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
        # restarting the local counter
        self.local_int_mem = 8000
        self.constant_mem = 15000

        for func in self.directory:
            if func.name == name:
                e = "The function " + name + " was previously declared"
                return e

        self.curr_function.name = name
        self.directory[len(self.directory) - 1].name = name
        return e

    def append_variable_to_curr_function(self, name, type):
        if self.curr_function.name == "global":
            self.curr_function.add_variable(name, type, self.global_mem)
            self.global_mem += 1

        else:
            self.curr_function.add_variable(name, type, self.local_mem)
            self.local_mem += 1


    def print_var_tables(self):
        for func in self.directory:
            print(func.name)
            for item in func.vars.table:
                print(item["name"], item["type"], item["virtual_address"])

    # todo - check error handling
    # si no encuentro en la curr_function, me voy a global
    def get_address(self, var_name):
        for i, func in enumerate(self.directory):
            if func.name == self.curr_function.name:
                return(i, self.curr_function.get_address(var_name))


            