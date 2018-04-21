import ply.lex as lex

tokens = [ 'NAME','NUMBER','PLUS','MINUS','TIMES','DIVIDE', 'EQUALS']

reserved = {
   'if' : 'IF',
   'then' : 'THEN',
   'else' : 'ELSE',
   'while' : 'WHILE'
}


tokens = tokens + list(reserved.values())

t_ignore = ' \t'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r':='
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_]*'
    if str(t.value) in reserved:
        t.type = reserved[ t.value ]
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lex.lex() # Build the lexer

lex.input("x := 3 - 4 + 5 * 6 if")
while True:
    tok = lex.token()
    if not tok: 
        break
    print str(tok.value) + " - " + str(tok.type)