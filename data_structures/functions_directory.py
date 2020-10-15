from .function import Function

class FunctionsDirectory:
    def __init__(self):
        self.directory = []
        self.curr_function = None

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
        return e

    def append_variable_to_curr_function(self, name, type):
        self.curr_function.add_variable(name, type)

    def print_var_tables(self):
        for func in self.directory:
            print(func.name)
            for item in func.vars.table:
                print(item["name"], item["type"])


            