import ply.lex as lex

# Inicio aporte Carlos Alvia
reserved = {"break": "BREAK", "default": "DEFAULT", "funct": "FUNCT", "Interface": "INTERFACE", "select": "SELECT", "case": "CASE", "defer": "DEFER", "Go": "GO", "map": "MAP", "struct": "STRUCT", "chan": "CHAN", "else": "ELSE", "Goto": "GOTO", "package": "PACKAGE", "switch": "SWITCH", "const": "CONST", "fallthrough": "FALLTHROUGH", "if": "IF", "range": "RANGE", "type": "TYPE", "continue": "CONTINUE", "for": "FOR", "import": "IMPORT", "return": "RETURN", "var": "VAR"}

tokens = (
    'ID',
    'BOOL'
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