import ply.yacc as yacc
from scanner import tokens
from data_structures.functions_directory import FunctionsDirectory
from data_structures.quadruple import Quadruple
from data_structures.semantic_cube import semantic_cube

fun_dict = FunctionsDirectory()
tabla_temporales = []
pila_operandos = []
pila_operadores = []
pila_saltos = []
cuadruplos = []
temporal_var = ["", ""]


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
    '''vars : VARTOKEN tipo ID r_register_variable_name arr arr varciclo PTOCOM tipociclo'''

def p_varciclo(p):
    '''varciclo : COMA ID r_register_variable_name arr arr varciclo
    | empty'''

def p_arr(p):
    '''arr : CORIZQ CTEI CORDER
    | empty'''

def p_tipociclo(p):
    '''tipociclo : tipo opciontipo
    | empty'''

def p_opciontipo(p):
    '''opciontipo : ID r_register_variable_name arr arr varciclo PTOCOM tipociclo
    | MODULE ID PARIZQ opcionvarsimple PARDER opvars bloquefunc'''

def p_tipo(p):
    '''tipo : INT r_register_variable_type
    | FLT r_register_variable_type
    | CHAR r_register_variable_type'''

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
    '''ident : ID r_register_variable_name arrini arrini'''

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
    '''asignacion : ID r_verifica_variable_existe r_pila_operandos_push asignacionarr asignacionarr IGU r_pila_operadores_push_igu  expresion r_pop_igu PTOCOM'''

def p_asignacionarr(p):
    '''asignacionarr : CORIZQ expresion CORDER
    | empty
    '''

def p_expresion(p):
    '''expresion : exp r_pop_comp expresionsig'''

def p_expresionsig(p):
    '''expresionsig : MAY r_pila_operadores_push_may expresionsigequal expresion
    | MEN r_pila_operadores_push_men expresionsigequal expresion
    | DIF r_pila_operadores_push_dif expresion
    | IGUIGU r_pila_operadores_push_iguigu expresion
    | AND r_pila_operadores_push_and expresion
    | OR r_pila_operadores_push_or expresion
    | MAYIGU r_pila_operadores_push_mayigu expresionsigequal expresion
    | MENIGU r_pila_operadores_push_menigu expresionsigequal expresion
    | empty'''

def p_expresionsigequal(p):
    '''expresionsigequal : IGU
    | empty'''

def p_exp(p):
    '''exp : termino r_pop_mas  expciclo'''

def p_expciclo(p):
    '''expciclo : MAS r_pila_operadores_push_mas exp
    | MENOS r_pila_operadores_push_menos  exp
    | empty
    '''

def p_termino(p):
    '''termino : factor r_pop_mult factorciclo'''

def p_factorciclo(p):
    '''factorciclo : MULT r_pila_operadores_push_mult termino
    | DIV  r_pila_operadores_push_div termino
    | empty
    '''

def p_factor(p):
    '''factor : PARIZQ expresion PARDER
    | masomenos varcte
    | ID r_verifica_variable_existe r_pila_operandos_push opcionid
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
    | CTEI r_pila_operandos_push_cte_int
    | CTEF r_pila_operandos_push_cte_flt
    '''

def p_parametros(p):
    '''parametros : expresion cicloparametros
    | empty'''

def p_cicloparametros(p):
    '''cicloparametros : COMA expresion cicloparametros
    | empty
    '''

def p_decision(p):
    '''decision : IF PARIZQ expresion PARDER r_if_paso_1 THEN bloque decision_else r_if_paso_3'''

def p_decision_else(p):
    '''decision_else : ELSE r_if_paso_2 bloque
    | empty'''

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
    '''iddim : ID r_verifica_variable_existe r_pila_operandos_push arrexp arrexp'''

def p_arrexp(p):
    '''arrexp : CORIZQ expresion CORDER
    | empty'''

def p_repeticion(p):
    '''repeticion : condicional 
    | nocondicional
    '''

def p_condicional(p):
    '''condicional : WHILE r_while_paso_1 PARIZQ expresion PARDER r_while_paso_2 DO bloque r_while_paso_3'''

def p_nocondicional(p):
    '''nocondicional : FOR iddim IGU r_pila_operadores_push_igu expresion TO r_pop_igu_for expresion r_for_paso_1 DO bloque r_for_paso_2
    '''

def p_decisionfunc(p):
    '''decisionfunc : IF PARIZQ expresion PARDER r_if_paso_1 THEN bloquefunc decisionfunc_else r_if_paso_3
    '''

def p_decisionfunc_else(p):
    '''decisionfunc_else : ELSE r_if_paso_2 bloquefunc
    | empty'''

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
    fun_dict.update_curr_function_name("global")

def p_r_register_function(p):
    'r_register_function : '
    fun_dict.add_function(p[-1])

def p_r_update_curr_function_name(p):
    'r_update_curr_function_name : '
    fun_dict.update_curr_function_name(p[-1])

def p_r_register_variable_type(p):
    'r_register_variable_type : '
    temporal_var[0] = p[-1]

def p_r_register_variable_name(p):
    'r_register_variable_name : '
    temporal_var[1] = p[-1]
    fun_dict.append_variable_to_curr_function(temporal_var[1], temporal_var[0])

def p_r_verifica_variable_existe(p):
    'r_verifica_variable_existe : '
    var, e = fun_dict.curr_function.vars.search(p[-1])

    if not var:
        # search in global
        func = fun_dict.search_function("global")
        if func:
            var, e = func.vars.search(p[-1])

            if not var:
                print("la variable no está declarada en ningún contexto " + p[-1])
                pass

def p_r_if_paso_1(p):
    'r_if_paso_1 : '
    #preguntar el tipo si el operando es boolano
    result = pila_operandos.pop()
    print(result)
    cuad = Quadruple(14, result, (-1,-1),(-1,-1))
    cuadruplos.append(cuad)
    pila_saltos.append(len(cuadruplos)-1)

def p_r_if_paso_2(p):
    'r_if_paso_2 : '
    cuad = Quadruple(13,  (-1,-1), (-1,-1),(-1,-1))
    cuadruplos.append(cuad)
    Salto = pila_saltos.pop()
    pila_saltos.append( len(cuadruplos)-1)
    cuadruplos[Salto].modificar_resultado((-1,len(cuadruplos)))

def p_r_if_paso_3(p):
    'r_if_paso_3 : '
    Salto = pila_saltos.pop()
    cuadruplos[Salto].modificar_resultado((-1,len(cuadruplos)))

def p_r_while_paso_1(p):
    'r_while_paso_1 : '
    pila_saltos.append(len(cuadruplos))

def p_r_while_paso_2(p):
    'r_while_paso_2 : '
    #preguntar el tipo si el operando es boolano
    resultado = pila_operandos.pop()
    cuad = Quadruple(14, resultado, (-1,-1),(-1,-1))
    pila_saltos.append(len(cuadruplos))
    cuadruplos.append(cuad)
    

def p_r_while_paso_3(p):
    'r_while_paso_3 : '
    #preguntar el tipo si el operando es boolano
    salto_al_final = pila_saltos.pop()
    salto_al_regreso = pila_saltos.pop()
    cuad = Quadruple(13, (-1,-1), (-1,-1),(-1,salto_al_regreso))
    cuadruplos.append(cuad)
    cuadruplos[salto_al_final].modificar_resultado(len(cuadruplos))

def p_r_pop_igu_for(p):
    'r_pop_igu_for : '
    tupla_der = pila_operandos.pop()
    tupla_izq = pila_operandos.pop()
    cuad = Quadruple(pila_operadores.pop(),  tupla_der,(-1,-1) ,tupla_izq)
    #verifica que el tipo se tal (ESTE TIPO,-1)
    #verifica que sea del tipo igual a
    pila_operandos.append(tupla_izq)
    cuadruplos.append(cuad)

def p_r_for_paso_1(p):
    'r_for_paso_1 : '
    valor_limite = pila_operandos.pop()
    valor_de_comp = pila_operandos.pop()
    #verificar que valor limite sea int
    pila_saltos.append(len(cuadruplos))
    cuad = Quadruple(2,valor_de_comp,valor_limite,(0,len(tabla_temporales)))
    pila_operandos.append(valor_de_comp)        
    pila_operandos.append((0,len(tabla_temporales)))
    tabla_temporales.append((-1,-1))
    cuadruplos.append(cuad)
    #guardar salto del gotof
    pila_saltos.append(len(cuadruplos))
    resultado_gotof = pila_operandos.pop()
    cuad2 = Quadruple(14,resultado_gotof,(-1,-1),(-1,-1)) 
    cuadruplos.append(cuad2)

def p_r_for_paso_2(p):
    'r_for_paso_2 : '
    resultado = pila_operandos.pop()
    #guardar constante 1
    tabla_temporales.append((2,1))
    cuad = Quadruple(7,(0,len(tabla_temporales)-1),resultado,(0,len(tabla_temporales)))
    tabla_temporales.append((-1,-1))
    cuadruplos.append(cuad)
    cuadasignacion = Quadruple(0,(0,len(tabla_temporales)-1),(-1,-1),resultado)
    cuadruplos.append(cuadasignacion)
    gotof = pila_saltos.pop()
    retorno = pila_saltos.pop()
    cuadgoto = Quadruple(13,(-1,-1),(-1,-1),retorno)
    cuadruplos.append(cuadgoto)
    cuadruplos[gotof].modificar_resultado(len(cuadruplos))

def p_r_pila_operandos_push(p):
    'r_pila_operandos_push : '
    pila_operandos.append((1, fun_dict.get_address(p[-2])))

def p_r_pila_operandos_push_cte_int(p):
    'r_pila_operandos_push_cte_int : '

    //guardar la constant en la direccion de memoria - Tener en que direcion de memoria la gua
    

    pila_operandos.append()
    //tabla_temporales.append(('int', p[-1]))

def p_r_pila_operandos_push_cte_flt(p):
    'r_pila_operandos_push_cte_flt : '
    pila_operandos.append((0,len(tabla_temporales)))
    tabla_temporales.append(('float', p[-1]))

def p_r_pop_mult(p):
    'r_pop_mult : '
    if len(pila_operadores) > 0:
        if(pila_operadores[len(pila_operadores) - 1] == 9 or pila_operadores[len(pila_operadores) - 1] == 10):
            tupla_der = pila_operandos.pop()
            tupla_izq = pila_operandos.pop()
            cuad = Quadruple(pila_operadores.pop(),  tupla_izq, tupla_der,(0,len(tabla_temporales)))
            #verifica que el tipo se tal (ESTE TIPO,-1)
            pila_operandos.append((0,len(tabla_temporales)))
            tabla_temporales.append((-1,-1))
            cuadruplos.append(cuad)

def p_r_pop_mas(p):
    'r_pop_mas : '
    if len(pila_operadores) > 0:
        if(pila_operadores[len(pila_operadores) - 1] == 7 or pila_operadores[len(pila_operadores) - 1] == 8):
            tupla_der = pila_operandos.pop()
            tupla_izq = pila_operandos.pop()

            cuad = Quadruple(pila_operadores.pop(),  tupla_izq, tupla_der,(0,len(tabla_temporales)))
            # verificar que combinación de tipos de tupla_der y tupla_izq, sea posible en el cubo semántico
            # si es posible, hacer consulta al cubo semántico de la mezcla de los tipos y operador 
            #  si no es posible, regreso error

            
            
            pila_operandos.append((0,len(tabla_temporales)))
            # guardar el tipo de los pasos anteriores en la posición 0
            tabla_temporales.append((-1,-1))


            cuadruplos.append(cuad)

def get_type(tupla):
    # Temporal
    if tupla[0] == 0:
        return tabla_temporales[tupla[1]]

    else:
        return fun_dict.curr_function.vars[tupla[1]]

def p_r_pop_comp(p):
    'r_pop_comp : '
    if len(pila_operadores) > 0:
        if(pila_operadores[len(pila_operadores) - 1] <= 6 and pila_operadores[len(pila_operadores) - 1] >= 1):
            tupla_der = pila_operandos.pop()
            tupla_izq = pila_operandos.pop()
            cuad = Quadruple(pila_operadores.pop(),  tupla_izq, tupla_der,(0,len(tabla_temporales)))
            #verifica que el tipo se tal (ESTE TIPO,-1)
            pila_operandos.append((0,len(tabla_temporales)))
            tabla_temporales.append((-1,-1))
            cuadruplos.append(cuad)

def p_r_pop_igu(p):
    'r_pop_igu : '
    if len(pila_operadores) > 0:
        if(pila_operadores[len(pila_operadores) - 1] == 0):
            tupla_der = pila_operandos.pop()
            tupla_izq = pila_operandos.pop()
            cuad = Quadruple(pila_operadores.pop(),  tupla_der,(-1,-1) ,tupla_izq)
            #verifica que el tipo se tal (ESTE TIPO,-1)
            cuadruplos.append(cuad)

    

def p_r_pila_operadores_push_mult(p):
    'r_pila_operadores_push_mult : '
    pila_operadores.append(9)

def p_r_pila_operadores_push_div(p):
    'r_pila_operadores_push_div : '
    pila_operadores.append(10)

def p_r_pila_operadores_push_mas(p):
    'r_pila_operadores_push_mas : '
    pila_operadores.append(7)

def p_r_pila_operadores_push_menos(p):
    'r_pila_operadores_push_menos : '
    pila_operadores.append(8)

def p_r_pila_operadores_push_may(p):
    'r_pila_operadores_push_may : '
    pila_operadores.append(2)

def p_r_pila_operadores_push_men(p):
    'r_pila_operadores_push_men : '
    pila_operadores.append(3)

def p_r_pila_operadores_push_dif(p):
    'r_pila_operadores_push_dif : '
    pila_operadores.append(1)

def p_r_pila_operadores_push_iguigu(p):
    'r_pila_operadores_push_iguigu : '
    pila_operadores.append(4)

def p_r_pila_operadores_push_and(p):
    'r_pila_operadores_push_and : '
    pila_operadores.append(5)

def p_r_pila_operadores_push_or(p):
    'r_pila_operadores_push_or : '
    pila_operadores.append(6)

def p_r_pila_operadores_push_igu(p):
    'r_pila_operadores_push_igu : '
    pila_operadores.append(0)

def p_r_pila_operadores_push_mayigu(p):
    'r_pila_operadores_push_mayigu : '
    pila_operadores.append(18)

def p_r_pila_operadores_push_menigu(p):
    'r_pila_operadores_push_menigu : '
    pila_operadores.append(19)

def print_quads():
    for i,cuad in enumerate(cuadruplos):
        print(i, cuad.operador, cuad.operando_izq, cuad.operando_der, cuad.resultado)
    
    # Build the parser
parser = yacc.yacc()

with open("test.txt") as f:
    data = f.read()


parser.parse(data)

fun_dict.print_var_tables()
#print_quads()