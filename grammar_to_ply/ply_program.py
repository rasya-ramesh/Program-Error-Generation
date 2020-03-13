from random import choice

class Node:
  def __init__(self, n_type, value, children=None, leaf=None):
    self.type = n_type
    self.value = value
    if children:
      self.children = children
    else:
      self.children = [ ]

    self.leaf = leaf
  def __repr__(self, level=0):
    ret = "	"*level+repr(self.value)+"\n"
    for child in self.children:
      ret += child.__repr__(level+1)
    return ret

reserved = {'def': 'DEF', 'if': 'IF', 'else': 'ELSE', 'elif': 'ELIF', 'return': 'RETURN', 'None': 'NONE', 'True': 'TRUE', 'False': 'FALSE', 'for': 'FOR', 'in': 'IN', 'pass': 'PASS'}
tokens = ['DEF', 'IF', 'ELSE', 'ELIF', 'RETURN', 'NONE', 'TRUE', 'FALSE', 'FOR', 'IN', 'PASS', 'EQUALS', 'COMMA', 'COLON', 'LPAREN', 'RPAREN', 'TAB', 'IDENTIFIER', 'STRING', 'NUMBER', 'PLUS', 'MINUS', 'DIVIDE', 'MULTIPLY', 'MODULUS', 'GR', 'LE', 'EQ', 'GREQ', 'LEEQ', 'LSQUARE', 'RSQUARE']

def t_NUMBER(t):
	r'\d+'
	t.type=reserved.get(t.value,'NUMBER')
	t.value = Node('NUMBER', t.value, leaf = 1)
	return t

def t_EQ(t):
	r'\=='
	t.type=reserved.get(t.value,'EQ')
	t.value = Node('EQ', t.value, leaf = 1)
	return t

def t_GREQ(t):
	r'\>='
	t.type=reserved.get(t.value,'GREQ')
	t.value = Node('GREQ', t.value, leaf = 1)
	return t

def t_LEEQ(t):
	r'\<='
	t.type=reserved.get(t.value,'LEEQ')
	t.value = Node('LEEQ', t.value, leaf = 1)
	return t

def t_STRING(t):
	r'\"[a-zA-Z0-9 _]*\"'
	t.type=reserved.get(t.value,'STRING')
	t.value = Node('STRING', t.value, leaf = 1)
	return t

def t_IDENTIFIER(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	t.type=reserved.get(t.value,'IDENTIFIER')
	t.value = Node('IDENTIFIER', t.value, leaf = 1)
	return t

def t_EQUALS(t):
	r'\='
	t.value = Node('EQUALS', '=', leaf = 1)
	return t

def t_COMMA(t):
	r'\,'
	t.value = Node('COMMA', ',', leaf = 1)
	return t

def t_COLON(t):
	r'\:'
	t.value = Node('COLON', ':', leaf = 1)
	return t

def t_LPAREN(t):
	r'\('
	t.value = Node('LPAREN', '(', leaf = 1)
	return t

def t_RPAREN(t):
	r'\)'
	t.value = Node('RPAREN', ')', leaf = 1)
	return t

def t_TAB(t):
	r'\t'
	t.value = Node('TAB', '\t', leaf = 1)
	return t

def t_PLUS(t):
	r'\+'
	t.value = Node('PLUS', '+', leaf = 1)
	return t

def t_MINUS(t):
	r'\-'
	t.value = Node('MINUS', '-', leaf = 1)
	return t

def t_DIVIDE(t):
	r'\/'
	t.value = Node('DIVIDE', '/', leaf = 1)
	return t

def t_MULTIPLY(t):
	r'\*'
	t.value = Node('MULTIPLY', '*', leaf = 1)
	return t

def t_MODULUS(t):
	r'\%'
	t.value = Node('MODULUS', '%', leaf = 1)
	return t

def t_GR(t):
	r'\>'
	t.value = Node('GR', '>', leaf = 1)
	return t

def t_LE(t):
	r'\<'
	t.value = Node('LE', '<', leaf = 1)
	return t

def t_LSQUARE(t):
	r'\['
	t.value = Node('LSQUARE', '[', leaf = 1)
	return t

def t_RSQUARE(t):
	r'\]'
	t.value = Node('RSQUARE', ']', leaf = 1)
	return t

def p_start(t):
	'''start : construct''' 
	t[0] = Node("start", "start", t[1:], leaf = 0)


def p_construct(t):
	'''construct : funcdef construct 
	| statement construct 
	| statement 
	| funcdef''' 
	t[0] = Node("construct", "construct", t[1:], leaf = 0)


def p_statement_suite(t):
	'''statement_suite : TAB statement  
	|  TAB statement statement_suite''' 
	t[0] = Node("statement_suite", "statement_suite", t[1:], leaf = 0)


def p_statement(t):
	'''statement : return_stmt 
	| assignment_stmt 
	| func_call_stmt 
	| loop_stmt 
	| if_stmt 
	| PASS''' 
	t[0] = Node("statement", "statement", t[1:], leaf = 0)


def p_loop_stmt(t):
	'''loop_stmt : for_loop''' 
	t[0] = Node("loop_stmt", "loop_stmt", t[1:], leaf = 0)


def p_for_loop(t):
	'''for_loop : FOR IDENTIFIER IN IDENTIFIER COLON statement_suite''' 
	t[0] = Node("for_loop", "for_loop", t[1:], leaf = 0)


def p_if_stmt(t):
	'''if_stmt : IF LPAREN arithmetic_expr RPAREN COLON statement_suite 
	| IF LPAREN arithmetic_expr RPAREN COLON statement_suite elif_stmt''' 
	t[0] = Node("if_stmt", "if_stmt", t[1:], leaf = 0)


def p_elif_stmt(t):
	'''elif_stmt : ELIF LPAREN arithmetic_expr RPAREN COLON statement_suite else_stmt 
	| else_stmt''' 
	t[0] = Node("elif_stmt", "elif_stmt", t[1:], leaf = 0)


def p_else_stmt(t):
	'''else_stmt : ELSE COLON statement_suite''' 
	t[0] = Node("else_stmt", "else_stmt", t[1:], leaf = 0)


def p_funcdef(t):
	'''funcdef : DEF IDENTIFIER LPAREN parameters RPAREN COLON statement_suite 
	| DEF IDENTIFIER LPAREN RPAREN COLON statement_suite''' 
	t[0] = Node("funcdef", "funcdef", t[1:], leaf = 0)


def p_parameters(t):
	'''parameters : atom 
	| atom COMMA parameters 
	| empty''' 
	t[0] = Node("parameters", "parameters", t[1:], leaf = 0)


def p_func_call_stmt(t):
	'''func_call_stmt : IDENTIFIER LPAREN parameters RPAREN''' 
	t[0] = Node("func_call_stmt", "func_call_stmt", t[1:], leaf = 0)


def p_assignment_stmt(t):
	'''assignment_stmt : IDENTIFIER EQUALS expression''' 
	t[0] = Node("assignment_stmt", "assignment_stmt", t[1:], leaf = 0)


def p_expression(t):
	'''expression : arithmetic_expr 
	| func_call_stmt''' 
	t[0] = Node("expression", "expression", t[1:], leaf = 0)


def p_arithmetic_expr(t):
	'''arithmetic_expr : arithmetic_expr arithmetic_op arithmetic_expr 
	| atom''' 
	t[0] = Node("arithmetic_expr", "arithmetic_expr", t[1:], leaf = 0)


def p_return_stmt(t):
	'''return_stmt : RETURN expression''' 
	t[0] = Node("return_stmt", "return_stmt", t[1:], leaf = 0)


def p_atom(t):
	'''atom : IDENTIFIER 
	| literal''' 
	t[0] = Node("atom", "atom", t[1:], leaf = 0)


def p_literal(t):
	'''literal : NUMBER 
	| NONE 
	| TRUE 
	| FALSE 
	| STRING 
	| list''' 
	t[0] = Node("literal", "literal", t[1:], leaf = 0)


def p_list(t):
	'''list : LSQUARE parameters  RSQUARE''' 
	t[0] = Node("list", "list", t[1:], leaf = 0)


def p_arithmetic_op(t):
	'''arithmetic_op : PLUS 
	| MINUS 
	| MODULUS 
	| DIVIDE 
	| MULTIPLY 
	| GR 
	| LE 
	| EQ 
	| GREQ 
	| LEEQ''' 
	t[0] = Node("arithmetic_op", "arithmetic_op", t[1:], leaf = 0)


# Ignored characters
t_ignore = " "
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def p_empty(p):
     'empty :'
     pass
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def p_error(t):
    print("Syntax error at '%s'" % t.value)

import ply.lex as lex
lexer = lex.lex()


import ply.yacc as yacc
yacc.yacc()


start= 'start'

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
data = open('../programs/python/functions/input_programs/helloworld.py',"r").read()

root = yacc.parse(data)
def printYield(root, reqpos, type):
    # Stack to store all the nodes
    # of tree
    s1 = []

    # Stack to store all the
    # leaf nodes
    s2 = []

    # Push the root node
    s1.append(root)
    n=0
    while len(s1) != 0:
        curr = s1.pop()

        # If current node has a left child
        # push it onto the first stack
        for child in curr.children:
          s1.append(child)

        if curr.leaf:
            n+=1
            if type == "remove" and n not in reqpos:
                s2.append(curr)

            if type == "add":
                s2.append(curr)
                if n in reqpos:
                    temp = Node("dummy", "errnode", leaf = 1)
                    s2.append(temp)
            if type == "replace":
                if n in reqpos:
                    temp = Node("dummy", "@@@", leaf = 1)
                    s2.append(temp)
                else:
                    s2.append(curr)

    # Print all the leaf nodes
    level = 0
    s = ""
    while len(s2) != 0:
      val = s2.pop()
      # s = print("	"*level + val.value, end = " ")
      s = s+'	' * level + val.value + " "
      # print(s)
      colon = Node("COLON",":", leaf = 1)
      if val == colon:
        #print("")
        level += 1


    return s

def getPgmLen(root):
    s1 = []
    s2 = []
    s1.append(root)
    while len(s1) != 0:
        curr = s1.pop()
        for child in curr.children:
            s1.append(child)

        if curr.leaf:
            s2.append(curr)

    return len(s2)


#print(root.__repr__())
# printYield(function, [0], "remove")
pgmLen = getPgmLen(root)


#### now we will try to introduce errors in the above syntax tree
pgms =  2
directory= '../programs/python/functions/output_programs/'
#directory = "../programs/python/functions/output_programs/"
fname = 'helloworld.py'.split(".")[0]
extension = 'helloworld.py'.split(".")[1]
positions = [i for i in range(1,pgmLen)]
for n_errors in range(1,4):
    #print("Programs with "+str(n_errors)+" errors")
    for i in range(0,pgms):
        reqpos = []
        for j in range(0,n_errors):
            c = choice(positions)
            reqpos.append(c)
            positions.remove(c)
        positions = [i for i in range(1,pgmLen)]
        #print("REMOVE:")
        pgm = printYield(root, reqpos, "remove")
        #f = open("pgm_" + str(pgms) + "_" + str(n_errors) + "remove." +extension, "w")
        f=open(directory+fname + "_" + str(n_errors) + "remove.py", "w")
        f.write(pgm)
        f.close()
        #print("ADD:")
        pgm = printYield(root, reqpos, "add")
        f = open(directory+fname + "_" + str(n_errors) + "add." + extension, "w")
        f.write(pgm)
        f.close()
        #print("REPLACE:")
        pgm = printYield(root, reqpos, "replace")
        f = open(directory+fname + "_" + str(n_errors)+ "replace." + extension , "w")
        f.write(pgm)
        f.close()
        #print("")
# x = open("temp.txt",'w')
# x.write("dude what")
# x.close()
