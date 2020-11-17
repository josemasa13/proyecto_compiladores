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

global_int = 1000
global_float = 4000
local_int = 8000
local_float = 12000
temporal_int = 16000
temporal_float = 19000
temporal_bool = 22000
constant_int = 24000
constant_float = 28000

comp_set = {'>', '<', '==', '&', '|', '>=', '<=', '!='}

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
    | MODULE ID r_update_func_type r_update_curr_function_name PARIZQ r_marcar_funcion opcionvarsimple r_desmarcar_funcion PARDER r_register_param_types opvars r_register_quad bloquefunc r_endfunc'''

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
    '''funcion : tipo_func MODULE ID r_update_curr_function_name PARIZQ r_marcar_funcion opcionvarsimple r_desmarcar_funcion PARDER r_register_param_types opvars r_register_quad bloquefunc r_endfunc'''

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
    '''asignacion : ID r_verifica_variable_existe r_pila_operandos_push_id asignacionarr asignacionarr IGU r_pila_operadores_push_igu  expresion r_pop_igu PTOCOM'''

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
    | ID r_verifica_variable_existe r_guardar_variable opcionid r_pila_operandos_push
    '''

def p_masomenos(p):
    '''masomenos : MAS
    | MENOS
    | empty
    '''

def p_opcionid(p):
    '''opcionid : PARIZQ r_era_funcion parametros r_terminar_parametro PARDER 
    | arrexp arrexp  '''

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
    '''llamadafunc : ID r_verifica_void PARIZQ r_era_funcion parametros r_terminar_parametro_void PARDER PTOCOM'''

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

def p_lectura(p):
    '''lectura : READ PARIZQ iddim ciclodim PARDER PTOCOM'''

def p_ciclodim(p):
    '''ciclodim : COMA iddim ciclodim
    | empty
    '''

def p_iddim(p):
    '''iddim : ID r_verifica_variable_existe r_pila_operandos_push_id arrexp arrexp'''

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


# Counters reset
def reset_counters():
    global local_int
    global local_float
    global temporal_int
    global temporal_float
    global temporal_bool
    global constant_int
    global constant_float

    local_int = 8000
    local_float = 12000
    temporal_int = 16000
    temporal_float = 19000
    temporal_bool = 22000
    constant_int = 24000
    constant_float = 28000

# * Puntos neurálgicos registro de funciones
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

def p_r_update_curr_function_name(p):
    'r_update_curr_function_name : '
    fun_dict.update_curr_function_name(p[-1])
    reset_counters()

def p_r_register_param_types(p):
    'r_register_param_types : '
    fun_dict.curr_function.register_parameters()

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

def p_r_era_funcion(p):
    'r_era_funcion : '
    print("ERA")
    pila_nombre_func.append("Guarda el nombre de la funcion")
    #TAMAÑO JOSEMARCIAL
    global apuntador_argumento
    cuad = Quadruple('ERA',None,None,'funcion')
    cuadruplos.append(cuad)
    if apuntador_argumento > -1:
        pila_apuntador_argumentos.append(apuntador_argumento)
    apuntador_argumento = 0
    if len(tipos_argumentos) > 0:
        pila_tipos_argumentos.append(tipos_argumentos)

def p_r_terminar_parametro(p):
    'r_terminar_parametro : '
    global apuntador_argumento
    global tipos_argumentos
    global temporal_int
    nombrefunc = pila_nombre_func.pop()
    num_quad = fun_dict.search_quad(nombrefunc)
    cuad = Quadruple('GOSUB',None,None,num_quad)
    cuadruplos.append(cuad)
    cuad = Quadruple('=','funcion',None,temporal_int)
    cuadruplos.append(cuad)
    pila_operandos.append(temporal_int)
    temporal_int += 1
    if apuntador_argumento < len(tipos_argumentos):
        print("Faltaron argumentos a la llamada de funcion")
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
    cuad = Quadruple('GOSUB',None,None,'funcion')
    cuadruplos.append(cuad)
    if apuntador_argumento < len(tipos_argumentos):
        print("Faltaron argumentos a la llamada de funcion")
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
    if apuntador_argumento < len(tipos_argumentos) and len(tipos_argumentos) > 0 :
        resultado = pila_operandos.pop()
        if tipos_argumentos[apuntador_argumento] == 'int' and ((resultado>=1000 and resultado<=3999) or (resultado>=8000 and resultado<=11999) or (resultado>=16000 and resultado<=18999) or (resultado>=24000 and resultado<=27999) ):
            cuad = Quadruple('parameter',resultado,None,"parameter" + str(apuntador_argumento) )
            cuadruplos.append(cuad)
            apuntador_argumento+=1
        elif tipos_argumentos[apuntador_argumento] == 'float' and ((resultado>=4000 and resultado<=7999) or (resultado>=12000 and resultado<=15999) or  (resultado>=19000 and resultado<=21999) or (resultado>=28000)  ):
            cuad = Quadruple('parameter',resultado,None,"parameter"+str(apuntador_argumento))
            cuadruplos.append(cuad)
            apuntador_argumento+=1
        else:
            print("el tipo de argumento no es del tipo de parametro")
    else:
        print("La funcion no tiene ese numero de parametros")

def p_r_verifica_void(p):
    'r_verifica_void : '
    global tipos_argumentos
    global pila_tipos_argumentos
    tipos_argumentos_defunc = fun_dict.search_existing_name(p[-1])
    if len(tipos_argumentos) > 0:
        pila_tipos_argumentos.append(tipos_argumentos)
    tipos_argumentos = tipos_argumentos_defunc
    if not tipos_argumentos:
        print("la variable no está declarada en ningún contexto " + p[-1])
    pass

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
    global local_int
    global global_float
    global local_float
    temporal_var[1] = p[-1]
    if temporal_var[0] == "int":
        if fun_dict.curr_function.name == "global":
            fun_dict.append_variable_to_curr_function(temporal_var[1], temporal_var[0], global_int)
            global_int += 1
        else:
            fun_dict.append_variable_to_curr_function(temporal_var[1], temporal_var[0], local_int)
            local_int += 1

    elif temporal_var[0] == "float":
        if fun_dict.curr_function.name == "global":
            fun_dict.append_variable_to_curr_function(temporal_var[1], temporal_var[0], global_float)
            global_float += 1

        else:
            fun_dict.append_variable_to_curr_function(temporal_var[1], temporal_var[0], local_float)
            local_float += 1

    else:
        raise Exception("El tipo de dato especificado, no existe " + temporal_var[0])
        

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
                #verifica que sea de tipo return JOSE MARCIAL
                if len(tipos_argumentos) > 0:
                    pila_tipos_argumentos.append(tipos_argumentos)
                tipos_argumentos = tipos_argumentos_defunc
                if not tipos_argumentos:
                    print("la variable no está declarada en ningún contexto " + p[-1])
                    pass

def p_r_return_func(p):
    'r_return_func : '
    #verificar tipo de return sea de tipo de funcion
    result = pila_operandos.pop()
    cuad = Quadruple('RETURN',None, None,result)
    cuadruplos.append(cuad)

def p_r_if_paso_2(p):
    'r_if_paso_2 : '
    cuad = Quadruple('goto',None, None,None)
    cuadruplos.append(cuad)
    salto = pila_saltos.pop()
    pila_saltos.append(len(cuadruplos)-1)
    cuadruplos[salto].modificar_resultado((-1,len(cuadruplos)))

def p_r_if_paso_3(p):
    'r_if_paso_3 : '
    salto = pila_saltos.pop()
    cuadruplos[salto].modificar_resultado((-1,len(cuadruplos)))

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
    cuad = Quadruple('+',constant_int,resultado,temporal_int)
    cuadruplos.append(cuad)
    cuadasignacion = Quadruple('=',temporal_int,None,resultado)
    temporal_int += 1
    constant_int += 1
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
    oper = pila_guardar_variable.pop()
    var = fun_dict.get_variable(oper)
    if var:
        pila_operandos.append(var['virtual_address'])
        pila_tipos.append(var["type"])
    else:
        funcion = fun_dict.search_function(oper)
        if not funcion:
            raise Exception("La variable no existe")

def p_r_pila_operandos_push_id(p):
    'r_pila_operandos_push_id : '
    var = fun_dict.get_variable(p[-2])
    if var:
        pila_operandos.append(var['virtual_address'])
        pila_tipos.append(var["type"])
    else:
        raise Exception("La variable " + p[-2] + " no existe")

def p_r_pila_operandos_push_cte_int(p):
    'r_pila_operandos_push_cte_int : '
    # guardar la constant en la direccion de memoria - Tener en que direcion de memoria la gua
    global constant_int
    pila_operandos.append(constant_int)
    pila_tipos.append('int')
    constant_int += 1
    tabla_temporales.append(('int', p[-1]))

def p_r_pila_operandos_push_cte_flt(p):
    'r_pila_operandos_push_cte_flt : '
    global constant_float
    pila_operandos.append(constant_float)
    pila_tipos.append('float')
    constant_float += 1
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

                elif res_type == 'int':
                    cuad = Quadruple(operator, operando_izq, operando_der,temporal_int)
                    pila_operandos.append(temporal_int)
                    temporal_int += 1

                elif res_type == 'bool':
                    cuad = Quadruple(operator, operando_izq, operando_der,temporal_bool)
                    pila_operandos.append(temporal_bool)
                    temporal_bool += 1


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

                elif res_type == 'int':
                    cuad = Quadruple(operator, operando_izq, operando_der,temporal_int)
                    pila_operandos.append(temporal_int)
                    temporal_int += 1

                elif res_type == 'bool':
                    cuad = Quadruple(operator, operando_izq, operando_der,temporal_bool)
                    pila_operandos.append(temporal_bool)
                    temporal_bool += 1


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

def p_r_pop_comp(p):
    'r_pop_comp : '
    if len(pila_operadores) > 0:
        if(pila_operadores[len(pila_operadores) - 1] in comp_set):
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

                elif res_type == 'int':
                    cuad = Quadruple(operator, operando_izq, operando_der,temporal_int)
                    pila_operandos.append(temporal_int)
                    temporal_int += 1

                elif res_type == 'bool':
                    cuad = Quadruple(operator, operando_izq, operando_der,temporal_bool)
                    pila_operandos.append(temporal_bool)
                    temporal_bool += 1


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

def print_quads():
    for i,cuad in enumerate(cuadruplos):
        print(i, cuad.operador, cuad.operando_izq, cuad.operando_der, cuad.resultado)
    
    # Build the parser
parser = yacc.yacc()

with open("test.txt") as f:
    data = f.read()


parser.parse(data)

fun_dict.print_funcs_params()
print_quads()