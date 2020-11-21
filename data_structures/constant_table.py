class Constanttable:
    def __init__(self):
        self.table = []

    
    def insert_constant(self, constant, const_type, vAddress):
        #Check if the constant already exists
        for i in self.table:
            if i['constant'] == constant:
                return i['v_address']

        new_constant = {
            'constant' :    constant,
            'type' :        const_type,
            'v_address' :   self.start_address
        }
        self.start_address += 1
        if(self.start_address < 20000):
            self.table.append(new_constant)
            return new_constant['v_address']
        else:
            print("Memory overflow")

    def display_table(self):
        print("Displaying constant table")
        print("Cons \t Type \t Address")
        for i in self.table:
            print(
                str(i["constant"]) + '\t' +
                i["type"] + '\t' +
                str(i["v_address"])
            )