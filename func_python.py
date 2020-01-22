
# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables -- all in one file.
# -----------------------------------------------------------------------------

# Function grammar:
# funcdef: 'def' NAME parameters  ':' func_body_suite
# parameters: '(' [typedargslist] ')'
reserved = {
    'def' : 'DEF'
 }
tokens = [ 'COLON', 'COMMA','TAB',  'NAME', 'LPAREN','RPAREN' ] + list(reserved.values())

# Tokens
t_COMMA   = r'\,'
t_COLON   = r'\:'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_TAB     = r'\t'
#t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_NAME(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reserved.get(t.value,'NAME')    # Check for reserved words
     return t

# Ignored characters
t_ignore = " "#"\t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def p_empty(p):
     'empty :'
     pass
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lexer = lex.lex()

# dictionary of names
#
# func_body = []
# func_stmt = []
start= 'funcdef'

def p_funcdef(t):
    '''funcdef : DEF NAME LPAREN parameters RPAREN COLON funcbody'''
    print("function name:",t[2])

def p_parameters(t):
    '''parameters : NAME
                  | NAME COMMA parameters
                  | empty'''
    if(t[1]!=None):
        print("arg: ",t[1])

def p_funcbody(t):
    '''funcbody :  TAB statement
                |  TAB statement funcbody'''        #how to do newline?
    # print("BODY: " ," ".join(func_stmt))


def p_statement(t):
    '''statement : NAME
                 | NAME statement'''            #have to change NAME with expressions/statements.
    # func_stmt.insert(0, t[1] )

def p_error(t):
    print("Syntax error at '%s'" % t.value)


import ply.yacc as yacc
parser = yacc.yacc()
#
# while True:
#     try:
#         s = input('codesegment > ')   # Use raw_input on Python 2
#     except EOFError:
#         break
#     print("code=",s)
#     print(yacc.parse(s))
#data = input('codesegment : \n')
#data.replace('\n','')
data='''def foo(a,b):
\tsome_statement
\treturn a'''
print(data)

print(yacc.parse(data))
