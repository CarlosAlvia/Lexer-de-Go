import ply.lex as lex
import logger 


reserved = {"default": "DEFAULT", "func": "FUNC", "case": "CASE", "map": "MAP", "switch": "SWITCH", "if": "IF", "for": "FOR", "var": "VAR"}
dataTypes = {"float64": "FLOAT64_TYPE", "int": "INT_TYPE", "string": "STRING_TYPE", "bool": "BOOL_TYPE",
             "complex64": "COMPLEX64_TYPE"}
standardFunctions = {"fmt": "FMT", "Println": "PRINT_LN", "Scanln":"SCANLN"}
#Este token tiene la unica finalidad de agregar los errores en la lista que usa el Logger para escribir los Logs
ilegalType = ('ILLEGAL',)

tokens = (
    'ID',
    'FLOAT64',
    'COMPLEX64',
    'INT',
    'STRING',
    'BOOL',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'MOD',
    'DOSPUNTOS',
    'ASSIGN',
    'PLUSPLUS',
    'MINUSMINUS',
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

t_LPAREN = r'\('
t_RPAREN = r'\)'

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


def t_ID(t):
    r'[_a-zA-Z]\w*'
    t.type = reserved.get(t.value,"ID")
    if t.type=="ID": 
        t.type = dataTypes.get(t.value,"ID")
    if t.type=="ID": 
        t.type = standardFunctions.get(t.value,"ID")
    return t

def t_COMMENT(t):
    r'//.*|/\*[\s\S]*?\*/'
    pass  # Para ignorar los comentarios

def t_PLUSPLUS(t):
    r'\+\+'
    return t

def t_MINUSMINUS(t): 
    r'--'
    return t

def t_PLUS(t): 
    r'\+'
    return t
def t_MINUS(t):
    r'-'
    return t

def t_TIMES(t):
    r'\*'
    return t

def t_DIVIDE(t):
    r'/'
    return t

def t_MOD(t):
    r'%'
    return t

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



def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)



t_ignore = ' \t'

def t_error(t):
    global tokensList
    illegal_tok = lex.LexToken()
    illegal_tok.type = 'ILLEGAL'
    illegal_tok.value = t.value[0]
    illegal_tok.lineno = t.lineno
    illegal_tok.lexpos = t.lexpos
    tokensList.append(illegal_tok)
    t.lexer.skip(1)


lexer = lex.lex()


algoritmoCarlos = '''
func algoritmo(){

    var entero int = (450  * 2 - 200 + 23) / (20%3)
    var complejo complex64 = 2+12i
    var verdadero bool = true
    mensajes := [2]string{"Algoritmo", "Random"}
    var flotante float64 = 23.92 

    if v := 4.12; 3 + 3 > 10 {

        flotante = flotante - v
        complejo++

    }
}
'''

algoritmoSofiaZarate = '''
// Variables globales
var complejo complex64 = 4.7+6.2i
var arreglo = []int{10, 20, 30}
var flotante float64 = 8.15
var entero int = 11

func main() {
    if entero > 10 || flotante == 1.23 {
        var cadena string = "Hola Soledad"
        for i := 0; i < 2; i++ {
            entero = entero + 2
        }

        if flotante <= 5 {
            fmt.Println(cadena,entero)
        }
    }
}
'''
tokensList = []
def lex_input(data):
    tokensList.clear()
    lexer.input(data)
    result = []
    while True:
            tok = lexer.token()
            if not tok:
                break  
            tokensList.append(tok)
    for tok in tokensList:
        result.append(str(tok))
    return '\n'.join(result)

# usuarioGit = 'Angello Bravo'
#logger.crear_logs(tokensList, usuarioGit, 0) Cero para el léxico
