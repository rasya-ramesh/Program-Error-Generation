# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables -- all in one file.
# -----------------------------------------------------------------------------

# Function grammar:
# funcdef: 'def' NAME parameters  ':' func_body_suite
# parameters: '(' [typedargslist] ')'
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

reserved = {
    'def' : 'DEF',
    'void' : 'VOID',
    'int' : 'INT'
 }
tokens = [ 'COLON', 'COMMA','TAB',  'NAME', 'LPAREN','RPAREN', 'LFPAREN', 'RFPAREN', 'SCOLON'] + list(reserved.values())

# Tokens
# t_COMMA   = r'\,'
# t_COLON   = r'\:'
# t_LPAREN  = r'\('
# t_RPAREN  = r'\)'
# t_TAB     = r'\t'
#t_LFPAREN = r'\{'
#t_RFPAREN = r'\}'
#t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'
def t_LFPAREN(t):
  r'\{'
  t.value = Node("LFPAREN", '{', leaf = 1)
  return t

def t_RFPAREN(t):
  r'\}'
  t.value = Node("RFPAREN", '}', leaf = 1)
  return t

def t_SCOLON(t):
  r'\;'
  t.value = Node("SCOLON", ';', leaf = 1)
  return t

def t_COMMA(t):
  r'\,'
  t.value = Node("COMMA", ',', leaf = 1)
  return t

def t_COLON(t):
  r'\:'
  t.value = Node("COLON", ':', leaf = 1)
  return t

def t_LPAREN(t):
  r'\('
  t.value = Node("LPAREN", '(', leaf = 1)
  return t

def t_RPAREN(t):
  r'\)'
  t.value = Node("RPAREN", ')', leaf = 1)
  return t

def t_TAB(t):
  r'\t'
  t.value = Node("TAB", '\t', leaf = 1)
  return t


def t_NAME(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reserved.get(t.value,'NAME')    # Check for reserved words
     t.value = Node("NAME", t.value, leaf = 1)
     return t

# Ignored characters
t_ignore = " "#"\t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    # t.value = Node("NAME", t.value, leaf = 1)

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
tlist=[]
stmts=[]
def p_funcdef(t):
    '''funcdef : VOID NAME LPAREN parameters RPAREN LFPAREN funcbody RFPAREN
               | INT NAME LPAREN parameters RPAREN LFPAREN funcbody RFPAREN'''
    print("function name:",t[2])
    t[0]=Node("function", "function", [t[1], t[2], t[3], t[4], t[5], t[6], t[7], t[8]], leaf = 0)

def p_parameters(t):
    '''parameters : NAME
                  | NAME COMMA parameters
                  | empty'''
    if(t[1]!=None):
        print("arg: ",t[1])
        tlist.append(t[1])

    t[0]=Node("parameters", "parameters", tlist, leaf = 0)

def p_funcbody(t):
    '''funcbody :  statement SCOLON
                |  statement SCOLON funcbody'''        #how to do newline?
    # print("BODY: " ," ".join(func_stmt))
    if(t[2]!=None):
        stmts.append(t[2])
    t[0]=Node("fbody", "fbody", stmts, leaf = 0)


def p_statement(t):
    '''statement : NAME
                 | NAME statement'''            #have to change NAME with expressions/statements.
    # func_stmt.insert(0, t[1] )
    t[0]=Node("stmts", "stmts", [t[1]], leaf = 0)

def p_error(t):
    print("Syntax error at '%s'" % t.value)


import ply.yacc as yacc
yacc.yacc()
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
data='''void foo(a,b){some;return a;}'''
#print(data)
print("meh")

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
    while len(s2) != 0:
      val = s2.pop()
      print("\t"*level + val.value, end = " ")

      colon = Node("COLON",":", leaf = 1)
      if val == colon:
        print("")
        level += 1

    print("\n------------------------------\n")

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

# printYield(function, [0], "remove")
pgmLen = getPgmLen(root)
# print(function.__repr__())


#### now we will try to introduce errors in the above syntax tree
print("")
# printYield(function, [7])
pgms =  2
print("Removal of nodes: ")
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
        printYield(root, reqpos, "remove")
        print("")
    
print("Addition of nodes: ")
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
        printYield(root, reqpos, "add")
        print("")

print("Replacing of nodes: ")
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
        printYield(root, reqpos, "replace")
        print("")