#Patito Virtual Machine
from operaciones import Operations
import json
import sys

operations = Operations()
quadruples = []
instruction_pointer = 0

op_list = {
    "goto" :            operations.goto,
    "gotof" :           operations.goto_false,
    "+" :               operations.plus_op,
    "-" :               operations.minus_op,
    "*" :               operations.mult_op,
    "/" :               operations.div_op,
    "==" :              operations.eq_op,
    "&" :              operations.and_op,
    "|" :              operations.or_op,
    "!=" :              operations.not_eq_op,
    ">=" :              operations.greater_eq_op,
    "<=" :              operations.less_qp_op,
    ">" :               operations.greater_op,
    "<" :               operations.less_op,
    "=" :               operations.asignation,
    'write':            operations.write,
    'era':              operations.era,
    'parameter':        operations.param,
    'gosub':            operations.gosub,
    'return':           operations.return_val,
    'read' :            operations.read,


    ''''VER':              operations.ver,
    'EBDOROC':          operations.ebdoroc,
    
    'CREATE_MATRIX':    operations.create_matrix,
    'DETERMINANT':      operations.determinant,
    'INVERSE':          operations.inverse,
    'TRANSPOSE':        operations.transpose,
    "+_arr" :           operations.plus_op_arr,
    "-_arr" :           operations.minus_op_arr,
    "*_arr" :           operations.mult_op_arr,
    "WRITE_MAT":        operations.write_mat'''
}

def main():
    global instruction_pointer
    #Check if we have parameters
    if(len(sys.argv) == 2):
        try:
            file = open(sys.argv[1], 'r')
            file_constants = open('c_' + sys.argv[1], 'r')
        except:
            print('File ' + str(sys.argv[1]) + ' not found')
            sys.exit()
        lines = file.readlines()
        constant_lines = file_constants.readlines()
        file_constants.close()
        file.close()
    else:
        print('Missing parameter') 
        sys.exit()

    #Insert quadruples into stack
    for line in lines:
        #Convert to JSON
        line = json.loads(line)
        quadruples.append(line)

    #Dump constants in memory
    operations.load_constants(constant_lines)

    while instruction_pointer < len(quadruples):
        #get the current operation
        new_quad_number = op_list[quadruples[instruction_pointer]['operator']](quadruples[instruction_pointer])
        if new_quad_number:
            instruction_pointer = new_quad_number
        else:
            instruction_pointer += 1
main()