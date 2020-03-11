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

reserved = {'void': 'VOID', 'int': 'INT', 'bool': 'BOOL', 'char': 'CHAR', 'else': 'ELSE', 'if': 'IF', 'while': 'WHILE', 'do': 'DO', 'for': 'FOR'}
tokens = ['VOID', 'INT', 'BOOL', 'CHAR', 'ELSE', 'IF', 'WHILE', 'DO', 'FOR', 'EQUALS', 'COMMA', 'COLON', 'LPAREN', 'RPAREN', 'TAB', 'NAME', 'STRING', 'NUMBER', 'PLUS', 'MINUS', 'DIVIDES', 'TIMES', 'MODULUS', 'GREATERTHAN', 'LESSTHAN', 'EQUALEQUAL', 'GREATEQ', 'LESSEQ', 'LSQUARE', 'RSQUARE', 'LFPAREN', 'RFPAREN', 'SCOLON']

def t_NUMBER(t):
	r'\d+'
	t.type=reserved.get(t.value,'NUMBER')
	t.value = Node('NUMBER', t.value, leaf = 1)
	return t

def t_EQUALEQUAL(t):
	r'\=='
	t.type=reserved.get(t.value,'EQUALEQUAL')
	t.value = Node('EQUALEQUAL', t.value, leaf = 1)
	return t

def t_GREATEQ(t):
	r'\>='
	t.type=reserved.get(t.value,'GREATEQ')
	t.value = Node('GREATEQ', t.value, leaf = 1)
	return t

def t_LESSEQ(t):
	r'\<='
	t.type=reserved.get(t.value,'LESSEQ')
	t.value = Node('LESSEQ', t.value, leaf = 1)
	return t

def t_STRING(t):
	r'\"[a-zA-Z0-9_]*\"'
	t.type=reserved.get(t.value,'STRING')
	t.value = Node('STRING', t.value, leaf = 1)
	return t

def t_NAME(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	t.type=reserved.get(t.value,'NAME')
	t.value = Node('NAME', t.value, leaf = 1)
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

def t_DIVIDES(t):
	r'\/'
	t.value = Node('DIVIDES', '/', leaf = 1)
	return t

def t_TIMES(t):
	r'\*'
	t.value = Node('TIMES', '*', leaf = 1)
	return t

def t_MODULUS(t):
	r'\%'
	t.value = Node('MODULUS', '%', leaf = 1)
	return t

def t_GREATERTHAN(t):
	r'\>'
	t.value = Node('GREATERTHAN', '>', leaf = 1)
	return t

def t_LESSTHAN(t):
	r'\<'
	t.value = Node('LESSTHAN', '<', leaf = 1)
	return t

def t_LSQUARE(t):
	r'\['
	t.value = Node('LSQUARE', '[', leaf = 1)
	return t

def t_RSQUARE(t):
	r'\]'
	t.value = Node('RSQUARE', ']', leaf = 1)
	return t

def t_LFPAREN(t):
	r'\{'
	t.value = Node('LFPAREN', '{', leaf = 1)
	return t

def t_RFPAREN(t):
	r'\}'
	t.value = Node('RFPAREN', '}', leaf = 1)
	return t

def t_SCOLON(t):
	r'\;'
	t.value = Node('SCOLON', ';', leaf = 1)
	return t

def p_start(t):
	'''start : declarationList''' 
	t[0] = Node("start", "start", t[1:], leaf = 0)


def p_declarationList(t):
	'''declarationList : declaration 
	| declarationList declaration''' 
	t[0] = Node("declarationList", "declarationList", t[1:], leaf = 0)


def p_declaration(t):
	'''declaration : varDeclaration 
	| funcdef''' 
	t[0] = Node("declaration", "declaration", t[1:], leaf = 0)


def p_varDeclaration(t):
	'''varDeclaration : typeSpecifier NAME SCOLON 
	| typeSpecifier NAME EQUALS NAME 
	| typeSpecifier NAME EQUALS NUMBER''' 
	t[0] = Node("varDeclaration", "varDeclaration", t[1:], leaf = 0)


def p_typeSpecifier(t):
	'''typeSpecifier : INT 
	| BOOL 
	| CHAR''' 
	t[0] = Node("typeSpecifier", "typeSpecifier", t[1:], leaf = 0)


def p_funcdef(t):
	'''funcdef : VOID NAME LPAREN parameters RPAREN LFPAREN funcbody RFPAREN
	| INT NAME LPAREN parameters RPAREN LFPAREN funcbody RFPAREN''' 
	t[0] = Node("funcdef", "funcdef", t[1:], leaf = 0)


def p_parameters(t):
	'''parameters : typeSpecifier NAME 
	| typeSpecifier NAME COMMA parameters 
	| empty''' 
	t[0] = Node("parameters", "parameters", t[1:], leaf = 0)


def p_funcbody(t):
	'''funcbody : statement 
	|  statement funcbody
	|  statement SCOLON funcbody''' 
	t[0] = Node("funcbody", "funcbody", t[1:], leaf = 0)


def p_blockitemlist(t):
	'''blockitemlist : blockitem
	| blockitemlist blockitem''' 
	t[0] = Node("blockitemlist", "blockitemlist", t[1:], leaf = 0)


def p_blockitem(t):
	'''blockitem : statement
	| varDeclaration''' 
	t[0] = Node("blockitem", "blockitem", t[1:], leaf = 0)


def p_cstatement(t):
	'''cstatement : LFPAREN RFPAREN
	| LFPAREN blockitemlist RFPAREN''' 
	t[0] = Node("cstatement", "cstatement", t[1:], leaf = 0)


def p_statement(t):
	'''statement : cstatement
	| selectionStmt
	| iterationStmt
	| NAME SCOLON
	| NAME statement
	| varDeclaration statement
	| expressionStmt SCOLON statement
	| expressionStmt SCOLON''' 
	t[0] = Node("statement", "statement", t[1:], leaf = 0)


def p_expressionStmt(t):
	'''expressionStmt : NAME PLUS NAME
	|  NAME MINUS NAME
	| NAME TIMES NAME
	| NAME DIVIDES NAME
	| NAME EQUALS NAME
	| NAME GREATERTHAN NAME
	| NAME LESSTHAN NAME
	| NAME GREATEQ NAME
	| NAME LESSEQ NAME
	| NAME EQUALS expressionStmt''' 
	t[0] = Node("expressionStmt", "expressionStmt", t[1:], leaf = 0)


def p_selectionStmt(t):
	'''selectionStmt : IF LPAREN simpleexpression RPAREN statement ELSE statement
	| IF LPAREN simpleexpression RPAREN statement''' 
	t[0] = Node("selectionStmt", "selectionStmt", t[1:], leaf = 0)


def p_iterationStmt(t):
	'''iterationStmt : WHILE LPAREN simpleexpression RPAREN statement 
	|  DO statement WHILE LPAREN simpleexpression RPAREN SCOLON
	| FOR LPAREN varDeclaration SCOLON forcondition SCOLON forchange RPAREN statement''' 
	t[0] = Node("iterationStmt", "iterationStmt", t[1:], leaf = 0)


def p_forcondition(t):
	'''forcondition : NAME EQUALS NAME
	| NAME GREATERTHAN NAME
	| NAME LESSTHAN NAME
	| NAME GREATEQ NAME
	| NAME LESSEQ NAME''' 
	t[0] = Node("forcondition", "forcondition", t[1:], leaf = 0)


def p_forchange(t):
	'''forchange : NAME PLUS PLUS
	| NAME MINUS MINUS
	| expressionStmt''' 
	t[0] = Node("forchange", "forchange", t[1:], leaf = 0)


def p_simpleexpression(t):
	'''simpleexpression : NAME''' 
	t[0] = Node("simpleexpression", "simpleexpression", t[1:], leaf = 0)


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
data = open('../programs/c/functions/input_programs/data.py',"r").read()

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
        print("")
        level += 1

    print(s)
    print("\n------------------------------\n")
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

print(root.__repr__())
# printYield(function, [0], "remove")
pgmLen = getPgmLen(root)
print(root.__repr__())


#### now we will try to introduce errors in the above syntax tree
pgms =  2
directory= '../programs/c/functions/output_programs/'
#directory = "../programs/python/functions/output_programs/"
fname = 'data.py'.split(".")[0]
extension = 'data.py'.split(".")[1]
positions = [i for i in range(1,pgmLen)]
for n_errors in range(1,4):
    print("Programs with "+str(n_errors)+" errors")
    for i in range(0,pgms):
        reqpos = []
        for j in range(0,n_errors):
            c = choice(positions)
            reqpos.append(c)
            positions.remove(c)
        positions = [i for i in range(1,pgmLen)]
        print("REMOVE:")
        pgm = printYield(root, reqpos, "remove")
        #f = open("pgm_" + str(pgms) + "_" + str(n_errors) + "remove." +extension, "w")
        f=open(directory+fname + "_" + str(n_errors) + "remove.py", "w")
        f.write(pgm)
        f.close()
        print("ADD:")
        pgm = printYield(root, reqpos, "add")
        f = open(directory+fname + "_" + str(n_errors) + "add." + extension, "w")
        f.write(pgm)
        f.close()
        print("REPLACE:")
        pgm = printYield(root, reqpos, "replace")
        f = open(directory+fname + "_" + str(n_errors)+ "replace." + extension , "w")
        f.write(pgm)
        f.close()
        print("")
x = open("temp.txt",'w')
x.write("dude what")
x.close()
