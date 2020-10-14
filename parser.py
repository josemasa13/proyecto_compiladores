import ply.yacc as yacc
from scanner import tokens
from data_structures.functions_directory import FunctionsDirectory

fun_dict = FunctionsDirectory()

# programa
def p_program(p):
    '''program : PRO ID r_register_global PTOCOM opvars opfunciones MAIN PARIZQ PARDER bloque'''
    print("1")

def p_opvars(p):
    '''opvars : vars
    | empty'''
    print("2")


def p_opfunciones(p):
    '''opfunciones : funciones opfunciones
    | empty'''
    print("3")

def p_vars(p):
    # aquí es donde hay ambigüedad
    '''vars : VARTOKEN tipo ID arr arr varciclo PTOCOM tipociclo'''
    #'''vars : VARTOKEN tipo DOSPTS ID arr arr varciclo PTOCOM tipociclo'''
    print("4")

def p_varciclo(p):
    '''varciclo : COMA ID arr arr varciclo
    | empty'''
    print("5")

def p_arr(p):
    '''arr : CORIZQ CTEI CORDER
    | empty'''
    print("6")

def p_tipociclo(p):
    '''tipociclo : tipo opciontipo
    | empty'''
    print("7")

def p_opciontipo(p):
    '''opciontipo : ID arr arr varciclo PTOCOM tipociclo
    | MODULE ID PARIZQ opcionvarsimple PARDER opvars bloquefunc'''

def p_tipo(p):
    '''tipo : INT
    | FLT
    | CHAR'''
    print("8")

def p_varsimple(p):
    '''varsimple : tipo ident'''
    print("9")

def p_funciones(p):
    '''funciones : funcionvoid 
    | funcion'''
    print("10")

def p_funcionvoid(p):
    '''funcionvoid : VOID MODULE ID PARIZQ opcionvarsimple PARDER opvars bloque'''
    print("11")

def p_opcionvarsimple(p):
    '''opcionvarsimple : varsimple ciclovarsimple
    | empty'''
    print("12")

def p_ciclovarsimple(p):
    '''ciclovarsimple : COMA varsimple ciclovarsimple
    | empty'''
    print("13")

def p_funcion(p): 
    '''funcion : tipo MODULE ID PARIZQ opcionvarsimple PARDER opvars bloquefunc'''
    print("14")

def p_ident(p):
    '''ident : ID arrini arrini'''
    print("15")

def p_arrini(p):
    '''arrini : CORIZQ CORDER
    | empty'''
    print("16")

def p_bloque(p):
    '''bloque : KEYIZQ bloqueopcion KEYDER'''
    print("17")

def p_bloqueopcion(p):
    '''bloqueopcion : estatuto bloqueopcion
    | empty'''
    print("18")

def p_bloquefunc(p):
    '''bloquefunc : KEYIZQ bloqueopcionfunc KEYDER'''
    print("19")

def p_bloqueopcionfunc(p):
    '''bloqueopcionfunc : estatutofunc bloqueopcionfunc
    | empty'''
    print("20")

def p_estatuto(p):
    '''estatuto : asignacion
    | decision
    | escritura
    | llamadafunc
    | repeticion
    | lectura'''
    print("21")

def p_estatutofunc(p):
    '''estatutofunc : asignacion
    | decisionfunc
    | escritura
    | llamadafunc
    | repeticionfunc
    | lectura
    | RETURN PARIZQ expresion PARDER PTOCOM
    '''
    print("22")

def p_asignacion(p):
    '''asignacion : ID asignacionarr asignacionarr IGU expresion PTOCOM'''
    print("23")

def p_asignacionarr(p):
    '''asignacionarr : CORIZQ expresion CORDER
    | empty
    '''
    print("24")

def p_expresion(p):
    '''expresion : exp expresionsig'''
    print("25")

def p_expresionsig(p):
    '''expresionsig : MAY expresionsigequal exp
    | MEN expresionsigequal exp
    | DIF exp
    | IGUIGU exp
    | AND exp
    | OR exp
    | empty'''
    print("26")

def p_expresionsigequal(p):
    '''expresionsigequal : IGU
    | empty'''

def p_exp(p):
    '''exp : termino expciclo'''
    print("27")

def p_expciclo(p):
    '''expciclo : MAS exp
    | MENOS exp
    | empty
    '''
    print("28")

def p_termino(p):
    '''termino : factor factorciclo'''
    print("29")

def p_factorciclo(p):
    '''factorciclo : MULT termino
    | DIV termino
    | empty
    '''
    print("30")

def p_factor(p):
    '''factor : PARIZQ expresion PARDER
    | masomenos varcte
    | ID opcionid
    '''
    print("31")

def p_masomenos(p):
    '''masomenos : MAS
    | MENOS
    | empty
    '''
    print("32")

def p_opcionid(p):
    '''opcionid : arrexp arrexp
    | PARIZQ parametros PARDER'''

def p_varcte(p):
    '''varcte : iddim
    | CTEI
    | CTEF
    '''
    print("33")

def p_parametros(p):
    '''parametros : expresion cicloparametros
    | empty'''
    print("34")

def p_cicloparametros(p):
    '''cicloparametros : COMA expresion cicloparametros
    | empty
    '''
    print("35")

def p_decision(p):
    '''decision : IF PARIZQ expresion PARDER THEN bloque ELSE bloque'''
    print("36")

def p_escritura(p):
    '''escritura : WRITE PARIZQ escrituraciclo otro PARDER PTOCOM'''
    print("37")

def p_escrituraciclo(p):
    '''escrituraciclo : CTE_STRING
    | expresion'''
    print("38")

def p_otro(p):
    '''otro : COMA escrituraciclo otro
    | empty
    '''
    print("39")

def p_llamadafunc(p):
    '''llamadafunc : ID PARIZQ parametros PARDER PTOCOM'''
    print("40")

def p_lectura(p):
    '''lectura : READ PARIZQ iddim ciclodim PARDER PTOCOM'''
    print("41")

def p_ciclodim(p):
    '''ciclodim : COMA iddim ciclodim
    | empty
    '''
    print("42")

def p_iddim(p):
    '''iddim : ID arrexp arrexp'''
    print("43")

def p_arrexp(p):
    '''arrexp : CORIZQ expresion CORDER
    | empty'''
    print("44")

def p_repeticion(p):
    '''repeticion : condicional 
    | nocondicional
    '''
    print("45")

def p_condicional(p):
    '''condicional : WHILE PARIZQ expresion PARDER DO bloque'''
    print("46")

def p_nocondicional(p):
    '''nocondicional : FOR iddim IGU expresion TO expresion DO bloque
    '''
    print("47")

def p_decisionfunc(p):
    '''decisionfunc : IF PARIZQ expresion PARDER THEN bloquefunc ELSE bloquefunc'''
    print("48")

def p_repeticionfunc(p):
    '''repeticionfunc : condicionalfunc
    | nocondicionalfunc
    '''
    print("49")

def p_condicionalfunc(p):
    '''condicionalfunc : WHILE PARIZQ expresion PARDER DO bloquefunc'''
    print("50")

def p_nocondicionalfunc(p):
    '''nocondicionalfunc : FOR iddim IGU expresion TO expresion DO bloquefunc'''
    print("51")

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
    

# * Puntos neurálgicos registro de variables

# * Puntos neurálgicos 
    

# Build the parser
parser = yacc.yacc()

with open("test.txt") as f:
    data = f.read()


parser.parse(data)