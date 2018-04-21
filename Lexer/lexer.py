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

#entrada_lexer="ggvg"
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'NAME')    # Check for reserved words
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
lex.input(open("archivo.txt").read())
#lex.input(entrada_lexer)
while True:
    tok = lex.token()
    if not tok: 
        break
    print str(tok.value) + " - " + str(tok.type)
    