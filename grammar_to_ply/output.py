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
    ret = "\t"*level+repr(self.value)+"\n"
    for child in self.children:
      ret += child.__repr__(level+1)
    return ret

reserved = {'def': 'DEF', 'if': 'IF'}
tokens = ['DEF', 'IF', 'COMMA', 'COLON', 'LPAREN', 'RPAREN', 'TAB', 'NAME']

def t_NAME(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	t.type=reserved.get(t.value,'NAME')
	t.value = Node('NAME', t.value, leaf = 1)
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
	t.value = Node('TAB', 't', leaf = 1)
	return t

def p_start(t):
	'''start : funcdef 
	| if_stmt''' 
	t[0] = Node("start", "start", t[1:], leaf = 0)


def p_if_stmt(t):
	'''if_stmt : IF statement COLON funcbody''' 
	t[0] = Node("if_stmt", "if_stmt", t[1:], leaf = 0)


def p_funcdef(t):
	'''funcdef : DEF NAME LPAREN parameters RPAREN COLON funcbody''' 
	t[0] = Node("funcdef", "funcdef", t[1:], leaf = 0)


def p_parameters(t):
	'''parameters : NAME 
	| NAME COMMA parameters 
	| empty''' 
	t[0] = Node("parameters", "parameters", t[1:], leaf = 0)


def p_funcbody(t):
	'''funcbody : TAB statement  
	|  TAB statement funcbody''' 
	t[0] = Node("funcbody", "funcbody", t[1:], leaf = 0)


def p_statement(t):
	'''statement : NAME   
	| NAME statement''' 
	t[0] = Node("statement", "statement", t[1:], leaf = 0)



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
data = open('../programs/python/functions/input_programs/functionfoo.py',"r").read()

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
      # s = print("\t"*level + val.value, end = " ")
      s = s+"\t" * level + val.value + " "
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


# #### now we will try to introduce errors in the above syntax tree
print("")
# printYield(function, [7])
pgms =  2
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
        print("REMOVE:\n")
        pgm = printYield(root, reqpos, "remove")
        f = open("pgm_" + str(pgms) + "_" + str(n_errors) + "remove.py", "w")
        f.write(pgm)
        f.close()
        print("ADD:\n")
        pgm = printYield(root, reqpos, "add")
        f = open("pgm_" + str(pgms) + "_" + str(n_errors) + "add.py", "w")
        f.write(pgm)
        f.close()
        print("REPLACE:\n")
        pgm = printYield(root, reqpos, "replace")
        f = open("pgm_" + str(pgms) + "_" + str(n_errors) + "replace.py", "w")
        f.write(pgm)
        f.close()
        print("")
