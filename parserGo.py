import ply.yacc as yacc
from lexer import tokens

def p_codigo(p):
    '''codigo : funcion'''#TODO

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
    
#ESTRUCTURAS DE CONTROL
def p_subcodigo(p): #Se refiere al código que puede ir en un if, for, switch o una función Carlos Alvia
     '''subcodigo : asignacionCorta
                  | asignacion''' #TODO

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

#ESTRUCTURAS DE DATOS

def p_estructurasDeDatos(p): #Carlos Alvia
    '''estructurasDeDatos : mapa'''
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

#DEFINICIÓN DE VARIABLES
def p_asignacionTipo(p): #Carlos Alvia 
    'asignacion : VAR ID tipoDato ASSIGN valor'

def p_asignacionInferencia(p): #Carlos Alvia 
    'asignacion : VAR ID ASSIGN valor'

def p_asignacionCorta(p): #Carlos Alvia 
    'asignacionCorta : ID DOSPUNTOS ASSIGN valor'

def p_tipoDato(p): #Carlos Alvia 
    '''tipoDato : FLOAT64_TYPE
                  | COMPLEX64_TYPE
                  | INT_TYPE
                  | BOOL_TYPE
                  | STRING_TYPE'''
    
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
    
#EXPRESIONES ARITMETICAS
def p_expresionesAritmeticas(p): #Carlos Alvia 
    '''expresionesAritmeticas : expresionAritmetica
                              | expresionAritmetica operador expresionesAritmeticas'''

def p_expresionAritmetica(p): #Carlos Alvia 
    '''expresionAritmetica : valor operador valor
                             | LPAREN valor operador valor RPAREN'''
    
def p_operador(p): #Carlos Alvia 
    '''operador : PLUS
                | MINUS
                | TIMES
                | DIVIDE
                | MOD'''
    
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

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")
    print(p.value)

# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = input('lp > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)