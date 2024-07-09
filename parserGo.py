import ply.yacc as yacc
import logger
from lexer import tokens

#Diccionario de variables
variables = {}

def p_codigo(p):
    '''codigo : lineaCodigo
              | lineaCodigo codigo'''
    
def p_lineaCodigo(p):
    '''lineaCodigo : asignacion
              | sentenciaSwitch
              | funcion
              | funcionSinArg
              | funcionAnonima
              | imprimir
              | mapa
              | array
              | solicitudDatos
              | sentenciaIf
              | slice
              | for
              | expresionAritmetica
              | autooperacion'''

#TIPOS DE FUNCION
def p_funcion(p): #con argumentos o variádica #Carlos Alvia
    'funcion : FUNC ID LPAREN argumentos RPAREN LBRACE subcodigo RBRACE'

def p_argumentos(p): #Carlos Alvia
    '''argumentos : argumento
                  | argumentoVariadico
                  | argumento COMMA argumentos
                  | argumentoVariadico COMMA argumentos'''

def p_argumento(p): #Carlos Alvia
    'argumento : ID tipoDato '

def p_argumentoVariadico(p):
    'argumentoVariadico : ID PUNTO PUNTO PUNTO tipoDato '
    
#FUNCION SIN ARGUMENTOS 
def p_funcionSinArg(p): #funcion sin argumentos Sofia Zarate
    'funcionSinArg : FUNC ID LPAREN RPAREN LBRACE subcodigo RBRACE'

def p_funcion_anonima(p):  #Angello Bravo
    '''funcionAnonima : FUNC LPAREN RPAREN LBRACE subcodigo RBRACE LPAREN RPAREN'''

def p_funcion_anonima_variadico(p): #Angello Bravo
    'funcionAnonima : FUNC LPAREN argumentos RPAREN LBRACE subcodigo RBRACE LPAREN RPAREN'

#ESTRUCTURAS DE CONTROL

def p_subcodigo(p):
     '''subcodigo : lineaSubcodigo
                  | lineaSubcodigo subcodigo'''
     
def p_lineaSubcodigo(p): #Se refiere al código que puede ir en un if, for, switch o una función Carlos Alvia
     '''lineaSubcodigo : asignacionCorta
                  | asignacion
                  | imprimir
                  | solicitudDatos
                  | sentenciaSwitch
                  | funcion
                  | funcionSinArg
                  | funcionAnonima
                  | mapa
                  | array
                  | sentenciaIf
                  | slice
                  | for
                  | expresionAritmetica
                  '''

def p_sentenciaSwitchClasica(p): #Carlos Alvia 
    '''sentenciaSwitch : SWITCH ID LBRACE bloqueCasosSwitch casoDefault RBRACE'''

def p_switchConDefinicionDeVariable(p): #Carlos Alvia 
    'sentenciaSwitch : SWITCH asignacionCorta SEMICOLON ID LBRACE bloqueCasosSwitch casoDefault RBRACE'

def p_switchNoCondicion(p): #Carlos Alvia 
    'sentenciaSwitch : SWITCH LBRACE bloqueCasosBooleanos casoDefault RBRACE'

def p_bloqueCasosBooleanos(p): #Carlos Alvia
    '''bloqueCasosBooleanos : casoBooleano
                            | casoBooleano bloqueCasosBooleanos'''

def p_casoBooleano(p): #Carlos Alvia
    '''casoBooleano : CASE condiciones DOSPUNTOS subcodigo
                      | CASE ID DOSPUNTOS subcodigo'''

def p_casoDefault(p): #Carlos Alvia
    '''casoDefault : DEFAULT DOSPUNTOS subcodigo
                   | empty'''

def p_bloqueCasosSwitch(p): #Carlos Alvia
    '''bloqueCasosSwitch : casoSwitch
                         | casoSwitch bloqueCasosSwitch'''

def p_casoSwitch(p): #Carlos Alvia
    '''casoSwitch : CASE valores DOSPUNTOS subcodigo'''


#IF -Sofia Zarate
def p_sentenciaIfClasica(p):
    '''sentenciaIf : IF condiciones LBRACE RBRACE
                    | IF condiciones LBRACE subcodigo RBRACE 
                    | IF asignacionCorta SEMICOLON condiciones LBRACE subcodigo RBRACE'''
def p_for(p): #Angello Bravo
    'for : FOR asignacionCorta SEMICOLON condiciones SEMICOLON autooperacion LBRACE subcodigo RBRACE'

def p_forCondicion(p): #Angello Bravo
    'for : FOR condiciones LBRACE subcodigo RBRACE'

def p_forInfinito(p): #Angello Bravo
    'for : FOR LBRACE subcodigo RBRACE'

#ESTRUCTURAS DE DATOS

def p_estructurasDeDatos(p): #Carlos Alvia
    '''estructurasDeDatos : mapa
                        | array
                        | slice
                        '''

#MAPA
def p_definicionMapaVacio(p): #Carlos Alvia 
    '''mapa : MAP LBRACKET tipoDato RBRACKET tipoDato LBRACE RBRACE
            | MAP LBRACKET tipoDato RBRACKET tipoDato'''

def p_definicionMapaValores(p): #Carlos Alvia 
    'mapa : MAP LBRACKET tipoDato RBRACKET tipoDato LBRACE elementosMapa RBRACE'

def p_elementosMapa(p): #Carlos Alvia 
    '''elementosMapa : elementoMapa
                     | elementoMapa elementosMapa'''

def p_elementoMapa(p): #Carlos Alvia 
    '''elementoMapa : valor DOSPUNTOS valor COMMA'''

#ARRAY Sofia Zarate
def p_arrayVacio(p):
    '''array : LBRACKET INT RBRACKET tipoDato
            | LBRACKET INT RBRACKET tipoDato LBRACE RBRACE'''

def p_arrayConElementos(p):
    'array : LBRACKET INT RBRACKET tipoDato LBRACE elementosArray RBRACE'

def p_elementosArray(p):
    '''elementosArray : valor
                        | valor COMMA elementosArray'''

# SLICE Angello Bravo
def p_slice(p):
    'slice : ID LBRACKET valor DOSPUNTOS valor RBRACKET ' 

def p_sliceArray(p):
    'slice : LBRACKET RBRACKET tipoDato LBRACE valores RBRACE'


#DEFINICIÓN DE VARIABLES

#Regla semántica: 
#Que la variable no haya sido definida previamente -SOFIA ZARATE

def p_asignacionTipo(p): #Carlos Alvia
    'asignacion : VAR ID tipoDato ASSIGN valor'
    if p[2] not in variables:
        tipo = p[3].split("_")[0]
        variables[p[2]] = {"tipo": tipo, "value": p[5]["value"]}
    else:
        manejarErrorSemantico(f"Error semántico: la variable {p[2]} ya ha sido declarada previamente", p.slice[1])

def p_asignacionInferencia(p): #Carlos Alvia
    'asignacion : VAR ID ASSIGN valor'
    if p[2] not in variables:
        variables[p[2]] = p[4]
    else:
        manejarErrorSemantico(f"Error semántico: la variable {p[2]} ya ha sido declarada previamente", p.slice[1])

def p_asignacionCorta(p): #Carlos Alvia
    'asignacionCorta : ID DOSPUNTOS ASSIGN valor'
    if p[1] not in variables:
        variables[p[1]] = p[4]
    else:
        manejarErrorSemantico(f"Error semántico: la variable {p[1]} ya ha sido declarada previamente",p.slice[1])

#Regla semántica
#El autoincremento solo es aplicable a variables de tipo numérico
def p_autoincremento(p): #Angello Bravo 
    'autoincremento : ID PLUSPLUS'
    if p[1] in variables:
        if variables[p[1]]["tipo"] not in ("INT", "FLOAT64", "COMPLEX64"):
            manejarErrorSemantico(f"Error Semántico: {variables[p[1]]['tipo']} no es un tipo numérico", p.slice[1])

def p_autodecremento(p): #Angello Bravo
    'autodecremento : ID MINUSMINUS'

def p_autooperacion(p): #Angello Bravo
    '''autooperacion : autoincremento
                        | autodecremento
                        '''

def p_tipoDato(p): #Carlos Alvia 
    '''tipoDato : FLOAT64_TYPE
                  | COMPLEX64_TYPE
                  | INT_TYPE
                  | BOOL_TYPE
                  | STRING_TYPE'''
    p[0] = p.slice[1].type
    
def p_valores(p): #Carlos Alvia 
    '''valores : valor
               | valor COMMA valores''' 
    
def p_valor(p): #Carlos Alvia 
    '''valor : FLOAT64
             | COMPLEX64
             | INT
             | BOOL
             | STRING
             | expresionesAritmeticas
             | condiciones
             | ID
             | estructurasDeDatos'''
    if p.slice[1].type == "ID" and p[1] in variables:
        p[0] = {"tipo": variables[p[1]]["tipo"], "value": variables[p[1]]["value"]}
    elif p.slice[1].type == "condiciones":
        p[0] = {"tipo": "BOOL", "value": p[1]}
    elif p.slice[1].type in ("expresionesAritmeticas","estructurasDeDatos"):
        p[0] = p[1]
    else:
        p[0] = {"tipo": p.slice[1].type, "value": p[1]}

#EXPRESIONES ARITMETICAS
def p_expresionesAritmeticas(p): #Carlos Alvia 
    '''expresionesAritmeticas : expresionAritmetica
                              | expresionAritmetica operador expresionesAritmeticas'''
    if len(p) == 2:
        p[0] = p[1]

def p_expresionAritmeticaPAREN(p):
    'expresionAritmetica : LPAREN valor operador valor RPAREN'
    try:
        if p[2]["tipo"] in ["FLOAT64","INT","COMPLEX64"]:
            if p[4]["tipo"] not in ["FLOAT64","INT","COMPLEX64"]:
        
                manejarErrorSemantico(f"Error semántico: La operación {p[3]} no está definida para {p[4]['tipo']}",p[3])
                
            else:
                if p[2]["tipo"] == p[4]["tipo"]:
                    p[0] = p[2]["tipo"]
                else: 
            
                    manejarErrorSemantico(f"Error semántico: Tipos de datos no coincidentes {p[2]['tipo']} y {p[4]['tipo']}",p[3])
        else:
    
            manejarErrorSemantico(f"Error semántico: La operación {p[3]} no está definida para {p[2]['tipo']}",p[3])   
    except Exception as e:
        pass


def p_expresionAritmetica(p): #Carlos Alvia
    'expresionAritmetica : valor operador valor'

    #Reglas semánticas Carlos Alvia:
    #Las operaciones aritméticas solo se aplican a valores numéricos 
    #Los valores a operar deben ser del mismo tipo de dato
    try:
        if p[1]["tipo"] in ["FLOAT64","INT","COMPLEX64"]:
            if p[3]["tipo"] not in ["FLOAT64","INT","COMPLEX64"]:
        
                manejarErrorSemantico(f"Error semántico: La operación {p[2].value} no está definida para {p[3]['tipo']}",p[2])
            else:
                if p[1]["tipo"] == p[3]["tipo"]: #Esta es la regla de los tipos distintos
                    p[0] = {"tipo": p[1]["tipo"], "value": 0}
                else: 
                    manejarErrorSemantico(f"Error semántico: Tipos de datos no coincidentes {p[1]['tipo']} y {p[3]['tipo']}",p[2])
                    
        else:
            manejarErrorSemantico(f"Error semántico: La operación {p[2].value} no está definida para {p[1]['tipo']}",p[2])
    except Exception as e:
        pass

def p_operador(p): #Carlos Alvia 
    '''operador : PLUS 
                | MINUS
                | TIMES
                | DIVIDE
                | MOD'''
    p[0] = p.slice[1]

#CONDICIONALES
def p_condiciones(p): #Carlos Alvia 
    '''condiciones : condicion
                   | condicion conector condiciones'''

def p_conector(p): #Carlos Alvia 
    '''conector : AND
                | OR'''
    
def p_condicion(p): #Carlos Alvia 
    '''condicion : valor operadorComp valor
                 | BOOL'''

def p_operadorComparacion(p): #Carlos Alvia 
    '''operadorComp : NOT_EQUAL
                    | LESS_THAN
                    | LESS_EQUAL
                    | GREATER_THAN
                    | GREATER_EQUAL
                    | EQUAL'''
    
def p_empty(p): #Carlos Alvia
    'empty :'
    pass

#Impresión con cero, uno o más argumentos Sofia Zarate
def p_imprimir(p):
    '''imprimir : FMT PUNTO PRINT_LN LPAREN valores RPAREN
                | FMT PUNTO PRINT_LN LPAREN RPAREN'''

# Solicitar datos por teclado Angello Bravo
def p_solicitud_datos(p): 
    'solicitudDatos : FMT PUNTO SCANLN LPAREN POINTER ID RPAREN'


def p_error(p):
    if p:
        line_start = p.lexer.lexdata.rfind('\n', 0, p.lexpos) + 1
        line_end = p.lexer.lexdata.find('\n', p.lexpos)
        if line_end == -1:
            line_end = len(p.lexer.lexdata)
        
        line_content = p.lexer.lexdata[line_start:line_end]
        
        token_position = p.lexpos - line_start
        
        error_message = f"Error de sintaxis en la línea:\n"
        error_message += f"{line_content.strip()}\n"
        error_message += f"Token inesperado: '{p.value}' \n"
    else:
        error_message = "Error de sintaxis al final del archivo"
    
    sintax_errors.append(error_message)

def manejarErrorSemantico(mensaje, token):
    line_start = token.lexer.lexdata.rfind('\n', 0, token.lexpos) + 1
    line_end = token.lexer.lexdata.find('\n', token.lexpos)
    if line_end == -1:
        line_end = len(token.lexer.lexdata)
    
    line_content = token.lexer.lexdata[line_start:line_end]
    
    error_message = f"Error Semántico en la línea:\n"
    error_message += f"{line_content.strip()}\n"
    error_message += mensaje
    semantic_errors.append(error_message)


# Build the parser
parser = yacc.yacc()
sintax_errors = []
semantic_errors = []
def parse_input(data):
    variables.clear()
    sintax_errors.clear()
    parser.parse(data)
    if sintax_errors:
        return '\n'.join(sintax_errors)
    else:
        return "No hay errores sintácticos"
    
def parse_semantic(data):
    variables.clear()
    semantic_errors.clear()
    parser.parse(data)
    if semantic_errors:
        return '\n'.join(semantic_errors)
    else:
        return "No hay errores semánticos"

logger.crear_logs(sintax_errors, "Sofia Zarate", 1)
logger.crear_logs(semantic_errors, "Sofia Zarate", 2)
