from data_structures.virtualmemory import Virtualmemory
import numpy as np
from pandas import DataFrame
import json
import sys

# regresar error en todas las operaciones si alguno de los operadores es none
class Operations:
    def __init__(self):
        self.virtual_memory = Virtualmemory()
        self.jump_stack = []
        self.mat_stack = []

    def load_constants(self, constants):
        for constant in constants:
            self.virtual_memory.update_memory(
                constant['v_address'],
                constant['constant']
            )
            
    def asignation(self,quadruple):
        l_operand = quadruple.operando_izq
        resultado = quadruple.resultado
        #Check if the resultado is a pointer
        if self.virtual_memory.is_pointer(resultado):
            resultado = self.virtual_memory.is_pointer(resultado)
        self.virtual_memory.update_memory(
            resultado,
            self.virtual_memory.get_value(l_operand)
        )

    def write(self, quadruple):
        value = self.virtual_memory.get_value(
            quadruple.resultado
        )
        print(value)

    def read(self, quadruple):
        value = input()
        try:
            val = int(value)
        except ValueError:
            try:
                val = float(value)
            except ValueError:
                val = value
        resultado = quadruple.resultado
        if self.virtual_memory.is_pointer(resultado):
            resultado = self.virtual_memory.is_pointer(resultado)
        self.virtual_memory.update_memory(
            resultado,
            val
        )

    def goto(self, quadruple):
        return quadruple.resultado

    def goto_false(self, quadruple):
        #Check if the operand is false
        if not self.virtual_memory.get_value(quadruple.operando_izq):
            return quadruple.resultado
        return None

    def plus_op(self, quadruple):
        l_operand = self.virtual_memory.get_value(quadruple.operando_izq)
        r_operand = self.virtual_memory.get_value(quadruple.operando_der)
        self.virtual_memory.update_memory(
            quadruple.resultado,
            l_operand + r_operand
        )
        return None

    def plus_op_esp(self, quadruple):
        l_operand = self.virtual_memory.get_value(quadruple.operando_izq)
        r_operand = quadruple.operando_der
        self.virtual_memory.update_memory(
            quadruple.resultado,
            l_operand + r_operand
        )
        return None

    def minus_op(self, quadruple):
        l_operand = self.virtual_memory.get_value(quadruple.operando_izq)
        r_operand = self.virtual_memory.get_value(quadruple.operando_der)
        self.virtual_memory.update_memory(
            quadruple.resultado,
            l_operand - r_operand
        )
        return None

    def mult_op(self, quadruple):
        l_operand = self.virtual_memory.get_value(quadruple.operando_izq)
        r_operand = self.virtual_memory.get_value(quadruple.operando_der)
        self.virtual_memory.update_memory(
            quadruple.resultado,
            l_operand * r_operand
        )
        return None

    def div_op(self, quadruple):
        l_operand = self.virtual_memory.get_value(quadruple.operando_izq)
        r_operand = self.virtual_memory.get_value(quadruple.operando_der)
        self.virtual_memory.update_memory(
            quadruple.resultado,
            l_operand / r_operand
        )
        return None

    def eq_op(self, quadruple):
        l_operand = self.virtual_memory.get_value(quadruple.operando_izq)
        r_operand = self.virtual_memory.get_value(quadruple.operando_der)
        self.virtual_memory.update_memory(
            quadruple.resultado,
            l_operand == r_operand
        )
        return None


    def and_op(self, quadruple):
        l_operand = self.virtual_memory.get_value(quadruple.operando_izq)
        r_operand = self.virtual_memory.get_value(quadruple.operando_der)
        self.virtual_memory.update_memory(
            quadruple.resultado,
            l_operand and r_operand
        )
        return None

    def or_op(self, quadruple):
        l_operand = self.virtual_memory.get_value(quadruple.operando_izq)
        r_operand = self.virtual_memory.get_value(quadruple.operando_der)
        self.virtual_memory.update_memory(
            quadruple.resultado,
            l_operand or r_operand
        )
        return None

    def not_eq_op(self, quadruple):
        l_operand = self.virtual_memory.get_value(quadruple.operando_izq)
        r_operand = self.virtual_memory.get_value(quadruple.operando_der)
        self.virtual_memory.update_memory(
            quadruple.resultado,
            l_operand != r_operand
        )
        return None

    def greater_eq_op(self, quadruple):
        l_operand = self.virtual_memory.get_value(quadruple.operando_izq)
        r_operand = self.virtual_memory.get_value(quadruple.operando_der)
        self.virtual_memory.update_memory(
            quadruple.resultado,
            l_operand >= r_operand
        )
        return None

    def less_qp_op(self, quadruple):
        l_operand = self.virtual_memory.get_value(quadruple.operando_izq)
        r_operand = self.virtual_memory.get_value(quadruple.operando_der)
        self.virtual_memory.update_memory(
            quadruple.resultado,
            l_operand <= r_operand
        )
        return None

    def greater_op(self, quadruple):
        l_operand = self.virtual_memory.get_value(quadruple.operando_izq)
        r_operand = self.virtual_memory.get_value(quadruple.operando_der)
        self.virtual_memory.update_memory(
            quadruple.resultado,
            l_operand > r_operand
        )
        return None

    def less_op(self, quadruple):
        l_operand = self.virtual_memory.get_value(quadruple.operando_izq)
        r_operand = self.virtual_memory.get_value(quadruple.operando_der)
        self.virtual_memory.update_memory(
            quadruple.resultado,
            l_operand < r_operand
        )
        return None


    def ver(self, quadruple):
        array_index = self.virtual_memory.get_value(quadruple.operando_izq)
        array_llimit = self.virtual_memory.get_value(quadruple.operando_der)
        array_ulimit = self.virtual_memory.get_value(quadruple.resultado)


        if not array_index:
            print("Error de ejecución: la posición no existe en el arreglo")
            sys.exit()

        #Check the limits
        if(array_index < array_llimit or array_index >= array_ulimit):
            print("Runtime Error: Array out of bounds")
            sys.exit()

    def endfunc(self, quadruple):
        #Return tu previos state
        previos_state = self.jump_stack.pop() + 1
        #restore local memory
        self.virtual_memory.restore_local_memory()
        return previos_state

    def era(self, quadruple):
        self.virtual_memory.new_local_memory()
        return None

    def param(self, quadruple):
        self.virtual_memory.insert_param(
            self.virtual_memory.get_value(quadruple.operando_izq)
        )
        return None
    
    def gosub(self, quadruple, number):
        self.virtual_memory.save_local_memory()
        self.virtual_memory.update_local_memory()
        self.jump_stack.append(number)
        return quadruple.resultado

    def return_val(self, quadruple):
        self.virtual_memory.update_memory(
            quadruple.operando_izq,
            self.virtual_memory.get_value(quadruple.resultado)
        )
        return None

    
