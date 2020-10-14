class FunctionsTable:
    def __init__():
        self.table = []

    def add_function(self, name, return_type, params):
        e = None
        for func in self.table:
            if func["name"] == name:
                e = "The function " + name + " was previously declared"
                return e

        self.table.append({
            'name': name,
            'return_type': return_type,
            'params': params
        })
        return e

            