import ply.lex as lex
import logger 

# Inicio aporte Carlos Alvia
reserved = {"break": "BREAK", "default": "DEFAULT", "funct": "FUNCT", "Interface": "INTERFACE", "select": "SELECT", "case": "CASE", "defer": "DEFER", "go": "GO", "map": "MAP", "struct": "STRUCT", "chan": "CHAN", "else": "ELSE", "goto": "GOTO", "package": "PACKAGE", "switch": "SWITCH", "const": "CONST", "fallthrough": "FALLTHROUGH", "if": "IF", "range": "RANGE", "type": "TYPE", "continue": "CONTINUE", "for": "FOR", "import": "IMPORT", "return": "RETURN", "var": "VAR"}
dataTypes = {"float64": "FLOTANTE64_TYPE", "int": "ENTERO_TYPE", "string": "CADENA_TYPE", "bool": "BOOL_TYPE"}

ilegalType = 'ILLEGAL'

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
    'SEMICOLON'
) + tuple(ilegalType) +tuple(reserved.values())+tuple(dataTypes.values())

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

data = '''
if ( !(x > 4) )
for }
var a int = -64.2e9
var b string = "asdaskodasda
  asdasdasdasdad break" 
'''

lexer.input(data)
tokensList = []
while True:
        tok = lexer.token()
        if not tok:
            break  
        print(tok)
        tokensList.append(tok)

        

usuarioGit = 'Angello Bravo'
logger.crear_logs(tokensList, usuarioGit)
