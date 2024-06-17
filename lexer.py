import ply.lex as lex
import logger 

# Inicio aporte Carlos Alvia
reserved = {"break": "BREAK", "default": "DEFAULT", "funct": "FUNCT", "Interface": "INTERFACE", "select": "SELECT", "case": "CASE", "defer": "DEFER", "go": "GO", "map": "MAP", "struct": "STRUCT", "chan": "CHAN", "else": "ELSE", "goto": "GOTO", "package": "PACKAGE", "switch": "SWITCH", "const": "CONST", "fallthrough": "FALLTHROUGH", "if": "IF", "range": "RANGE", "type": "TYPE", "continue": "CONTINUE", "for": "FOR", "import": "IMPORT", "return": "RETURN", "var": "VAR"}
dataTypes = {"float64": "FLOTANTE64_TYPE", "int": "ENTERO_TYPE", "string": "CADENA_TYPE", "bool": "BOOL_TYPE"}

tokens = (
    'FLOTANTE64',
    'ENTERO',
    'CADENA',
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
    'IGUAL'
)+tuple(reserved.values())+tuple(dataTypes.values())

# Expresiones regulares
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_MOD = r'%'
t_DOSPUNTOS = r':'
t_IGUAL = r'='

def t_BOOL(t):
    r'true|false'
    if(t == 'true'):
        t.value = True
    else: 
        t.value = False
    return t

def t_CADENA(t):
    r'("[^"]*")|(`[^`]*`)'
    t.value = str(t.value)
    return t

def t_FLOTANTE64(t):
    r'(-)?\d+\.(\d+)?([eE][+-]?\d+)?'
    t.value = float(t.value)
    return t

def t_ENTERO(t):
    r'(-|\+)?\d{1,19}'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[_a-zA-Z]\w*'
    t.type = reserved.get(t.value,"ID")
    if t.type=="ID": 
        t.type = dataTypes.get(t.value,"ID")
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

data = '''
if ( x > 4 )
for
var a int = -64.2e9
var b string = "asdaskodasda
  asdasdasdasdad"
'''

lexer.input(data)
tokens = []
while True:
        tok = lexer.token()
        if not tok:
            break  
        print(tok)
        tokens.append(tok)

usuarioGit = 'Angello Bravo'
logger.crear_logs(tokens, usuarioGit)
