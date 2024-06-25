import ply.lex as lex
import logger 


reserved = {"break": "BREAK", "default": "DEFAULT", "func": "FUNC", "Interface": "INTERFACE", "select": "SELECT", "case": "CASE", "defer": "DEFER", "go": "GO", "map": "MAP", "struct": "STRUCT", "chan": "CHAN", "else": "ELSE", "goto": "GOTO", "package": "PACKAGE", "switch": "SWITCH", "const": "CONST", "fallthrough": "FALLTHROUGH", "if": "IF", "range": "RANGE", "type": "TYPE", "continue": "CONTINUE", "for": "FOR", "import": "IMPORT", "return": "RETURN", "var": "VAR"}
dataTypes = {"float64": "FLOAT64_TYPE", "int": "INT_TYPE", "string": "STRING_TYPE", "bool": "BOOL_TYPE",
             "complex64": "COMPLEX64_TYPE"}
standardFunctions = {"fmt": "FMT", "Println": "PRINT_LN", "Scanln":"SCANLN"}
#Este token tiene la unica finalidad de agregar los errores en la lista que usa el Logger para escribir los Logs
ilegalType = ('ILLEGAL',)

tokens = (
    'FLOAT64',
    'COMPLEX64',
    'INT',
    'STRING',
    'BOOL',
    'ID',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'MOD',
    'DOSPUNTOS',
    'ASSIGN',
    'EQUAL', #Inicio de los operadores de comparacion
    'NOT_EQUAL',
    'LESS_THAN',
    'LESS_EQUAL',
    'GREATER_THAN',
    'GREATER_EQUAL',
    'AND', #Inicio de los operadores lógicos
    'OR',
    'NOT',
    'LBRACE', #Inicio de delimitadores {
    'RBRACE', 
    'LBRACKET',
    'RBRACKET',
    'COMMA',
    'PUNTO',
    'SEMICOLON',
    'COMMENT',
    'POINTER',
) + ilegalType + tuple(reserved.values())+tuple(dataTypes.values())+tuple(standardFunctions.values())

# Expresiones regulares
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_MOD = r'%'
t_DOSPUNTOS = r':'
t_ASSIGN = r'='

t_EQUAL = r'=='
t_NOT_EQUAL = r'!='
t_LESS_THAN = r'<'
t_LESS_EQUAL = r'<='
t_GREATER_THAN = r'>'
t_GREATER_EQUAL = r'>='

t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'

t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA = r','
t_PUNTO = r'\.'
t_SEMICOLON = r';'
t_POINTER = r'&'

def t_BOOL(t):
    r'true|false'
    if(t == 'true'):
        t.value = True
    else: 
        t.value = False
    return t

def t_STRING(t):
    r'("[^"]*")|(`[^`]*`)'
    t.value = str(t.value)
    return t


def t_COMPLEX64(t):
    r'((-)?\d+(\.(\d+)?([eE][+-]?\d+)?)?(-|\+))?(\d+i|\d*\.(\d+)?([eE][+-]?\d+)?i)'
    return t

def t_FLOAT64(t):
    r'(-)?\d+\.(\d+)?([eE][+-]?\d+)?'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'(-|\+)?\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[_a-zA-Z]\w*'
    t.type = reserved.get(t.value,"ID")
    if t.type=="ID": 
        t.type = dataTypes.get(t.value,"ID")
    if t.type=="ID": 
        t.type = standardFunctions.get(t.value,"ID")
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_COMMENT(t):
    r'//.*|/\*[\s\S]*?\*/'
    pass  # Para ignorar los comentarios

t_ignore = ' \t'

def t_error(t):
    global tokensList
    print("Illegal character '%s'" % t.value[0])
    illegal_tok = lex.LexToken()
    illegal_tok.type = 'ILLEGAL'
    illegal_tok.value = t.value[0]
    illegal_tok.lineno = t.lineno
    illegal_tok.lexpos = t.lexpos
    tokensList.append(illegal_tok)
    t.lexer.skip(1)


lexer = lex.lex()

algoritmoAngello = '''
//Esto es un comentario
/*Esto tambien es un comentario*/

package main
import "fmt"

var complejo complex64 = 2.5+12i
var arreglo = []int{1, 2, 3}
var z float64 = 2.65
var entero int = 2

func main(){
    if  entero >= 2 || z != 2.66 {
        var texto string = "Hola Mundo"
        for i := 0; i < 5; i++{
            entero += i * z / 3
        }
        if z > 20 && z <= 30 {
        return texto;
        }else{
            return entero
        }
    }
}


'''

algoritmoCarlos = '''

func algoritmo(){
    var entero int = (450  * 2 - 200 + 23) / (20%3)
    var complejo complex64 = 2+12i
    var condicion bool =  !(entero > 2 && entero >= 400 || entero <= 2000)
    var condicion2 = entero != 40 && entero < 50000 
    const verdadero bool = true
    mensajes := [2]string{"Algoritmo", "Random"}
    var flotante float64 = 23.92;  
    p := Persona{ Nombre: "Juan", Edad: 30, } 
    nombre := p.Nombre
    if v := 4.12; condicion && condicion2 || !verdadero {
        flotante = flotante - v
        nombre = nombre + mensajes[1]
        complejo = complejo + 2i // Suma complejos 
    }
}
'''

algoritmoSofiaZarate = '''
package main

import "fmt"

// Variables globales
var complejo complex64 = 4.7+6.2i
var arreglo = []int{10, 20, 30}
var flotante float64 = 8.15
var entero int = 11

func main() {
    if entero > 10 || flotante == 1.23 {
        var cadena string = "Hola Soledad"
        for i := 0; i < 2; i++ {
            entero += i * int(flotante) / 2
        }

        if flotante <= 5 {
            fmt.Println(cadena)
        } else {
            fmt.Println(entero, complejo)
        }
    }
}
'''

data = algoritmoAngello

lexer.input(data)
tokensList = []
while True:
        tok = lexer.token()
        if not tok:
            break  
        # print(tok)
        tokensList.append(tok)

        

usuarioGit = 'Angello Bravo'
#logger.crear_logs(tokensList, usuarioGit, 0) Cero para el léxico
