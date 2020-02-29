from random import choice 
import sys

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

    'void' : 'VOID',
    'int' : 'INT',
    'bool': 'BOOL',
    'char' : 'CHAR',
    'else' : 'ELSE',
    'if'   : 'IF',
    'while' : 'WHILE'
 }
tokens = [ 'COLON', 'COMMA','TAB',  'NAME', 'LPAREN','RPAREN', 'LFPAREN', 'RFPAREN', 'SCOLON', 'TIMES','DIVIDES', 'PLUS', 'MINUS', 'EQUALS'] + list(reserved.values())

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

def t_PLUS(t):
  r'\+'
  t.value = Node("PLUS", '+', leaf = 1)
  return t

def t_MINUS(t):
  r'\-'
  t.value = Node("MINUS", '-', leaf = 1)
  return t

def t_TIMES(t):
  r'\*'
  t.value = Node("TIMES", '*', leaf = 1)
  return t

def t_DIVIDES(t):
  r'\/'
  t.value = Node("DIVIDES", '/', leaf = 1)
  return t

def t_EQUALS(t):
  r'\='
  t.value = Node("EQUALS", '=', leaf = 1)
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
start= 'start'
tlist=[]
stmts=[]
slist=[]
stoutside_list=[]
eoutside_list=[]
seoutside_list=[]

def p_start(t):
	'''start : declarationList'''
	t[0]=Node("start","start",[t[1]],leaf=0)
def p_declarationList(t):
	'''declarationList : declaration 
					   | declarationList declaration'''
	t[0]=Node("declarationList","declarationList",[t[1]],leaf=0)
def p_declaration(t):
	'''declaration : varDeclaration 
				   | funcdef'''
	t[0]=Node("declaration","declaration",[t[1]],leaf=0)
def p_varDeclaration(t):
	'''varDeclaration : typeSpecifier NAME SCOLON'''
	print("name: ",t[2])
	t[0]=Node("varDeclaration","varDeclaration",[t[1],t[2],t[3]],leaf=0)
def p_typeSpecifier(t):
	'''typeSpecifier : INT 
					 | BOOL 
					 | CHAR'''
	t[0]=Node("typeSpecifier","typeSpecifier",[t[1]],leaf=0)
def p_funcdef(t):
    '''funcdef : VOID NAME LPAREN parameters RPAREN LFPAREN funcbody RFPAREN
               | INT NAME LPAREN parameters RPAREN LFPAREN funcbody RFPAREN'''
    print("function name:",t[2])
    t[0]=Node("function", "function", t[1:], leaf = 0)

def p_parameters(t):
    '''parameters : typeSpecifier NAME
                  | typeSpecifier NAME COMMA parameters
                  | empty'''
    if(t[1]!=None):
        print("arg: ",t[1])
        tlist.append(t[1])
        print("tlist",tlist)

    t[0]=Node("parameters", "parameters", t[1:], leaf = 0)

def p_funcbody(t):
    '''funcbody :  statement 
    			|  statement funcbody
                |  statement SCOLON funcbody'''        
    # print("BODY: " ," ".join(func_stmt))
    #print("stjsbdfjkdav",t[1])
    
    t[0]=Node("fbody", "fbody", t[1:], leaf = 0)


def p_statement(t):
    '''statement : selectionStmt
                 | iterationStmt
    			       | NAME SCOLON
                 | NAME statement
                 | varDeclaration statement
                 | expressionStmt SCOLON statement'''            
    
    
    t[0]=Node("statement", "statement", t[1:], leaf = 0)


def p_expressionStmt(t):
  '''expressionStmt : NAME PLUS NAME
                      | NAME MINUS NAME
                      | NAME TIMES NAME
                      | NAME DIVIDES NAME'''
  t[0]=Node("expressionStmt", "expressionStmt", t[1:], leaf = 0) 

def p_expressionStmt(t):
	'''expressionStmt : NAME PLUS NAME
                  	  | NAME MINUS NAME
                      | NAME TIMES NAME
                      | NAME DIVIDES NAME'''
	t[0]=Node("expressionStmt", "expressionStmt", t[1:], leaf = 0)     
'''def p_statement(t):
	statement : expressionStmt 
				 | compoundStmt 
				 | selectionStmt 
				 | iterationStmt 
				 | returnStmt
				 | breakStmt
'''
def p_selectionStmt(t):
  '''selectionStmt : IF LPAREN simpleexpression RPAREN LFPAREN statement RFPAREN elseif
                   | IF LPAREN simpleexpression RPAREN LFPAREN statement RFPAREN elseif ELSE LFPAREN statement RFPAREN'''

  t[0]=Node("selectionStmt", "selectionStmt", t[1:], leaf = 0)

	  


def p_elseif(t):
	
	''' elseif : ELSE IF LPAREN simpleexpression RPAREN LFPAREN statement RFPAREN 
			       | empty '''
	
	
	t[0]=Node("elseif", "elseif", t[1:], leaf = 0)

def iterationStmt(t):
  '''iterationStmt: WHILE LPAREN simpleexpression RPAREN LFPAREN statement RFPAREN'''
  t[0]=Node("iterationStmt", "iterationStmt", t[1:], leaf = 0)

def p_simpleexpression(t):
	'''simpleexpression : NAME'''
	t[0]=Node("simp", "simp", [t[1]], leaf = 0)

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
#data='''void foo(int a,int b){ if(a){a;}else{a;}int a;some;}'''
#print(data)
#print("meh")

data = open("data.py", "r")
data = data.read()

root = yacc.parse(data)
print(root.__repr__)
number=0
def printYield(root, reqpos, type):
    # Stack to store all the nodes  
    # of tree  
    s1 = []  
    global number
    number=number+1
    # Stack to store all the 
    # leaf nodes  
    s2 = []  
    message=""
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
            if type == "remove" and n in reqpos:
              message=message+"\n"+curr.type + "missing";

            if type == "remove" and n not in reqpos:
                s2.append(curr)

                
            if type == "add":
                s2.append(curr)
                if n in reqpos:
                    temp = Node("dummy", "errnode", leaf = 1)
                    s2.append(temp)
                    message=message+"\n"+"Unknown errnode found "
            if type == "replace":
                if n in reqpos:
                    temp = Node("dummy", "@@@", leaf = 1)
                    s2.append(temp)
                    message=message+"\n"+"Unknown @@@ found"
                else:
                    s2.append(curr)
    f=open('outputmeg'+str(number)+'.txt', 'w')
    # Print all the leaf nodes  
    level = 0
    while len(s2) != 0:
      val = s2.pop()
      s="\t"*level + val.value + " "
      f.write(s)
      colon = Node("COLON",":", leaf = 1)
      if val == colon:
        f.write("")
        level += 1
    print("\n")
    print(number)
    #original = sys.stdout
    
    #print('This is your redirected text:')
    f.write(message)
    #sys.stdout = original
    #print("\n------------------------------\n")

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