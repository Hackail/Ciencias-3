import ply.lex as lex

tokens = ['NAME','ID', 'NUMBER', 'LESSEQUAL', 'ASSIGN' ]
reserved = {
    'while' : 'WHILE',
    'then' : 'THEN'
}
tokens += list(reserved.values())

t_ignore    = ' \t'
t_NUMBER    = '\d+'
t_LESSEQUAL = '\<\='
t_ASSIGN    = '\='
t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in reserved:
        t.type = reserved[ t.value ]
    return t

def t_error(t):
    print 'Illegal character'
    t.lexer.skip(1)

lexer = lex.lex()
lexer.input("x while n <= 0 then h = 1 hj")
while True:
    tok = lexer.token()
    if not tok:
        break
    print str(tok.value) + " - " + str(tok.type)