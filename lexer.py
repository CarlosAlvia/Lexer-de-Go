import ply.lex as lex

# Inicio aporte Carlos Alvia
reserved = {"break": "BREAK", "default": "DEFAULT", "funct": "FUNCT", "Interface": "INTERFACE", "select": "SELECT", "case": "CASE", "defer": "DEFER", "go": "GO", "map": "MAP", "struct": "STRUCT", "chan": "CHAN", "else": "ELSE", "goto": "GOTO", "package": "PACKAGE", "switch": "SWITCH", "const": "CONST", "fallthrough": "FALLTHROUGH", "if": "IF", "range": "RANGE", "type": "TYPE", "continue": "CONTINUE", "for": "FOR", "import": "IMPORT", "return": "RETURN", "var": "VAR"}

tokens = (
    'ID',
    'FLOTANTE64',
    'FLOTANTE64_TYPE',
    'ENTERO',
    'ENTERO_TYPE',
    'CADENA',
    'CADENA_TYPE',
    'BOOL',
    'BOOL_TYPE',
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
t_FLOTANTE64_TYPE = r'float64'
t_BOOL_TYPE = r'bool'

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

def t_CADENA(t):
    r'("[^"]*")|(`[^`]*`)'
    t.value = str(t.value)
    return t

def t_FLOTANTE64(t):
    r'(-)?\d+(\.\d+)?([eE][+-]?\d+)?'
    t.value = float(t.value)
    return t

def t_ENTERO(t):
    r'(-|\+)?\d{1,19}'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# Test it out
data = '''var a int = -64.2e9
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

