import ply.yacc as yacc
from scanner import tokens
from data_structures.functions_directory import FunctionsDirectory
from data_structures.quadruple import Quadruple
from data_structures.semantic_cube import semantic_cube
from data_structures.constant_table import Constanttable
import sys

fun_dict = FunctionsDirectory()
const_table = Constanttable()
tabla_temporales = []
pila_operandos = []
pila_operadores = []
pila_saltos = []
pila_tipos = []
cuadruplos = []
temporal_var = ["", ""]
tipo_funcion = 0
tipo_parametros = []
tipos_argumentos = []
pila_tipos_argumentos = []
pila_apuntador_argumentos = []
apuntador_argumento = -1
pila_guardar_variable = []
pila_nombre_func = []
flag_return = False
flag_dim_uno = False
flag_dim_dos = False
dimension_uno = -1
dimension_dos = -1

global_int = 1000
global_float = 4000
local = 8000
local_int = 8000
local_float = 12000
temporal_int = 16000
temporal_float = 19000
temporal_bool = 22000
constant_int = 24000
constant_float = 28000
constant_string = 32000
pointers = 36000


comp_set = {'>', '<', '==', '&', '|', '>=', '<=', '!='}

# programa
def p_program(p):
    '''program : PRO r_register_gotomain ID r_register_global PTOCOM opvars opfunciones MAIN r_switch_to_global PARIZQ PARDER bloque'''

def p_opvars(p):
    '''opvars : vars
    | empty'''

def p_opfunciones(p):
    '''opfunciones : funciones opfunciones
    | empty'''

def p_vars(p):
    '''vars : VARTOKEN tipo ID r_register_variable_name arr_uno arr_dos r_verify_array varciclo PTOCOM tipociclo'''

def p_varciclo(p):
    '''varciclo : COMA ID r_register_variable_name arr_uno arr_dos r_verify_array varciclo
    | empty'''

def p_arr(p):
    '''arr : CORIZQ CTEI r_register_const CORDER
    | empty'''

def p_arr_uno(p):
    '''arr_uno : CORIZQ CTEI r_register_const r_arr_dim_uno CORDER
    | empty'''

def p_arr_dos(p):
    '''arr_dos : CORIZQ CTEI r_register_const r_arr_dim_dos CORDER
    | empty'''

def p_tipociclo(p):
    '''tipociclo : tipo opciontipo
    | empty'''

def p_opciontipo(p):
    '''opciontipo : ID r_register_variable_name arr_uno arr_dos r_verify_array varciclo PTOCOM tipociclo
    | MODULE ID r_update_func_type r_update_curr_function_name_especial PARIZQ r_marcar_funcion opcionvarsimple r_desmarcar_funcion PARDER r_register_param_types opvars r_register_quad bloquefunc r_endfunc r_asegurar_return'''

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
    '''funcionvoid : VOID r_register_function MODULE ID r_update_curr_function_name PARIZQ r_marcar_funcion opcionvarsimple r_desmarcar_funcion PARDER r_register_param_types opvars r_register_quad bloque  r_endfunc'''

def p_opcionvarsimple(p):
    '''opcionvarsimple : varsimple ciclovarsimple
    | empty'''

def p_ciclovarsimple(p):
    '''ciclovarsimple : COMA varsimple ciclovarsimple
    | empty'''

def p_funcion(p): 
    '''funcion : tipo_func MODULE ID r_update_curr_function_name PARIZQ r_marcar_funcion opcionvarsimple r_desmarcar_funcion PARDER r_register_param_types opvars r_register_quad bloquefunc r_endfunc r_asegurar_return'''

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
    | RETURN PARIZQ expresion r_return_func PARDER PTOCOM
    '''

def p_asignacion(p):
    '''asignacion : ID r_verifica_variable_existe r_guardar_variable arrexp_uno arrexp_dos r_pila_operandos_push_id IGU r_pila_operadores_push_igu  expresion r_pop_igu PTOCOM'''

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
    '''factor : PARIZQ r_marcar_fondo_de_pila expresion r_desmarcar_fondo_de_pila PARDER
    | masomenos varcte
    | ID r_verifica_variable_existe r_guardar_variable opcionid r_pila_operandos_push
    '''

def p_masomenos(p):
    '''masomenos : MAS
    | MENOS
    | empty
    '''

def p_opcionid(p):
    '''opcionid : PARIZQ r_era_funcion_retorno parametros r_terminar_parametro PARDER 
    | arrexp_uno arrexp_dos  '''

def p_arrexp_uno(p):
    '''arrexp_uno : CORIZQ r_push_arr expresion r_verifica_arrexp_uno CORDER
    | empty'''

def p_arrexp_dos(p):
    '''arrexp_dos : CORIZQ  r_push_arr expresion r_verifica_arrexp_dos CORDER
    | empty'''

def p_varcte(p):
    '''varcte : iddim
    | CTEI r_pila_operandos_push_cte_int
    | CTEF r_pila_operandos_push_cte_flt
    '''

def p_parametros(p):
    '''parametros : expresion r_extraer_parametro cicloparametros
    | empty'''

def p_cicloparametros(p):
    '''cicloparametros : COMA expresion r_extraer_parametro cicloparametros
    | empty
    '''

def p_llamadafunc(p):
    '''llamadafunc : ID r_verifica_void PARIZQ r_era_funcion_void parametros r_terminar_parametro_void PARDER PTOCOM'''

def p_decision(p):
    '''decision : IF PARIZQ expresion PARDER r_if_paso_1 THEN bloque decision_else r_if_paso_3'''

def p_decision_else(p):
    '''decision_else : ELSE r_if_paso_2 bloque
    | empty'''

def p_decisionfunc(p):
    '''decisionfunc : IF PARIZQ expresion PARDER r_if_paso_1 THEN bloquefunc decisionfunc_else r_if_paso_3
    '''

def p_decisionfunc_else(p):
    '''decisionfunc_else : ELSE r_if_paso_2 bloquefunc
    | empty'''

def p_condicional(p):
    '''condicional : WHILE r_while_paso_1 PARIZQ expresion PARDER r_while_paso_2 DO bloque r_while_paso_3'''

def p_condicionalfunc(p):
    '''condicionalfunc : WHILE r_while_paso_1 PARIZQ r_while_paso_2 expresion PARDER DO bloquefunc'''

def p_nocondicional(p):
    '''nocondicional : FOR ID r_verifica_variable_existe r_guardar_variable arrexp_uno  arrexp_dos r_pila_operandos_push IGU r_pila_operadores_push_igu expresion TO r_pop_igu_for expresion r_for_paso_1 DO bloque r_for_paso_2
    '''

def p_nocondicionalfunc(p):
    '''nocondicionalfunc : FOR ID r_verifica_variable_existe r_guardar_variable arrexp_uno  arrexp_dos r_pila_operandos_push IGU r_pila_operadores_push_igu expresion TO r_pop_igu_for expresion r_for_paso_1 DO bloquefunc r_for_paso_2'''

def p_escritura(p):
    '''escritura : WRITE PARIZQ escrituraciclo otro PARDER PTOCOM'''

def p_lectura(p):
    '''lectura : READ PARIZQ ID r_verifica_variable_existe r_guardar_variable arrexp_uno  arrexp_dos r_pila_operandos_push  r_genera_lectura ciclodim PARDER PTOCOM'''

def p_escrituraciclo(p):
    '''escrituraciclo : CTE_STRING r_genera_escribe_string
    | expresion r_genera_escribe'''

def p_otro(p):
    '''otro : COMA escrituraciclo otro
    | empty
    '''

def p_repeticion(p):
    '''repeticion : condicional 
    | nocondicional
    '''

def p_repeticionfunc(p):
    '''repeticionfunc : condicionalfunc
    | nocondicionalfunc
    '''

def p_empty(p):
    'empty :'
    pass

def p_ciclodim(p):
    '''ciclodim : COMA iddim r_genera_lectura ciclodim
    | empty
    '''

def p_iddim(p):
    '''iddim : ID r_verifica_variable_existe r_pila_operandos_push_id arrexp arrexp'''

def p_arrexp(p):
    '''arrexp : CORIZQ expresion CORDER
    | empty'''

def p_error(p):
    if p:
         print("Syntax error at token", p.type)
    print("ERROR, el input no cumple con todas las reglas gramaticales")


# Counters reset
def reset_counters():
    global local
    global temporal_int
    global temporal_float
    global temporal_bool


    local = 8000
    temporal_int = 16000
    temporal_float = 19000
    temporal_bool = 22000

# * Puntos neurálgicos registro de funciones
def p_r_register_gotomain(p):
    'r_register_gotomain : '
    cuad = Quadruple('goto',None,None,None)
    cuadruplos.append(cuad)
    pila_saltos.append(len(cuadruplos) - 1)

def p_r_register_global(p):
    'r_register_global : '
    fun_dict.add_function("global")
    fun_dict.update_curr_function_name("global")

def p_r_register_function(p):
    'r_register_function : '
    exists = fun_dict.search_function(p[-1])
    if exists:
        raise Exception("La función que intentas declarar ya existe " + p[-1])
    fun_dict.add_function(p[-1])

def p_r_register_const(p):
    'r_register_const : '
    global constant_int
    insertion = const_table.insert_constant(p[-1], 'int', constant_int)
    if insertion == constant_int:
        constant_int += 1


def p_r_switch_to_global(p):
    'r_switch_to_global : '
    fun_dict.curr_function = fun_dict.directory[0]
    salto = pila_saltos.pop()
    cuadruplos[salto].modificar_resultado(len(cuadruplos))


def p_r_update_curr_function_name_especial(p):
    'r_update_curr_function_name_especial : '
    fun_dict.update_curr_function_name(p[-2])
    reset_counters()

def p_r_update_curr_function_name(p):
    'r_update_curr_function_name : '
    fun_dict.update_curr_function_name(p[-1])
    reset_counters()

def p_r_register_param_types(p):
    'r_register_param_types : '
    
    curr_func = fun_dict.curr_function
    global global_float
    global global_int
    
    if curr_func.type == "float":
        fun_dict.add_function_to_global(curr_func.name + "_func", curr_func.type, global_float)
        global_float += 1

    elif curr_func.type == "int":
        fun_dict.add_function_to_global(curr_func.name + "_func", curr_func.type, global_int)
        global_int += 1
    
        

def p_r_register_variable_type(p):
    'r_register_variable_type : '
    if tipo_funcion == 1:
        tipo_parametros.append(p[-1])
    temporal_var[0] = p[-1]

def p_r_update_func_type(p):
    'r_update_func_type : '
    fun_dict.add_function(temporal_var[0])

def p_r_register_quad(p):
    'r_register_quad : '
    fun_dict.add_quadruple(len(cuadruplos))

def p_r_era_funcion_void(p):
    'r_era_funcion_void : '
    # guardar nombre de la función llamada
    pila_operadores.append("FUNC")
    nombre_func = p[-3]
    pila_nombre_func.append(nombre_func)
    func = fun_dict.search_function(nombre_func)

    if func:
        if func.type == "void":
            global apuntador_argumento
            cuad = Quadruple('era',None,None,nombre_func)
            cuadruplos.append(cuad)
            if apuntador_argumento > -1:
                pila_apuntador_argumentos.append(apuntador_argumento)
                #pila_tipos_argumentos.append(tipos_argumentos)
            if len(tipos_argumentos)> 0:
                apuntador_argumento = 0
        else:
            raise Exception("La función " + nombre_func + " tiene tipo de retorno")

    else:
        raise Exception("La función " + nombre_func + " no ha sido declarada")

def p_r_era_funcion_retorno(p):
    'r_era_funcion_retorno : '
    # guardar nombre de la función llamada
    pila_operadores.append("FUNC")
    nombre_func = pila_guardar_variable[-1]
    pila_nombre_func.append(nombre_func)
    func = fun_dict.search_function(nombre_func)
    if func:
        if func.type != "void":
            global apuntador_argumento
            cuad = Quadruple('era',None,None,nombre_func)
            cuadruplos.append(cuad)
            if apuntador_argumento > -1:
                pila_apuntador_argumentos.append(apuntador_argumento)
            if len(tipos_argumentos)> 0:
                apuntador_argumento = 0
        else:
            raise Exception("La función " + nombre_func + " es de tipo void")

    else:
        raise Exception("La función " + nombre_func + " no ha sido declarada")

def p_r_asegurar_return(p):
    'r_asegurar_return : '
    global flag_return
    if flag_return == False:
        raise Exception("No se regresó ningún valor para la función " + fun_dict.curr_function.name)

    else:
        flag_return = False

    pass

def p_r_terminar_parametro(p):
    'r_terminar_parametro : '
    global apuntador_argumento
    global tipos_argumentos
    global temporal_int
    pila_operadores.pop()
    nombrefunc = pila_nombre_func.pop()
    num_quad = fun_dict.search_quad(nombrefunc)
    cuad = Quadruple('gosub',None,None,num_quad)
    cuadruplos.append(cuad)
    if apuntador_argumento != -1:
        if apuntador_argumento < len(tipos_argumentos):
            raise Exception("Faltan argumentos en la llamada a la función")
        else:
            if len(pila_apuntador_argumentos) > 0:
                apuntador_argumento = pila_apuntador_argumentos.pop()
            else:
                apuntador_argumento = -1
            if len(pila_tipos_argumentos) > 0:
                tipos_argumentos = pila_tipos_argumentos.pop()
            else:
                tipos_argumentos = []

def p_r_terminar_parametro_void(p):
    'r_terminar_parametro_void : '
    global apuntador_argumento
    global tipos_argumentos
    global temporal_int
    pila_operadores.pop()
    nombrefunc = pila_nombre_func.pop()
    num_quad = fun_dict.search_quad(nombrefunc)
    cuad = Quadruple('gosub',None,None,num_quad)
    cuadruplos.append(cuad)
    if apuntador_argumento != -1:
        if apuntador_argumento < len(tipos_argumentos):
            raise Exception("Faltaron argumentos a la llamada de funcion")
        else:
            if len(pila_apuntador_argumentos) > 0:
                apuntador_argumento = pila_apuntador_argumentos.pop()
            else:
                apuntador_argumento = -1
            if len(pila_tipos_argumentos) > 0:
                tipos_argumentos = pila_tipos_argumentos.pop()
            else:
                tipos_argumentos = []

def p_r_extraer_parametro(p):
    'r_extraer_parametro : '
    global apuntador_argumento
    print(apuntador_argumento)
    print(tipos_argumentos)
    if apuntador_argumento < len(tipos_argumentos) and len(tipos_argumentos) > 0 :
        resultado = pila_operandos.pop()
        if tipos_argumentos[apuntador_argumento] == 'int':
            cuad = Quadruple('parameter',resultado,None,"parameter" + str(apuntador_argumento) )
            cuadruplos.append(cuad)
            apuntador_argumento+=1
        elif tipos_argumentos[apuntador_argumento] == 'float':
            cuad = Quadruple('parameter',resultado,None,"parameter"+str(apuntador_argumento))
            cuadruplos.append(cuad)
            apuntador_argumento+=1
        else:
            raise Exception("el tipo de argumento no es del tipo del parametro")
    else:
        raise Exception("La funcion no tiene ese numero de parametros")

def p_r_verifica_void(p):
    'r_verifica_void : '
    global tipos_argumentos
    global pila_tipos_argumentos
    func = fun_dict.search_function(p[-1])
    if func:
        if func.type == "void":
            tipos_argumentos_defunc = fun_dict.search_existing_name(p[-1])
            if apuntador_argumento >= 0:
                pila_tipos_argumentos.append(tipos_argumentos)
            tipos_argumentos = tipos_argumentos_defunc
            if tipos_argumentos == -1:
                raise Exception("la variable no está declarada en ningún contexto " + p[-1])
                print("la variable no está declarada en ningún contexto " + p[-1])
            pass

        else:
            raise Exception("La función llamada no es de tipo void")

def p_r_marcar_funcion(p):
    'r_marcar_funcion : '
    global tipo_funcion
    tipo_funcion = 1

def p_r_desmarcar_funcion(p):
    'r_desmarcar_funcion : '
    global tipo_funcion
    global tipo_parametros
    tipo_funcion = 0
    e = fun_dict.add_typesofparameter(tipo_parametros)
    tipo_parametros = []


def p_r_endfunc(p):
    'r_endfunc : '
    cuad = Quadruple('endfunc',None,None,None)
    cuadruplos.append(cuad)
    #guardar el tamaño se lo que funcion size.append([lo que uso ])

def p_r_if_paso_1(p):
    'r_if_paso_1 : '
    #preguntar el tipo si el operando es boolano
    result = pila_operandos.pop()
    cuad = Quadruple('gotof', result, None,None)
    cuadruplos.append(cuad)
    pila_saltos.append(len(cuadruplos)-1)

def p_r_register_variable_name(p):
    'r_register_variable_name : '
    global global_int
    global local
    global global_float
    temporal_var[1] = p[-1]
    if temporal_var[0] == "int":
        if fun_dict.curr_function.name == "global":
            fun_dict.append_variable_to_curr_function(temporal_var[1], temporal_var[0], global_int)
            global_int += 1
        else:
            fun_dict.append_variable_to_curr_function(temporal_var[1], temporal_var[0], local)
            local += 1

        fun_dict.curr_function.int_spaces += 1


    elif temporal_var[0] == "float":
        if fun_dict.curr_function.name == "global":
            fun_dict.append_variable_to_curr_function(temporal_var[1], temporal_var[0], global_float)
            global_float += 1

        else:
            fun_dict.append_variable_to_curr_function(temporal_var[1], temporal_var[0], local)
            local += 1

        fun_dict.curr_function.float_spaces += 1


    else:
        raise Exception("El tipo de dato especificado, no existe " + temporal_var[0])
        
def p_r_arr_dim_uno(p):
    'r_arr_dim_uno : '
    global dimension_uno
    global flag_dim_uno
    dimension_uno = p[-2]
    if dimension_uno == 0:
        raise Exception("La dimension de la variable " + temporal_var[1]+ " no puede ser 0")
    flag_dim_uno = True

def p_r_arr_dim_dos(p):
    'r_arr_dim_dos : '
    global dimension_dos
    global flag_dim_dos
    dimension_dos = p[-2]
    if dimension_dos == 0:
        raise Exception("La dimension de la variable " + temporal_var[1]+ " no puede ser 0")
    flag_dim_dos = True

def p_r_verify_array(p):
    'r_verify_array : '
    global global_int
    global local
    global global_float
    global flag_dim_uno
    global flag_dim_dos
    if  flag_dim_uno == True and flag_dim_dos == True:
        fun_dict.add_dim_two(temporal_var[1],dimension_uno,dimension_dos)
        espacios = dimension_uno * dimension_dos
        if temporal_var[0] == "int":
            if fun_dict.curr_function.name == "global":
                global_int += espacios - 1
            else:
                local +=  espacios - 1
            fun_dict.curr_function.int_spaces += espacios - 1
        elif temporal_var[0] == "float":
            if fun_dict.curr_function.name == "global":
                global_float += espacios - 1
            else:
                local += espacios - 1
            fun_dict.curr_function.float_spaces += espacios - 1
    elif  flag_dim_uno == True and flag_dim_dos == False:
        fun_dict.add_dim_one(temporal_var[1],dimension_uno)
        espacios = dimension_uno
        if temporal_var[0] == "int":
            if fun_dict.curr_function.name == "global":
                global_int += espacios - 1
            else:
                local +=  espacios - 1
            fun_dict.curr_function.int_spaces += espacios - 1
        elif temporal_var[0] == "float":
            if fun_dict.curr_function.name == "global":
                global_float += espacios - 1
            else:
                local += espacios - 1
            fun_dict.curr_function.float_spaces += espacios - 1
    flag_dim_uno = False
    flag_dim_dos = False

def p_r_verifica_variable_existe(p):
    'r_verifica_variable_existe : '
    global tipos_argumentos
    global pila_tipos_argumentos
    var, e = fun_dict.curr_function.vars.search(p[-1])
    if not var:
        # search in global
        func = fun_dict.search_function("global")
        if func:
            var, e = func.vars.search(p[-1])
            if not var:
                tipos_argumentos_defunc = fun_dict.search_existing_name(p[-1])
                if apuntador_argumento >= 0:
                    pila_tipos_argumentos.append(tipos_argumentos)
                tipos_argumentos = tipos_argumentos_defunc
                if tipos_argumentos == -1:
                    raise Exception("la variable no está declarada en ningún contexto " + p[-1])
                    pass

def p_r_verifica_arrexp_uno(p):
    'r_verifica_arrexp_uno : '
    global pointers
    global temporal_int
    global constant_int
    name_var = pila_guardar_variable.pop()
    var = fun_dict.get_variable(name_var)

    pila_operadores.pop()
    if var["dim_uno"] == None:
        raise Exception("La variable " + name_var + " no es un arreglo")
    elif ("dim_uno" in var and var["dim_uno"] != None) and ("dim_dos" in var and var["dim_dos"] == None):
        index = pila_operandos.pop()
        tipo_var = pila_tipos.pop()
        if tipo_var != "int":
            raise Exception("La expresion tiene que ser de tipo entero")
        
        l_limit = const_table.insert_constant(0, "int", constant_int)
        if l_limit == constant_int:
            constant_int += 1

        u_limit = const_table.insert_constant(var["dim_uno"], "int", constant_int)
        if u_limit == constant_int:
            constant_int += 1

        quad =  Quadruple('ver',index,l_limit,u_limit)

        cuadruplos.append(quad)
        quad =  Quadruple('+_',index,var["virtual_address"],pointers)
        cuadruplos.append(quad)
        pila_tipos.append(var["type"])
        pila_operandos.append(pointers)
        pila_guardar_variable.append("tipo arreglo")
        pointers+=1
    elif ("dim_uno" in var and var["dim_uno"] != None) and ("dim_dos" in var and var["dim_dos"] != None):
        pila_guardar_variable.append(name_var)
        pila_guardar_variable.append("tipo matriz")
        
        index = pila_operandos.pop()
        tipo_var = pila_tipos.pop()
        if tipo_var != "int":
            raise Exception("La expresion tiene que ser de tipo entero")

        l_limit = const_table.insert_constant(0, "int", constant_int)
        if l_limit == constant_int:
            constant_int += 1

        u_limit = const_table.insert_constant(var["dim_uno"], "int", constant_int)
        if u_limit == constant_int:
            constant_int += 1

        quad =  Quadruple('ver',index,l_limit,u_limit)
        cuadruplos.append(quad)
        quad =  Quadruple('*',index,u_limit,temporal_int)
        cuadruplos.append(quad)
        pila_tipos.append("int")
        pila_operandos.append(temporal_int)
        temporal_int+=1

def p_r_verifica_arrexp_dos(p):
    'r_verifica_arrexp_dos : '
    global pointers
    global temporal_int
    global constant_int
    pila_operadores.pop()
    verifica = pila_guardar_variable.pop()
    name_var = pila_guardar_variable.pop()
    var = fun_dict.get_variable(name_var)
    if (verifica == "tipo arreglo"):
        raise Exception("La variable  no es una matriz")
    if ("dim_uno" in var and var["dim_uno"] != None) and ("dim_dos" in var and var["dim_dos"] != None):
        pila_guardar_variable.append("tipo arreglo")
        index = pila_operandos.pop()
        tipo_var = pila_tipos.pop()
        if tipo_var != "int":
            raise Exception("La expresion tiene que ser de tipo entero")

        l_limit = const_table.insert_constant(0, "int", constant_int)
        if l_limit == constant_int:
            constant_int += 1

        u_limit = const_table.insert_constant(var["dim_dos"], "int", constant_int)
        if u_limit == constant_int:
            constant_int += 1

        quad =  Quadruple('ver',index,l_limit,u_limit)
        cuadruplos.append(quad)
        temporal_index = pila_operandos.pop()
        pila_tipos.pop()
        quad =  Quadruple('+',temporal_index,index,temporal_int)
        cuadruplos.append(quad)
        quad =  Quadruple('+_',temporal_int,var["virtual_address"],pointers)
        cuadruplos.append(quad)
        temporal_int+=1
        pila_tipos.append(var["type"])
        pila_operandos.append(pointers)
        print(pointers)
        pointers+=1


def p_r_return_func(p):
    'r_return_func : '
    global flag_return
    flag_return = True
    result = pila_operandos.pop()
    print("res",result)
    tipo = pila_tipos.pop()
    if tipo == fun_dict.curr_function.type:
        space = fun_dict.search_global(fun_dict.curr_function.name + '_func')["virtual_address"]
        cuad = Quadruple('return',space, None,result)
        cuadruplos.append(cuad)

    else:
        curr_func = fun_dict.curr_function
        raise Exception("Error, la función " + curr_func.name + " es de tipo " + curr_func.type + " y el retorno de tipo " + tipo)

def p_r_if_paso_2(p):
    'r_if_paso_2 : '
    cuad = Quadruple('goto',None, None,None)
    cuadruplos.append(cuad)
    salto = pila_saltos.pop()
    pila_saltos.append(len(cuadruplos)-1)
    cuadruplos[salto].modificar_resultado(len(cuadruplos))

def p_r_if_paso_3(p):
    'r_if_paso_3 : '
    salto = pila_saltos.pop()
    cuadruplos[salto].modificar_resultado(len(cuadruplos))

def p_r_while_paso_1(p):
    'r_while_paso_1 : '
    pila_saltos.append(len(cuadruplos))

def p_r_while_paso_2(p):
    'r_while_paso_2 : '
    #preguntar el tipo si el operando es boolano
    resultado = pila_operandos.pop()
    cuad = Quadruple('gotof', resultado, None,None)
    pila_saltos.append(len(cuadruplos))
    cuadruplos.append(cuad)

def p_r_while_paso_3(p):
    'r_while_paso_3 : '
    #preguntar el tipo si el operando es boolano
    salto_al_final = pila_saltos.pop()
    salto_al_regreso = pila_saltos.pop()
    cuad = Quadruple('goto', None, None,salto_al_regreso)
    cuadruplos.append(cuad)
    cuadruplos[salto_al_final].modificar_resultado(len(cuadruplos))

def p_r_pop_igu_for(p):
    'r_pop_igu_for : '
    operando_der = pila_operandos.pop()
    operando_izq = pila_operandos.pop()
    tipo_der = pila_tipos.pop()
    tipo_izq = pila_tipos.pop()
    operator = pila_operadores.pop()
    res_type = semantic_cube[tipo_izq][tipo_der][operator]
    if tipo_der == "int" and tipo_izq == "int":
        cuad = Quadruple(operator,operando_der,None ,operando_izq)
        #verifica que el tipo se tal (ESTE TIPO,-1)
        #verifica que sea del tipo igual a
        pila_operandos.append(operando_izq)
        pila_tipos.append('int')
        cuadruplos.append(cuad)

    else:
        raise Exception("Los dos operandos deben ser enteros")

def p_r_for_paso_1(p):
    'r_for_paso_1 : '
    global temporal_bool
    valor_limite = pila_operandos.pop()
    valor_de_comp = pila_operandos.pop()
    #verificar que valor limite sea int
    pila_saltos.append(len(cuadruplos))
    cuad = Quadruple('<',valor_de_comp,valor_limite,temporal_bool)
    pila_operandos.append(valor_de_comp)
    pila_tipos.append('int')      
    #pila_operandos.append((0,len(tabla_temporales)))
    #tabla_temporales.append((-1,-1))
    cuadruplos.append(cuad)
    #guardar salto del gotof
    pila_saltos.append(len(cuadruplos))
    #resultado_gotof = pila_operandos.pop()
    cuad2 = Quadruple('gotof',temporal_bool,None,None)
    temporal_bool += 1
    cuadruplos.append(cuad2)

def p_r_for_paso_2(p):
    'r_for_paso_2 : '
    resultado = pila_operandos.pop()
    #guardar constante 1
    global constant_int
    global temporal_int
    insertion = const_table.insert_constant(1, 'int', constant_int)
    if insertion != constant_int:
        cuad = Quadruple('+',insertion,resultado,temporal_int)

    else:
        cuad = Quadruple('+',constant_int,resultado,temporal_int)
        constant_int += 1

    cuadruplos.append(cuad)
    cuadasignacion = Quadruple('=',temporal_int,None,resultado)
    temporal_int += 1
    cuadruplos.append(cuadasignacion)
    gotof = pila_saltos.pop()
    retorno = pila_saltos.pop()
    cuadgoto = Quadruple('goto',None,None,retorno)
    cuadruplos.append(cuadgoto)
    cuadruplos[gotof].modificar_resultado(len(cuadruplos))

def p_r_guardar_variable(p):
    'r_guardar_variable : '
    pila_guardar_variable.append(p[-2])

def p_r_pila_operandos_push(p):
    'r_pila_operandos_push : '
    global temporal_float
    global temporal_int

    oper = pila_guardar_variable.pop()

    if oper != "tipo matriz":
        if oper != "tipo arreglo":
            var = fun_dict.get_variable(oper)
            if var:
                pila_operandos.append(var['virtual_address'])
                pila_tipos.append(var["type"])
            else:
                funcion = fun_dict.search_function(oper)
                if not funcion:
                    raise Exception("El identificador " + oper + " no existe")

                else:
                    return_type = funcion.type
                    if return_type == "float":
                        new_quad = Quadruple('=', oper, None, temporal_float)
                        pila_operandos.append(temporal_float)
                        pila_tipos.append("float")
                        temporal_float += 1

                    else:
                        func = fun_dict.search_global(oper + "_func")
                        new_quad = Quadruple('=', func["virtual_address"], None, temporal_int)
                        pila_operandos.append(temporal_int)
                        pila_tipos.append("int")
                        temporal_int += 1

                    cuadruplos.append(new_quad)
    else:
        raise Exception("La variable debe ser matriz")
            

def p_r_pila_operandos_push_id(p):
    'r_pila_operandos_push_id : '
    oper = pila_guardar_variable.pop()
    if oper != "tipo matriz":
        if oper != "tipo arreglo":
            var = fun_dict.get_variable(oper)
            if var:
                pila_operandos.append(var['virtual_address'])
                pila_tipos.append(var["type"])
            else:
                raise Exception("La variable " + p[-2] + " no existe")
    else:
        raise Exception("La variable debe ser matriz")

def p_r_pila_operandos_push_cte_int(p):
    'r_pila_operandos_push_cte_int : '
    # guardar la constant en la direccion de memoria - Tener en que direcion de memoria la gua
    global constant_int
    insertion = const_table.insert_constant(p[-1], 'int', constant_int)
    if insertion != constant_int:
        pila_operandos.append(insertion)

    else:
        pila_operandos.append(constant_int)
        constant_int += 1

    pila_tipos.append('int')
    tabla_temporales.append(('int', p[-1]))

def p_r_pila_operandos_push_cte_flt(p):
    'r_pila_operandos_push_cte_flt : '
    global constant_float
    pila_operandos.append(constant_float)
    insertion = const_table.insert_constant(p[-1], 'float', constant_float)
    if insertion != constant_float:
        pila_operandos.append(insertion)

    else:
        pila_operandos.append(constant_float)
        constant_float += 1

    pila_tipos.append('float')
    tabla_temporales.append(('float', p[-1]))

def p_r_pop_mult(p):
    'r_pop_mult : '
    if len(pila_operadores) > 0:
        if(pila_operadores[len(pila_operadores) - 1] == '*' or pila_operadores[len(pila_operadores) - 1] == '/'):
            operando_der = pila_operandos.pop()
            operando_izq = pila_operandos.pop()
            tipo_der = pila_tipos.pop()
            tipo_izq = pila_tipos.pop()
            operator = pila_operadores.pop()
            res_type = semantic_cube[tipo_izq][tipo_der][operator]

            if res_type != "Error":
                global temporal_float
                global temporal_int
                global temporal_bool
                
                #verifica que el tipo se tal (ESTE TIPO,-1)
                if res_type == 'float':
                    cuad = Quadruple(operator, operando_izq, operando_der,temporal_float)
                    pila_operandos.append(temporal_float)
                    temporal_float += 1
                    fun_dict.curr_function.temporal_float_spaces += 1

                elif res_type == 'int':
                    cuad = Quadruple(operator, operando_izq, operando_der,temporal_int)
                    pila_operandos.append(temporal_int)
                    temporal_int += 1
                    fun_dict.curr_function.temporal_int_spaces += 1

                elif res_type == 'bool':
                    cuad = Quadruple(operator, operando_izq, operando_der,temporal_bool)
                    pila_operandos.append(temporal_bool)
                    temporal_bool += 1
                    fun_dict.curr_function.temporal_bool_spaces += 1


                pila_tipos.append(res_type)
                tabla_temporales.append((-1,-1))
                cuadruplos.append(cuad)

            else:
                raise Exception("La combinación de tipos no es compatible " + tipo_izq + ' ' + operator + ' ' + tipo_der)

def p_r_pop_mas(p):
    'r_pop_mas : '
    if len(pila_operadores) > 0:
        if(pila_operadores[len(pila_operadores) - 1] == '+' or pila_operadores[len(pila_operadores) - 1] == '-'):
            operando_der = pila_operandos.pop()
            operando_izq = pila_operandos.pop()
            tipo_der = pila_tipos.pop()
            tipo_izq = pila_tipos.pop()
            operator = pila_operadores.pop()
            res_type = semantic_cube[tipo_izq][tipo_der][operator]

            if res_type != "Error":
                global temporal_float
                global temporal_int
                global temporal_bool
                
                #verifica que el tipo se tal (ESTE TIPO,-1)
                if res_type == 'float':
                    cuad = Quadruple(operator, operando_izq, operando_der,temporal_float)
                    pila_operandos.append(temporal_float)
                    temporal_float += 1
                    fun_dict.curr_function.temporal_float_spaces += 1


                elif res_type == 'int':
                    cuad = Quadruple(operator, operando_izq, operando_der,temporal_int)
                    pila_operandos.append(temporal_int)
                    temporal_int += 1
                    fun_dict.curr_function.temporal_int_spaces += 1

                elif res_type == 'bool':
                    cuad = Quadruple(operator, operando_izq, operando_der,temporal_bool)
                    pila_operandos.append(temporal_bool)
                    temporal_bool += 1
                    fun_dict.curr_function.temporal_bool_spaces += 1


                pila_tipos.append(res_type)
                tabla_temporales.append((-1,-1))
                cuadruplos.append(cuad)

            else:
                raise Exception("La combinación de tipos no es compatible " + tipo_izq + ' ' + operator + ' ' + tipo_der)
def get_type(tupla):
    # Temporal
    if tupla[0] == 0:
        return tabla_temporales[tupla[1]]

    else:
        return fun_dict.curr_function.vars[tupla[1]]

def p_r_push_arr(p):
    'r_push_arr : '
    pila_operadores.append("arreglo")

def p_r_genera_escribe(p):
    'r_genera_escribe : '
    cuad = Quadruple("write", None, None, pila_operandos.pop())
    pila_tipos.pop()
    cuadruplos.append(cuad)

def p_r_genera_lectura(p):
    'r_genera_lectura : '
    cuad = Quadruple("read", None, None, pila_operandos.pop())
    pila_tipos.pop()
    cuadruplos.append(cuad)


def p_r_genera_escribe_string(p):
    'r_genera_escribe_string : '
    global constant_string

    insertion = const_table.insert_constant(p[-1], 'string',constant_string)
    
    if insertion != constant_string:
        cuad = Quadruple("write", None, None, insertion)

    else:
        cuad = Quadruple("write", None, None, constant_string)
        constant_string += 1

    cuadruplos.append(cuad)

def p_r_pop_comp(p):
    'r_pop_comp : '
    if len(pila_operadores) > 0:
        if(pila_operadores[len(pila_operadores) - 1] in comp_set):
            operando_der = pila_operandos.pop()
            operando_izq = pila_operandos.pop()
            tipo_der = pila_tipos.pop()
            tipo_izq = pila_tipos.pop()
            operator = pila_operadores.pop()
            print(operator)
            print(tipo_izq)
            print(tipo_der)
            res_type = semantic_cube[tipo_izq][tipo_der][operator]
            print(res_type)
            if res_type != "Error":
                global temporal_float
                global temporal_int
                global temporal_bool
                
                #verifica que el tipo se tal (ESTE TIPO,-1)
                if res_type == 'float':
                    cuad = Quadruple(operator, operando_izq, operando_der,temporal_float)
                    pila_operandos.append(temporal_float)
                    temporal_float += 1
                    fun_dict.curr_function.temporal_float_spaces += 1

                elif res_type == 'int':
                    cuad = Quadruple(operator, operando_izq, operando_der,temporal_int)
                    pila_operandos.append(temporal_int)
                    temporal_int += 1
                    fun_dict.curr_function.temporal_int_spaces += 1

                elif res_type == 'bool':
                    cuad = Quadruple(operator, operando_izq, operando_der,temporal_bool)
                    pila_operandos.append(temporal_bool)
                    temporal_bool += 1
                    fun_dict.curr_function.temporal_bool_spaces += 1


                pila_tipos.append(res_type)
                tabla_temporales.append((-1,-1))
                cuadruplos.append(cuad)

            else:
                raise Exception("La combinación de tipos no es compatible " + tipo_izq + ' ' + operator + ' ' + tipo_der)


def p_r_pop_igu(p):
    'r_pop_igu : '
    if len(pila_operadores) > 0:
        if(pila_operadores[len(pila_operadores) - 1] == '='):
            operando_der = pila_operandos.pop()
            operando_izq = pila_operandos.pop()
            tipo_der = pila_tipos.pop()
            tipo_izq = pila_tipos.pop()
            operator = pila_operadores.pop()
            res_type = semantic_cube[tipo_izq][tipo_der][operator]

            if res_type != "Error":
                cuad = Quadruple(operator, operando_der, None, operando_izq)
                cuadruplos.append(cuad)

            else:
                raise Exception("La combinación de tipos no es compatible " + tipo_izq + ' ' + operator + ' ' + tipo_der)

def p_r_marcar_fondo_de_pila(p):
    'r_marcar_fondo_de_pila : '
    pila_operadores.append("(")

def p_r_desmarcar_fondo_de_pila(p):
    'r_desmarcar_fondo_de_pila : '
    while pila_operadores[-1] != "(":
        if pila_operadores[-1] == "*" or pila_operadores[-1] == "/":
            p_r_pop_mult(-1)
        elif pila_operadores[-1] == "+" or pila_operadores[-1] == "-":
            p_r_pop_mas(-1)
        else:
            p_r_pop_comp(-1)
    pila_operadores.pop()

def p_r_pila_operadores_push_mult(p):
    'r_pila_operadores_push_mult : '
    pila_operadores.append('*')

def p_r_pila_operadores_push_div(p):
    'r_pila_operadores_push_div : '
    pila_operadores.append('/')

def p_r_pila_operadores_push_mas(p):
    'r_pila_operadores_push_mas : '
    pila_operadores.append('+')

def p_r_pila_operadores_push_menos(p):
    'r_pila_operadores_push_menos : '
    pila_operadores.append('-')

def p_r_pila_operadores_push_may(p):
    'r_pila_operadores_push_may : '
    pila_operadores.append('>')

def p_r_pila_operadores_push_men(p):
    'r_pila_operadores_push_men : '
    pila_operadores.append('<')

def p_r_pila_operadores_push_dif(p):
    'r_pila_operadores_push_dif : '
    pila_operadores.append('!=')

def p_r_pila_operadores_push_iguigu(p):
    'r_pila_operadores_push_iguigu : '
    pila_operadores.append("==")

def p_r_pila_operadores_push_and(p):
    'r_pila_operadores_push_and : '
    pila_operadores.append('&')

def p_r_pila_operadores_push_or(p):
    'r_pila_operadores_push_or : '
    pila_operadores.append('|')

def p_r_pila_operadores_push_igu(p):
    'r_pila_operadores_push_igu : '
    pila_operadores.append('=')

def p_r_pila_operadores_push_mayigu(p):
    'r_pila_operadores_push_mayigu : '
    pila_operadores.append('>=')

def p_r_pila_operadores_push_menigu(p):
    'r_pila_operadores_push_menigu : '
    pila_operadores.append('<=')

def p_r_push_fondo_falso(p):
    'r_push_fondo_falso : '
    pila_operandos.append("(")
    pila_tipos.append("(")

def p_r_vaciar_fondo_falso(p):
    'r_vaciar_fondo_falso : '
    pass

# Arreglos
def p_r_register_dim(p):
    'r_register_dim : '
    pass



def print_quads():
    for i,cuad in enumerate(cuadruplos):
        print(i, cuad.operador, cuad.operando_izq, cuad.operando_der, cuad.resultado)

 
# Build the parser


def compile():
    try:
        file = open(sys.argv[1], "r")
    except:
        print('File ' + str(sys.argv[1]) + ' not found')
        sys.exit()

    parser = yacc.yacc()
    parser.parse(file.read())
    fun_dict.print_var_tables()
    '''
    fun_dict.print_memory_spaces()
    fun_dict.print_funcs_params()
    print_quads()'''
    const_table.display_table()
    return cuadruplos, const_table


from operaciones import Operations

operations = Operations()

op_list = {
    "goto" :            operations.goto,
    "gotof" :           operations.goto_false,
    "+" :               operations.plus_op,
    "+_" :              operations.plus_op_esp,
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
    'endfunc' :         operations.endfunc,
    'ver':              operations.ver
}


def execute(quads, const_table):
    instruction_pointer = 0
    quadruples = []
    operations.load_constants(const_table)

    while instruction_pointer < len(quads):
        '''if quads[instruction_pointer].operador == "ver":
            print(quads[instruction_pointer].operando_izq, quads[instruction_pointer].operando_der, quads[instruction_pointer].resultado)'''

        if quads[instruction_pointer].operador == "gosub":
            new_quad_number = op_list[quads[instruction_pointer].operador](quads[instruction_pointer], instruction_pointer)
        else:
            new_quad_number = op_list[quads[instruction_pointer].operador](quads[instruction_pointer])
            
        if new_quad_number:
            instruction_pointer = new_quad_number
        else:
            instruction_pointer += 1


def main():
    quads, const_table = compile()
    for i,cuad in enumerate(quads):
        print(i, cuad.operador, cuad.operando_izq, cuad.operando_der, cuad.resultado)

    execute(quads, const_table.table)

    

    

main()
    

