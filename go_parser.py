import ply.yacc as yacc
from lexer import tokens, reserved

# Reglas de la gramática

def p_program(p):
    'program : package_decl import_decl func_decl'
    pass

def p_package_decl(p):
    'package_decl : PACKAGE MAIN'
    pass

def p_import_decl(p):
    'import_decl : IMPORT STRING'
    pass

def p_func_decl(p):
    'func_decl : FUNC MAIN LPAREN RPAREN LBRACE stmt RBRACE'
    pass

def p_stmt(p):
    'stmt : ID DOT PRINTLN LPAREN STRING RPAREN'
    pass

def p_error(p):
    if not p:
        raise SyntaxError("Error de sintaxis: se esperaba un componente, pero el archivo terminó de forma inesperada.")
    
    if p.type == 'ID' and p.value in reserved:
        raise SyntaxError(f"Error de sintaxis: se esperaba una palabra reservada pero se encontró '{p.value}'.")
    elif p.type == 'ID':
        raise SyntaxError(f"Error de sintaxis: identificador desconocido '{p.value}' en la línea {p.lineno}.")
    elif p.type in ('LPAREN', 'RPAREN', 'LBRACE', 'RBRACE'):
        raise SyntaxError(f"Error de sintaxis: falta '{p.type}' en la línea {p.lineno}.")
    elif p.type == 'STRING':
        raise SyntaxError(f"Error de sintaxis: cadena mal formada '{p.value}' en la línea {p.lineno}.")
    else:
        raise SyntaxError(f"Error de sintaxis: se encontró '{p.value}' pero se esperaba otra cosa en la línea {p.lineno}.")

# Construir el parser
parser = yacc.yacc()