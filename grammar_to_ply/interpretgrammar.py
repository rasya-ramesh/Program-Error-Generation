
# Run command:
# python3 interpretgrammar.py -g grammars/python_grammar.txt -l python -i temp.py  -t functions
# output in: programs/python/functions/output_programs

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-g", required=True, help="This is the grammar file")
parser.add_argument("-l", required=True, help="Language")
parser.add_argument("-i", required=True, help="The syntactically correct input program segment")
parser.add_argument("-t", required=True, help="Category of program (construct)")

args = parser.parse_args()
grammar_file = args.g
l = args.l
t = args.t
i = args.i
input_file = '../programs/' + l + '/' + t + '/input_programs/' + i
output_directory = '../programs/' + l + '/' + t + '/output_programs/'
#print(input_file)
codesegment = open(input_file,"r").read()

print("\n\nGRAMMAR FILE : ", grammar_file)
print( "_"*80, "\n")
f = open(grammar_file, "r")
l = f.readlines()
lines=[]
for line in l:
    lines.append(line.rstrip('\n'))

#dictionary of lvalue and rvalues in grammar
dict= {}
for line in lines:
    print(line)
    lr = line.split(":=")
    print(lr)
    rule_right = lr[1].strip()
    rule_right = rule_right.replace("|","\n\t|")
    dict[lr[0].strip()] = rule_right

#reserved keywords:
reserved={}
reserved_words = dict['reserved'].split(" ")
for word in reserved_words:
    word=word.strip()
    if( word != "" ):
        reserved[word]=word.upper()
print("RESERVED WORDS: ",reserved)
#token values:
tokens = list(reserved.values())
for token in dict['tokens'].split(" "):
    t=token.split('=')
    tokens_temp = {}
    tokens_temp[t[0]]=t[1]
    tokens.append(t[0].split("_")[1])
    locals().update(tokens_temp)
print("TOKENS GENERATED: ", tokens,"\n\n")
#start production
start_dict={}
start_dict['start'] = dict['start']
locals().update(start_dict)


tokens_done = []

action_funcs = ""
function =""
for line in dict:
    if line.startswith('t_'):
        left_production = line[2:]
        function = "\ndef "+line+"(t):\n\tr\'" +dict[line]+ "\'\n\tt.type=reserved.get(t.value,\'"+ left_production +"\')"
        function += "\n\tt.value = Node(\'" + left_production + "\', t.value, leaf = 1)\n\treturn t"
        print(function)
        action_funcs =action_funcs + function + "\n"
        tokens_done.append(line)

print(dict['tokens'])
list_of_tokens = dict['tokens'].split(" ")

for token in list_of_tokens:
    fname = token.split("=", 1)[0]
    if fname not in tokens_done:
        character = token.split("=", 1)[1]
        ch = character[1:2]
        if ch=='t' or ch==' n ':
            function = "\ndef " + fname + "(t):\n\tr\'" + token.split("=",1)[1]  + "\'\n\tt.value = Node(\'" + fname[2:] + "\', \'\\"+ch+"\', leaf = 1)\n\treturn t"
        elif ch =='=':
            #function = "\ndef " + fname + "(t):\n\tr\'=" + "\'\n\tt.value = Node(\'" + fname[2:] + "\', \'=" +  "\', leaf = 1)\n\treturn t"
            function = "def t_EQUALS(t):\n\tr\'\=\'\n\tt.value = Node('EQUALS', '=', leaf = 1)\n\treturn t"
        else:
            function = "\ndef " + fname + "(t):\n\tr\'" + token.split("=",1)[1]  + "\'\n\tt.value = Node(\'" + fname[2:] + "\', \'" + character[1:] + "\', leaf = 1)\n\treturn t"
        action_funcs =action_funcs + function + "\n"

# exec(function)

# def t_NAME(t):
#      r'[a-zA-Z_][a-zA-Z_0-9]*'
#      t.type = reserved.get(t.value,'NAME')    # Check for reserved words
#      return t
# #

#defining the actions:
for line in dict:
    if (line not in ['reserved','tokens']) and (not line.startswith('t_')):
        function = "\ndef p_"+line+"(t):\n\t\'\'\'"+line+ " : " +dict[line] + "\'\'\' "
        tree_generation = '\n\tt[0] = Node(\"' + line + '\", \"' + line + '\", t[1:], leaf = 0)\n'
        function += tree_generation
        action_funcs = action_funcs + function + "\n"
print("_"*80)
print("ACTION FUNCTIONS GENERATED: ", action_funcs,"\n\n")
def p_error(t):
    print("Syntax error at '%s'" % t.value)


# codesegment='''def foo(a,b,x):
# \tsome_statement
# \treturn a'''
print( "_"*80)
print("\n\nCODE SEGMENT BEING PARSED:\n")

print(codesegment)
print("_"*80)
execute_code = action_funcs +'''\n\nimport ply.yacc as yacc
parser = yacc.yacc()
yacc.parse(codesegment)\n\n'''

ply_file_str = '''from random import choice

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
    ret = "\t"*level+repr(self.value)+"\\n"
    for child in self.children:
      ret += child.__repr__(level+1)
    return ret

'''

rest_of_ply_code = '''
# Ignored characters
t_ignore = " "
def t_newline(t):
    r'\\n+'
    t.lexer.lineno += t.value.count("\\n")

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
#data = input('codesegment : \\n')
#data.replace('\\n','')'''

rest_of_ply_code += '''\ndata = open(\'{0}\',"r").read()

root = yacc.parse(data)'''.format(input_file)


rest_of_ply_code += '''\ndef printYield(root, reqpos, type):
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
      s = s+'\t' * level + val.value + " "
      # print(s)
      colon = Node("COLON",":", leaf = 1)
      if val == colon:
        print("")
        level += 1

    print(s)
    print("\\n------------------------------\\n")
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
directory= \'{0}\'
#directory = "../programs/python/functions/output_programs/"
fname = \'{1}\'.split(".")[0]
extension = \'{1}\'.split(".")[1]
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
'''.format(output_directory, i)
ply_file_str += "reserved = " + str(reserved) + "\n" + "tokens = " + str(tokens) + "\n" + action_funcs + rest_of_ply_code

f = open("ply_program.py", "w")
f.write(ply_file_str)
f.close()

# exec(execute_code)
#exec(open('ply_program.py').read())
import os
import subprocess
os.system("/usr/bin/python3 ply_program.py>>ply.out")
#subprocess.call(['/usr/bin/python3', os.getcwd() + '/ply_program.py'])
