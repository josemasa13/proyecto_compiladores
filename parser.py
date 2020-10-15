import ply.yacc as yacc
from scanner import tokens
from data_structures.functions_directory import FunctionsDirectory

fun_dict = FunctionsDirectory()

# programa
def p_program(p):
    '''program : PRO ID r_register_global PTOCOM opvars opfunciones MAIN PARIZQ PARDER bloque'''

def p_opvars(p):
    '''opvars : vars
    | empty'''

def p_opfunciones(p):
    '''opfunciones : funciones opfunciones
    | empty'''

def p_vars(p):
    '''vars : VARTOKEN tipo ID arr arr varciclo PTOCOM tipociclo'''

def p_varciclo(p):
    '''varciclo : COMA ID arr arr varciclo
    | empty'''

def p_arr(p):
    '''arr : CORIZQ CTEI CORDER
    | empty'''

def p_tipociclo(p):
    '''tipociclo : tipo opciontipo
    | empty'''

def p_opciontipo(p):
    '''opciontipo : ID arr arr varciclo PTOCOM tipociclo
    | MODULE ID PARIZQ opcionvarsimple PARDER opvars bloquefunc'''

def p_tipo(p):
    '''tipo : INT r_register_variables
    | FLT r_register_variables
    | CHAR r_register_variables'''

def p_tipo_func(p):
    '''tipo_func : INT r_register_function
    | FLT r_register_function
    | CHAR r_register_function
    '''

def p_varsimple(p):
    '''varsimple : tipo ident'''

def p_funciones(p):
    '''funciones : funcionvoid 
    | funcion'''

def p_funcionvoid(p):
    '''funcionvoid : VOID r_register_function MODULE ID r_update_curr_function_name PARIZQ opcionvarsimple PARDER opvars bloque'''

def p_opcionvarsimple(p):
    '''opcionvarsimple : varsimple ciclovarsimple
    | empty'''

def p_ciclovarsimple(p):
    '''ciclovarsimple : COMA varsimple ciclovarsimple
    | empty'''

def p_funcion(p): 
    '''funcion : tipo_func MODULE ID r_update_curr_function_name PARIZQ opcionvarsimple PARDER opvars bloquefunc'''

def p_ident(p):
    '''ident : ID arrini arrini'''

def p_arrini(p):
    '''arrini : CORIZQ CORDER
    | empty'''

def p_bloque(p):
    '''bloque : KEYIZQ bloqueopcion KEYDER'''

def p_bloqueopcion(p):
    '''bloqueopcion : estatuto bloqueopcion
    | empty'''

def p_bloquefunc(p):
    '''bloquefunc : KEYIZQ bloqueopcionfunc KEYDER'''

def p_bloqueopcionfunc(p):
    '''bloqueopcionfunc : estatutofunc bloqueopcionfunc
    | empty'''

def p_estatuto(p):
    '''estatuto : asignacion
    | decision
    | escritura
    | llamadafunc
    | repeticion
    | lectura'''

def p_estatutofunc(p):
    '''estatutofunc : asignacion
    | decisionfunc
    | escritura
    | llamadafunc
    | repeticionfunc
    | lectura
    | RETURN PARIZQ expresion PARDER PTOCOM
    '''

def p_asignacion(p):
    '''asignacion : ID asignacionarr asignacionarr IGU expresion PTOCOM'''

def p_asignacionarr(p):
    '''asignacionarr : CORIZQ expresion CORDER
    | empty
    '''

def p_expresion(p):
    '''expresion : exp expresionsig'''

def p_expresionsig(p):
    '''expresionsig : MAY expresionsigequal exp
    | MEN expresionsigequal exp
    | DIF exp
    | IGUIGU exp
    | AND exp
    | OR exp
    | empty'''

def p_expresionsigequal(p):
    '''expresionsigequal : IGU
    | empty'''

def p_exp(p):
    '''exp : termino expciclo'''

def p_expciclo(p):
    '''expciclo : MAS exp
    | MENOS exp
    | empty
    '''

def p_termino(p):
    '''termino : factor factorciclo'''

def p_factorciclo(p):
    '''factorciclo : MULT termino
    | DIV termino
    | empty
    '''

def p_factor(p):
    '''factor : PARIZQ expresion PARDER
    | masomenos varcte
    | ID opcionid
    '''

def p_masomenos(p):
    '''masomenos : MAS
    | MENOS
    | empty
    '''

def p_opcionid(p):
    '''opcionid : arrexp arrexp
    | PARIZQ parametros PARDER'''

def p_varcte(p):
    '''varcte : iddim
    | CTEI
    | CTEF
    '''

def p_parametros(p):
    '''parametros : expresion cicloparametros
    | empty'''

def p_cicloparametros(p):
    '''cicloparametros : COMA expresion cicloparametros
    | empty
    '''

def p_decision(p):
    '''decision : IF PARIZQ expresion PARDER THEN bloque ELSE bloque'''

def p_escritura(p):
    '''escritura : WRITE PARIZQ escrituraciclo otro PARDER PTOCOM'''

def p_escrituraciclo(p):
    '''escrituraciclo : CTE_STRING
    | expresion'''

def p_otro(p):
    '''otro : COMA escrituraciclo otro
    | empty
    '''

def p_llamadafunc(p):
    '''llamadafunc : ID PARIZQ parametros PARDER PTOCOM'''

def p_lectura(p):
    '''lectura : READ PARIZQ iddim ciclodim PARDER PTOCOM'''

def p_ciclodim(p):
    '''ciclodim : COMA iddim ciclodim
    | empty
    '''

def p_iddim(p):
    '''iddim : ID arrexp arrexp'''

def p_arrexp(p):
    '''arrexp : CORIZQ expresion CORDER
    | empty'''

def p_repeticion(p):
    '''repeticion : condicional 
    | nocondicional
    '''

def p_condicional(p):
    '''condicional : WHILE PARIZQ expresion PARDER DO bloque'''

def p_nocondicional(p):
    '''nocondicional : FOR iddim IGU expresion TO expresion DO bloque
    '''

def p_decisionfunc(p):
    '''decisionfunc : IF PARIZQ expresion PARDER THEN bloquefunc ELSE bloquefunc'''

def p_repeticionfunc(p):
    '''repeticionfunc : condicionalfunc
    | nocondicionalfunc
    '''

def p_condicionalfunc(p):
    '''condicionalfunc : WHILE PARIZQ expresion PARDER DO bloquefunc'''

def p_nocondicionalfunc(p):
    '''nocondicionalfunc : FOR iddim IGU expresion TO expresion DO bloquefunc'''

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p:
         print("Syntax error at token", p.type)
    print("ERROR, el input no cumple con todas las reglas gramaticales")

# * Puntos neurálgicos registro de funciones
def p_r_register_global(p):
    'r_register_global : '
    fun_dict.add_function("global")
    fun_dict.update_curr_function_name(p[-1])

def p_r_register_function(p):
    'r_register_function : '
    fun_dict.add_function(p[-1])

def p_r_update_curr_function_name(p):
    'r_update_curr_function_name : '
    fun_dict.update_curr_function_name(p[-1])

def p_r_register_variables(p):
    'r_register_variables : '
    fun_dict.append_variable_to_curr_function()    

# * Puntos neurálgicos registro de variables

# * Puntos neurálgicos 
    

# Build the parser
parser = yacc.yacc()

with open("test.txt") as f:
    data = f.read()


parser.parse(data)