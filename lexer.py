import ply.lex as lex

reserved = {
   'si' : 'SI',
   'luego' : 'LUEGO',
   'sino' : 'SINO',
   'mientras' : 'MIENTRAS'
}

tokens = [ 'NAME','NUMBER','PLUS','MINUS','TIMES','DIVIDE', 'EQUALS']+list(reserved.values())

t_ignore = ' \t'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r':='
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t
    
    
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID') 
    return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex() # Build the lexer

lex.input("x := 3 - 4 + 5 * 6 si")
while True:
    tok = lex.token()
    if not tok: break
    print str(tok.value) + " - " + str(tok.type)
