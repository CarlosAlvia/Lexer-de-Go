import ply.lex as lex

# Inicio aporte Carlos Alvia
reserved = {"break": "BREAK", "default": "DEFAULT", "funct": "FUNCT", "Interface": "INTERFACE", "select": "SELECT", "case": "CASE", "defer": "DEFER", "go": "GO", "map": "MAP", "struct": "STRUCT", "chan": "CHAN", "else": "ELSE", "goto": "GOTO", "package": "PACKAGE", "switch": "SWITCH", "const": "CONST", "fallthrough": "FALLTHROUGH", "if": "IF", "range": "RANGE", "type": "TYPE", "continue": "CONTINUE", "for": "FOR", "import": "IMPORT", "return": "RETURN", "var": "VAR"}

tokens = (
    'ID',
    'ENTERO',
    'CADENA',
    'CADENA_TYPE',
    'ENTERO_TYPE',
    'FLOTANTE_TYPE',
    'BOOL_TYPE',
    'FLOTANTE'
    'BOOL',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'MOD',
    'DOSPUNTOS',
    'IGUAL'
)+tuple(reserved.values())

# Expresiones regulares

def t_ID(t):
    r'[_a-zA-Z]\w*'
    t.type = reserved.get(t.value,"ID")
    return t

def t_BOOL(t):
    r'true|false'
    if(t == 'true'):
        t.value = True
    else: 
        t.value = False
    return t

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_MOD = r'%'
t_DOSPUNTOS = r':'
t_IGUAL = r'='
t_ENTERO_TYPE = r'int'
t_CADENA_TYPE = r'string'
t_BOOL_TYPE = r'bool'

def t_CADENA(t):
    r'("[^"]*")|(`[^`]*`)'
    t.value = str(t.value)
    return t

def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_FLOTANTE(t):
    r'(-?)(0|[1-9][0-9]*)?\.\d*'
    t.value = float(t.value)
    return t

t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# Test it out
data = '''var a int = 64
var b string = "asdaskodasda
  asdasdasdasdad"'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)

