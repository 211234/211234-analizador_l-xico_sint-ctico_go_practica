import ply.lex as lex

# Lista de palabras reservadas
reserved = {
    'package': 'PACKAGE',
    'import': 'IMPORT',
    'func': 'FUNC',
    'main': 'MAIN',
    'Println': 'PRINTLN'
}

# Lista de tokens
tokens = [
    'ID',
    'LPAREN', 'RPAREN',
    'LBRACE', 'RBRACE',
    'STRING',
    'DOT',
] + list(reserved.values())

# Reglas de expresiones regulares para los tokens
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_DOT = r'\.'
t_STRING = r'\"([^\\\n]|(\\.))*?\"'

# Reglas de expresiones regulares con acciones
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t

# Regla para manejar los números de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Caracteres ignorados
t_ignore = ' \t'

# Regla de error
def t_error(t):
    print("Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()
