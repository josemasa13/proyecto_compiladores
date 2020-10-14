from .function import Function

class FunctionsDirectory:
    def __init__(self):
        self.directory = []

    def add_function(self, name, type):
        e = None
        for func in self.table:
            if directory["name"] == name:
                e = "The function " + name + " was previously declared"
                return e
        
        # Creating the new function to append
        newfunc = Function(name, type)
        self.directory.append(newfunc)

        return e

            