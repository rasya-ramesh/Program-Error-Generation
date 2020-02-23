from random import choice 
import sys
import ply.lex as lex
from ply.lex import TOKEN
import tokenize

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



tokens=[]
keywordlist = [
    'and', 'break', 'class', 'continue', 'def', 
    'del', 'elif', 'else', 'except', 'exec', 'finally', 'for', 
    'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 
    'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 
    'with', 'yield'
    ]

RESERVED = {}
for keyword in keywordlist:
  name = keyword.upper()
  RESERVED[keyword] = name
  tokens.append(name)

tokens = tuple(tokens) + (
    'EQEQUAL','NOTEQUAL','LESSEQUAL','GREATEREQUAL','PLUSEQUAL','MINEQUAL','STAREQUAL','SLASHEQUAL',
    'SLASHSLASH','SLASHSLASHEQUAL',
    'COLON','COMMA','SEMI','PLUS','MINUS','STAR','SLASH', 'LESS',
    'GREATER','EQUAL','DOT','PERCENT', 'TILDE',

      'LPAREN', 'RPAREN',
      'LBRACE', 'RBRACE',
      'LSQB', 'RSQB',
    'NEWLINE',
    'NUMBER',
    'INDENT', 'DEDENT',
    'NAME','WS',
    'ENDMARKER'
  )

# Regular expression rules for simple tokens
def newToken(newType, lineno):
  tok = lex.LexToken()
  tok.type = newType
  tok.value = None
  tok.lineno = lineno
  tok.lexpos = -100
  return tok

def t_DEF(t):
  r"def"
  t.type = RESERVED.get(t.value, "DEF")
  t.value = Node("DEF", t.value, leaf = 1)
  return t

def t_COLON(t):
  r'\:'
  t.value = Node("COLON", ':', leaf = 1)
  return t

def t_COMMA(t):
  r'\,'
  t.value = Node("COMMA", ',', leaf = 1)
  return t

def t_SEMI(t):
  r'\;'
  t.value = Node("SEMI", ';', leaf = 1)
  return t

def t_PLUS(t):
  r'\+'
  t.value = Node("PLUS", '+', leaf = 1)
  return t

def t_MINUS(t):
  r'-'
  t.value = Node("MINUS", '-', leaf = 1)
  return t

def t_STAR(t):
  r'\*'
  t.value = Node("STAR", '*', leaf = 1)
  return t

def t_SLASH(t):
  r'/'
  t.value = Node("SLASH", '/', leaf = 1)
  return t

def t_LESS(t):
  r'<'
  t.value = Node("LESS", '<', leaf = 1)
  return t

def t_GREATER(t):
  r'>'
  t.value = Node("GREATER", '>', leaf = 1)
  return t

def t_EQUAL(t):
  r'='
  t.value = Node("EQUAL", '=', leaf = 1)
  return t

def t_PERCENT(t):
  r'%'
  t.value = Node("PERCENT", '%', leaf = 1)
  return t

def t_TILDE(t):
  r'~'
  t.value = Node("TILDE", '~', leaf = 1)
  return t

def t_SLASHSLASHEQUAL(t):
  r'//='
  t.value = Node("SLASHSLASHEQUAL", '//=', leaf = 1)
  return t


def t_STAREQUAL(t):
  r'\*='
  t.value = Node("STAREQUAL", '*=', leaf = 1)
  return t

def t_EQEQUAL(t):
  r'=='
  t.value = Node("EQEQUAL", '==', leaf = 1)
  return t

def t_NOTEQUAL(t):
  r'!='
  t.value = Node("NOTEQUAL", '!=', leaf = 1)
  return t

def t_LESSEQUAL(t):
  r'<='
  t.value = Node("LESSEQUAL", '<=', leaf = 1)
  return t

def t_GREATEREQUAL(t):
  r'>='
  t.value = Node("GREATEREQUAL", '>=', leaf = 1)
  return t

def t_PLUSEQUAL(t):
  r'\+='
  t.value = Node("PLUSEQUAL", '+=', leaf = 1)
  return t

def t_MINEQUAL(t):
  r'-='
  t.value = Node("MINEQUAL", '-=', leaf = 1)
  return t

def t_LPAREN(t):
  r"\("
  t.value = Node("LPAREN", '(', leaf = 1)
  return t

def t_RPAREN(t):
  r"\)"
  t.value = Node("RPAREN", ')', leaf = 1)
  return t

#ignore comments in source code
def t_comment(t):
  r"[ ]*\043[^\n]*"
  pass

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)  
    t.value = Node("NUMBER", t.value, leaf = 1)  
    return t


def t_continueLine(t):
  r'\\(\n)+'

def t_newline(t):
    r'\n+'
    print("NEWLINE!")
    t.lexer.lineno += len(t.value)
    t.type = "NEWLINE"

    t.value = Node("NEWLINE", 'NEWLINE', leaf = 1)
    return t

def t_NAME(t):
  r"[a-zA-Z_][a-zA-Z0-9_]*"
  t.type = RESERVED.get(t.value, "NAME")
  t.value = Node("NAME", t.value, leaf = 1)
  return t

# Error handling rule
def t_error(t):
    message = "\n# ERROR: Illegal character '%s' in %s at line %d" % (t.value[0], t.value, t.lineno)
    # errorList.append(message)
    t.lexer.skip(1)

# REFERENCE: https://docs.python.org/2/reference/lexical_analysis.html
# WHITESPACE
# def t_WS(t):
#   r" [ \t\f]+ "
#   value = t.value
#   value = value.rsplit("\f", 1)[-1]
#   pos = 0
#   while True:
#     pos = value.find("\t")
#     if pos == -1:
#       break
#     n = 8 - (pos % 8)               # Convert each \t to 8 spaces (Python Documentation)
#     value = value[:pos] + " "*n + value[pos+1:]
#   t.value = value
#   # if t.lexer.atLineStart and t.lexer.parenthesisCount == 0:
#   return t

def INDENT(lineno):
  return newToken("INDENT", lineno)

def DEDENT(lineno):
  return newToken("DEDENT",lineno)


import ply.lex as lex
lexer = lex.lex()


start= 'single_input'


#single_input: NEWLINE | simple_stmt | compound_stmt NEWLINE
def p_single_input(t):
  '''single_input     : NEWLINE
                      | simple_stmt
                      | compound_stmt NEWLINE
                      | '''
  t[0]=Node("single_input", "start", t[1:], leaf = 0)
  print(t[1:])


#stmt: simple_stmt | compound_stmt 
def p_stmt(t):
  '''stmt   : simple_stmt
            | compound_stmt'''
  t[0]=Node("stmt", "stmt", t[1:], leaf = 0)


#simple_stmt: small_stmt (';' small_stmt)* [';'] NEWLINE
def p_simple_stmt(t):
  '''simple_stmt  : small_stmts NEWLINE
                  | small_stmts SEMI NEWLINE'''
  t[0] = Node("simple_stmt", "simple_stmt", t[1:], leaf = 0)

def p_small_stmts(t):
  """small_stmts  : small_stmts SEMI small_stmt
                  | small_stmt
  """
  t[0] = Node("small_stmts", "small_stmts", t[1:], leaf = 0)

#small_stmt: testlist (augassign testlist | [('=' testlist) * )      ###########
def p_small_stmt(t):
  '''small_stmt  : testlist augassign testlist
                | testlist eqtestlist'''
  t[0] = Node("small_stmt", "small_stmt", t[1:], leaf = 0)

def p_eqtestlist(t):
  '''eqtestlist   :
                  | eqtestlist EQUAL testlist'''
  t[0] = Node("eqtestlist", "eqtestlist", t[1:], leaf = 0)

# testlist: test (',' test)* [',']
def p_testlist(t):
  '''testlist     : test
                  | test COMMA
                  | test COMMA testlist'''
  t[0] = Node("testlist", "testlist", t[1:], leaf = 0)

# test: or_test ['if' or_test 'else' test]
def p_test(t):
  '''test     : or_test
              | or_test IF or_test ELSE test'''

  t[0] = Node("test", "test", t[1:], leaf = 0)

# or_test: and_test ('or' and_test)*
def p_or_test(t):
  """or_test  : and_test ortestlist"""
  t[0] = Node("ortest", "ortest", t[1:], leaf = 0)

# our new symbol
def p_ortestlist(t):
  '''ortestlist   : 
                  | OR and_test ortestlist'''
  t[0] = Node("ortestlist", "ortestlist", t[1:], leaf = 0)

# and_test: not_test ('and' not_test)*
def p_and_test(t):
  '''and_test     : not_test andtestlist'''
  t[0] = Node("andtest", "andtest", t[1:], leaf = 0)

#our new symbol
def p_andtestlist(t):
  """andtestlist  : 
                  | AND not_test andtestlist"""
  t[0] = Node("andtestlist", "andtestlist", t[1:], leaf = 0)

# not_test: 'not' not_test | comparison
def p_not_test(t):
  """not_test     : NOT not_test
                  | comparison"""
  t[0] = Node("nottest", "nottest", t[1:], leaf = 0)

# comparison: expr (comp_op expr)*
def p_comparision(t):
  """comparison   : arith_expr compexprlist"""
  t[0] = Node("comparison", "comparison", t[1:], leaf = 0)

# our new symbol
def p_compexprlist(t):
  """compexprlist     : 
                      | comp_op arith_expr compexprlist"""
  t[0] = Node("compexprlist", "compexprlist", t[1:], leaf = 0)

# comp_op: '<'|'>'|'=='|'>='|'<='|'!='|'in'|'not' 'in'|'is'|'is' 'not'
def p_comp_op(t):
  """comp_op  : LESS
              | GREATER
              | EQEQUAL
              | GREATEREQUAL
              | LESSEQUAL
              | NOTEQUAL
              | IN
              | NOT IN
              | IS
              | IS NOT"""
  t[0] = Node("comp_op", "comp_op", t[1:], leaf = 0)

# augassign: ('+=' | '-=' | '*=' | '/=' | '%=' | '**=' | '//=')
def p_augassign(t):
  '''augassign  : PLUSEQUAL 
                | MINEQUAL 
                | STAREQUAL 
                | SLASHEQUAL 
                | SLASHSLASHEQUAL '''
  t[0] = Node("augassign", "augassign", t[1:], leaf = 0)


# arith_expr: term (('+'|'-') term)*
def p_arith_expr(t):
  '''arith_expr   :   term termlist'''
  t[0] = Node("arith_expr", "arith_expr", t[1:], leaf = 0)

# our new symbol
def p_termlist(t):
  '''termlist     : 
                  | PLUS term termlist
                  | MINUS term termlist'''
  t[0] = Node("termlist", "termlist", t[1:], leaf = 0)

# term: factor (('*'|'/'|'%'|'//') factor)*
def p_term(t):
  """term :   factor factorlist"""
  t[0] = Node("term", "term", t[1:], leaf = 0)

# our new symbol
def p_factorlist(t):
  """factorlist   : 
                  | STAR factor factorlist
                  | SLASH factor factorlist
                  | PERCENT factor factorlist
                  | SLASHSLASH factor factorlist"""
  t[0] = Node("factorlist", "factorlist", t[1:], leaf = 0)

# factor: ('+'|'-'|'~') factor | power
def p_factor(t):
  '''factor   : NAME
              | NUMBER'''
  t[0] = Node("factor", t[1], leaf = 0)


# compound_stmt: if_stmt | while_stmt | for_stmt | funcdef | classdef 
def p_compound_stmt(t):
  '''compound_stmt  : if_stmt
                    | funcdef'''
  t[0] = Node("compound_stmt", "compound_stmt", t[1:], leaf = 0)
  

# if_stmt: 'if' test ':' suite ('elif' test ':' suite)* ['else' ':' suite]
def p_if_stmt(t):
  '''if_stmt  : IF test COLON suite elif_list
              | IF test COLON suite elif_list ELSE COLON suite'''
  t[0] = Node("if_stmt", "if_stmt", t[1:], leaf = 0)

# our new symbol
def p_elif_list(t):
  """elif_list  : 
                | ELIF test COLON suite elif_list"""
  t[0] = Node("elif_stmt", "elif_stmt", t[1:], leaf = 0)

# suite: simple_stmt | NEWLINE INDENT stmt+ DEDENT
def p_suite(t):
  """suite    : simple_stmt
              | NEWLINE INDENT stmts DEDENT"""
  t[0] = Node("suite", "suite", t[1:], leaf = 0)

def p_stmts(t):
  """stmts    : stmts stmt
              | stmt"""
  t[0] = Node("stmts", "stmts", t[1:], leaf = 0)

# funcdef: [decorators] 'def' NAME parameters ':' suite
def p_funcdef(t):
  '''funcdef : DEF NAME parameters COLON suite'''
  t[0] = Node("funcdef", "funcdef", t[1:], leaf = 0)

# parameters: '(' [varargslist] ')'
def p_parameters(t):
  """parameters : LPAREN varargslist RPAREN"""
  t[0] = Node("parameters", "parameters", t[1:], leaf = 0)

#varargslist: ( | fpdef ['=' test] (',' fpdef ['=' test])* [',']) 

def p_varargslist(t):
  """varargslist  :
                  | fpdef EQUAL test fpdeflist COMMA
                  | fpdef EQUAL test fpdeflist
                  | fpdef fpdeflist COMMA
                  | fpdef fpdeflist
  """
  t[0] = Node("varargslist", "varargslist", t[1:], leaf = 0)

def p_fpdeflist(t):
  """fpdeflist    :
                  | fpdeflist COMMA fpdef
                  | fpdeflist COMMA fpdef EQUAL test
  """
  t[0] = Node("fpdeflist", "fpdeflist", t[1:], leaf = 0)

# fpdef: NAME | '(' fplist ')'
def p_fpdef(t):
  """fpdef    : NAME 
              | LPAREN fplist RPAREN
  """
  t[0] = Node("fpdef", "fpdef", t[1:], leaf = 0)

# fplist: fpdef (',' fpdef)* [',']
def p_fplist(t):
  """fplist   : fpdef fplist1 COMMA
              | fpdef fplist1 
  """
  t[0] = Node("fplist", "fplist", t[1:], leaf = 0)

# our temp symbol
def p_fplist1(t):
  """fplist1  :
              | fplist1 COMMA fpdef
  """
  t[0] = Node("fplist1", "fplist1", t[1:], leaf = 0)


import ply.yacc as yacc
yacc.yacc()


data = open("data.py", "r")
data = data.read()
print(data)
print("meh")

import pdb; pdb.set_trace()
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

# printYield(function, [0], "remove")
# pgmLen = getPgmLen(root)
print(root.__repr__())


# #### now we will try to introduce errors in the above syntax tree
# print("")
# # printYield(function, [7])
# pgms =  2
# positions = [i for i in range(1,pgmLen)]
# for n_errors in range(1,4):
#     print("Programs with "+str(n_errors)+" errors")
#     for i in range(0,pgms):
#         reqpos = []    
#         for j in range(0,n_errors):
#             c = choice(positions)
#             reqpos.append(c)
#             positions.remove(c)
#         positions = [i for i in range(1,pgmLen)]
#         print("REMOVE:\n")
#         pgm = printYield(root, reqpos, "remove")
#         f = open("pgm_" + str(pgms) + "_" + str(n_errors) + "remove.py", "w")
#         f.write(pgm)
#         f.close()
#         print("ADD:\n")
#         pgm = printYield(root, reqpos, "add")
#         f = open("pgm_" + str(pgms) + "_" + str(n_errors) + "add.py", "w")
#         f.write(pgm)
#         f.close()
#         print("REPLACE:\n")
#         pgm = printYield(root, reqpos, "replace")
#         f = open("pgm_" + str(pgms) + "_" + str(n_errors) + "replace.py", "w")
#         f.write(pgm)
#         f.close()
#         print("")
    
# print("Addition of nodes: ")
# positions = [i for i in range(1,pgmLen)]
# for n_errors in range(1,4):
#     print("Programs with "+str(n_errors)+" errors")
#     for i in range(0,pgms):
#         reqpos = []    
#         for j in range(0,n_errors):
#             c = choice(positions)
#             reqpos.append(c)
#             positions.remove(c)

#         positions = [i for i in range(1,pgmLen)]
#         printYield(root, reqpos, "add")
#         print("")

# print("Replacing of nodes: ")
# positions = [i for i in range(1,pgmLen)]
# for n_errors in range(1,4):
#     print("Programs with "+str(n_errors)+" errors")
#     for i in range(0,pgms):
#         reqpos = []    
#         for j in range(0,n_errors):
#             c = choice(positions)
#             reqpos.append(c)
#             positions.remove(c)

#         positions = [i for i in range(1,pgmLen)]
#         printYield(root, reqpos, "replace")
#         print("")

