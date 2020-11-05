from data_structures import Virtualmemory
import numpy as np
from pandas import DataFrame
import json
import sys

class Operations:
    def __init__(self):
        self.virtual_memory = Virtualmemory()
        self.jump_stack = []
        self.mat_stack = []

    def load_constants(self, constants):
        for i in constants:
            constant = json.loads(i)
            self.virtual_memory.update_memory(
                constant['v_address'],
                constant['constant']
            )

    def asignation(self,quadruple):
        l_operand = quadruple['l_operand']
        result = quadruple['result']
        #Check if the result is a pointer
        if self.virtual_memory.is_pointer(result):
            result = self.virtual_memory.is_pointer(result)
        self.virtual_memory.update_memory(
            result,
            self.virtual_memory.get_value(l_operand)
        )

    def write(self, quadruple):
        value = self.virtual_memory.get_value(
            quadruple['result']
        )
        print(value)

    def lee(self, quadruple):
        value = input()
        try:
            val = int(value)
        except ValueError:
            try:
                val = float(value)
            except ValueError:
                val = value
        result = quadruple['result']
        if self.virtual_memory.is_pointer(result):
            result = self.virtual_memory.is_pointer(result)
        self.virtual_memory.update_memory(
            result,
            val
        )

    def goto(self, quadruple):
        return quadruple['result']

    def goto_false(self, quadruple):
        #Check if the operand is false
        if not self.virtual_memory.get_value(quadruple['l_operand']):
            return quadruple['result']
        return None

    def plus_op(self, quadruple):
        l_operand = self.virtual_memory.get_value(quadruple['l_operand'])
        r_operand = self.virtual_memory.get_value(quadruple['r_operand'])
        self.virtual_memory.update_memory(
            quadruple['result'],
            l_operand + r_operand
        )
        return None

    def minus_op(self, quadruple):
        l_operand = self.virtual_memory.get_value(quadruple['l_operand'])
        r_operand = self.virtual_memory.get_value(quadruple['r_operand'])
        self.virtual_memory.update_memory(
            quadruple['result'],
            l_operand - r_operand
        )
        return None

    def mult_op(self, quadruple):
        l_operand = self.virtual_memory.get_value(quadruple['l_operand'])
        r_operand = self.virtual_memory.get_value(quadruple['r_operand'])
        self.virtual_memory.update_memory(
            quadruple['result'],
            l_operand * r_operand
        )
        return None

    def div_op(self, quadruple):
        l_operand = self.virtual_memory.get_value(quadruple['l_operand'])
        r_operand = self.virtual_memory.get_value(quadruple['r_operand'])
        self.virtual_memory.update_memory(
            quadruple['result'],
            l_operand / r_operand
        )
        return None

    def eq_op(self, quadruple):
        l_operand = self.virtual_memory.get_value(quadruple['l_operand'])
        r_operand = self.virtual_memory.get_value(quadruple['r_operand'])
        self.virtual_memory.update_memory(
            quadruple['result'],
            l_operand == r_operand
        )
        return None


    def and_op(self, quadruple):
        l_operand = self.virtual_memory.get_value(quadruple['l_operand'])
        r_operand = self.virtual_memory.get_value(quadruple['r_operand'])
        self.virtual_memory.update_memory(
            quadruple['result'],
            l_operand and r_operand
        )
        return None

    def or_op(self, quadruple):
        l_operand = self.virtual_memory.get_value(quadruple['l_operand'])
        r_operand = self.virtual_memory.get_value(quadruple['r_operand'])
        self.virtual_memory.update_memory(
            quadruple['result'],
            l_operand or r_operand
        )
        return None

    def not_eq_op(self, quadruple):
        l_operand = self.virtual_memory.get_value(quadruple['l_operand'])
        r_operand = self.virtual_memory.get_value(quadruple['r_operand'])
        self.virtual_memory.update_memory(
            quadruple['result'],
            l_operand != r_operand
        )
        return None

    def greater_eq_op(self, quadruple):
        l_operand = self.virtual_memory.get_value(quadruple['l_operand'])
        r_operand = self.virtual_memory.get_value(quadruple['r_operand'])
        self.virtual_memory.update_memory(
            quadruple['result'],
            l_operand >= r_operand
        )
        return None

    def less_qp_op(self, quadruple):
        l_operand = self.virtual_memory.get_value(quadruple['l_operand'])
        r_operand = self.virtual_memory.get_value(quadruple['r_operand'])
        self.virtual_memory.update_memory(
            quadruple['result'],
            l_operand <= r_operand
        )
        return None

    def greater_op(self, quadruple):
        l_operand = self.virtual_memory.get_value(quadruple['l_operand'])
        r_operand = self.virtual_memory.get_value(quadruple['r_operand'])
        self.virtual_memory.update_memory(
            quadruple['result'],
            l_operand > r_operand
        )
        return None

    def less_op(self, quadruple):
        l_operand = self.virtual_memory.get_value(quadruple['l_operand'])
        r_operand = self.virtual_memory.get_value(quadruple['r_operand'])
        self.virtual_memory.update_memory(
            quadruple['result'],
            l_operand < r_operand
        )
        return None


    def ver(self, quadruple):
        array_index = self.virtual_memory.get_value(quadruple['l_operand'])
        array_llimit = self.virtual_memory.get_value(quadruple['r_operand'])
        array_ulimit = self.virtual_memory.get_value(quadruple['result'])
        #Check the limits
        if(array_index < array_llimit or array_index >= array_ulimit):
            print("Runtime Error: Array out of bounds")
            sys.exit()

    def ebdoroc(self, quadruple):
        #Return tu previos state
        previos_state = self.jump_stack.pop() + 1
        #restore local memory
        self.virtual_memory.restore_local_memory()
        return previos_state

    def eka(self, quadruple):
        self.virtual_memory.new_local_memory()
        return None

    def param(self, quadruple):
        self.virtual_memory.insert_param(
            self.virtual_memory.get_value(quadruple['l_operand'])
        )
        return None
    
    def gosub(self, quadruple):
        self.virtual_memory.save_local_memory()
        self.virtual_memory.update_local_memory()
        self.jump_stack.append(quadruple['quadruple_no'])
        return quadruple['result']

    def return_val(self, qudaruple):
        self.virtual_memory.update_memory(
            qudaruple['l_operand'],
            self.virtual_memory.get_value(qudaruple['result'])
        )
        return None

    
