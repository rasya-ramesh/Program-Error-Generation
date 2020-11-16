
# Run command:
# python3 interpretgrammar.py -g grammars/new_python_grammar.txt -l python -i factorial.py  -t toy_programs -p 20
# output in: programs/python/functions/output_programs

import argparse
import itertools
import random
import os
parser = argparse.ArgumentParser()
parser.add_argument("-g", required=True, help="This is the grammar file")
parser.add_argument("-l", required=True, help="Language")
parser.add_argument("-i", required=True, help="The syntactically correct input program segment")
parser.add_argument("-t", required=True, help="Category of program (construct)")
parser.add_argument("-p", required=True, help="Percentage of errors")


args = parser.parse_args()
grammar_file = args.g
l = args.l
t = args.t
i = args.i
perc_str = args.p
input_file = 'programs/' + l + '/' + t + '/input_programs/' + i
output_directory = 'programs/' + l + '/' + t + '/output_programs/'
if not os.path.exists(output_directory):
    os.mkdir(output_directory)
    os.mkdir(output_directory + "/errors")
codesegment = open(input_file,"r").read()
perc=int(perc_str)
f = open(grammar_file, "r")
l = f.readlines()
lines=[]
for line in l:
    lines.append(line.rstrip('\n'))

#dictionary of lvalue and rvalues in grammar
dict= {}
for line in lines:
    lr = line.split(":=")
    rule_right = lr[1].strip()
    rule_left = lr[0]
    if "reserved" not in rule_left and "token" not in rule_left and "t_" not in rule_left[0:2] and "operator" not in rule_left and "symbol" not in rule_left and "ignore" not in rule_left:
        rule_right = rule_right.replace("|","\n\t|")
    dict[lr[0].strip()] = rule_right

#reserved keywords:
reserved={}
reserved_words = dict['reserved'].split(" ")
for word in reserved_words:
    word=word.strip()
    if( word != "" ):
        reserved[word]=word.upper()

selection={}
selection_words = dict['selection'].split(" ")
for word in selection_words:
    word=word.strip()
    if( word != "" ):
        selection[word]=word.upper()
loop={}
loop_words = dict['loop'].split(" ")
for word in loop_words:
    word=word.strip()
    if( word != "" ):
        loop[word]=word.upper()

list_of_tokens = []
final_lists = {}
#token values:
tokens = list(reserved.values())
for key in dict.keys():
    if key == "start" or "t_" in key:
        break
    if key != "reserved":
        list_of_tokens.extend(dict[key].split(" "))
        final_lists[key] = []
    for token in dict[key].split(" "):
        if key == 'reserved':
            break
        if key == 'selection':
            break
        if key == 'loop':
            break
        t=token.split('=',1)
        tokens_temp = {}
        tokens_temp[t[0]]=t[1]
        tokens.append(t[0].split("_",1)[1])
        final_lists[key].append(t[0].split("_",1)[1])
        locals().update(tokens_temp)

#start production
start_dict={}
start_dict['start'] = dict['start']
locals().update(start_dict)

tokens_done = []

action_funcs = ""
function =""
for line in dict:
    if line.startswith('t_'):
        # if "|" in dict[line]:
        #     dict[line] = dict[line].replace("\n", "")
        #     dict[line] = dict[line].replace("\t", "")
        left_production = line[2:]
        tokens.append(left_production)
        function = "\ndef "+line+"(t):\n\tr\'" +dict[line]+ "\'\n\tt.type=reserved.get(t.value,\'"+ left_production +"\')"
        function += "\n\tglobal current_level_of_nesting"
        function += "\n\tt.value = Node(\'" + left_production + "\', t.value, current_level_of_nesting, leaf = 1)\n\treturn t"
        action_funcs =action_funcs + function + "\n"
        tokens_done.append(line)
values=["if","else","switch", "case", "do","while","for"]
# list_of_tokens = dict['tokens'].split(" ")
flag = 0
for key in list(dict.keys())[1:]:
    if key == "start" or "t_" in key:
        break

    list_of_tokens = dict[key].split(" ")
    for token in list_of_tokens:
        fname = token.split("=", 1)[0]
        if fname not in tokens_done:
            if token in values:
                break
            character = token.split("=", 1)[1]
            ch = character[1:2]
            function = "\ndef " + fname + "(t):\n\tr\'" + token.split("=",1)[1]  + "\'\n\t"
            function += "global current_level_of_nesting\n\t"
            if fname == "t_NEWLINE":
                function += "global line_number\n\t"
                # function += "print('in newline')\n\t"
                function += "global just_saw_newline\n\tjust_saw_newline = 1\n\tcurrent_level_of_nesting = 0\n\t"
                function += "line_number += 1\n\t"
                # function += "print('LEXING with line_number: ', line_number)\n\t"
            if ch=='t' or ch==' n ':
                function +="t.value = Node(\'" + key + "\', \'\\"+ch+"\', current_level_of_nesting, leaf = 1)"
            else:
                function += "t.value = Node(\'" + key + "\', \'" + character[1:] + "\', current_level_of_nesting, leaf = 1)"
            if key != "ignore":
                function += "\n\tt.typee = \'" + key + "\'\n\treturn t"
            else:
                function += "\n\tpass"
            action_funcs =action_funcs + function + "\n"

#####ADD RETURN T


# exec(function)

# def t_NAME(t):
#      r'[a-zA-Z_][a-zA-Z_0-9]*'
#      t.type = reserved.get(t.value,'NAME')    # Check for reserved words
#      return t
# #

#defining the actions:
flag = 0
for line in dict:
    if line == "start":
        flag = 1
    if flag:
        function = "\ndef p_"+line+"(t):\n\t\'\'\'"+line+ " : " +dict[line] + "\'\'\' "
        if line == "start":
            function += '\n\tglobal line_number\n\tglobal current_level_of_nesting\n\tline_number = 1\n\tprint("beginning yacc")'
        tree_generation = '\n\tt[0] = Node(\"' + line + '\", \"' + line + '\", current_level_of_nesting, t[1:], leaf = 0)\n'
        function += tree_generation
        action_funcs = action_funcs + function + "\n"
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
#yacc.parse(codesegment)\n\n'''

ply_file_str = '''from random import choice
line_number = 1
just_saw_newline = 0
current_level_of_nesting = 0
class Node:
    def __init__(self, n_type, value, nesting, children=None, leaf=None, error_node = 0, missing = 0):
        self.type = n_type
        self.value = value
        self.lno = line_number
        self.error = error_node
        self.missing = missing
        self.nesting = nesting
        if children:
            self.children = children
        else:
            self.children = [ ]

        self.leaf = leaf

    def set_parent(self, parent):
        self.parent = parent

    def get_parent(self):
        return self.parent

    def get_prevchild(self, parent):
        return self.parent.children[(self.parent.children.index(self.value)-1)]

    def set_error_node(self):
        self.error = 1

    def set_missing(self):
        self.missing = 1

    def get_missing(self):
        return self.missing

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        for i, o in enumerate(self.children):
            if o.value == child.value:
                del self.children[i]
                break

    def __repr__(self, level=0):
        ret = "\t"*level+repr(self.value)+"\\n"
        for child in self.children:
            ret += child.__repr__(level+1)
        return ret


class temp_node:
    def __init__(self, value, type):
        self.value = value
        self.type = type

'''

rest_of_ply_code = '''
# Ignored characters
t_ignore = " "

def t_TAB(t):
    r'\\t'
    global just_saw_newline
    global current_level_of_nesting
    if just_saw_newline:
        current_level_of_nesting = 1
        just_saw_newline = 0
    else:
        current_level_of_nesting += 1

    pass

def find_column(input, token):
    line_start = input.rfind('\\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

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
import random
yacc.yacc()


start= 'start'
'''

rest_of_ply_code += '''\ndata = open(\'{0}\',"r").read()

#root = yacc.parse(data)'''.format(input_file)

rest_of_ply_code += '''\nnumber=0'''

rest_of_ply_code += '''\n\ndef printYield(root, reqpos, type):
    # Stack to store all the nodes
    # of tree
    s1 = []
    global number
    number=number+1
    global line_number
    #print("Global Line Number: " + type + " " + str(line_number))
    # Stack to store all the
    # leaf nodes
    s2 = []
    message=""
    # Push the root node
    s1.append(root)
    prev = root
    n=0
    while len(s1) != 0:
        curr = s1.pop()

        # If current node has a left child
        # push it onto the first stack
        for child in curr.children:
            s1.append(child)
            child.set_parent(curr)

        if curr.leaf:
            n+=1
            if n in reqpos:
                if curr.value == "n+" or 'NAME' in curr.type or 'NUMBER' in curr.type or 'IDENTIFIER' in curr.type:
                        #print("LOG: a number/identifier")
                        reqpos.remove(n)
                        reqpos.append(n+1)
                        s2.append(curr)
                        continue

            if type == "remove" and n in reqpos:
                #print("LOG: inside remove")
                # curr.get_parent().remove_child(curr)
                curr.set_missing()
                reqpos.remove(n)
                message=message + "Line no. " + str(curr.lno) + ": " + curr.value + " missing\\n"
                print("LOG: inside remove message " + "Line no. " + str(curr.lno) + ": " + curr.value + " missing")

            elif type == "remove" and n not in reqpos:
                #print("LOG: remove and n not in reqpos")
                s2.append(curr)

            elif curr.get_missing() == 1:
                s2.append(curr)

            elif type == "add":
                #print("LOG: inside add")
                s2.append(curr)
                if n in reqpos:

                    if curr.type=="bracket" or curr.type=="symbol":
                        print("LOG: inside add, bracket/sym")
                        temp=curr
                    if(random.random()>0.5):
                        temp=curr
                    else:
                        reqpos.remove(n)
                        valid_to_add = arithoperator
                        #valid_to_add.extend(booloperator)
                        valid_to_add.extend(symbol)
                        valid_to_add.extend(bracket)
                        try:
                            valid_to_add.remove("SCOLON")
                            valid_to_add.remove("SEMI")
                        except:
                            pass
                        tok = choice(valid_to_add)
                        if not tok in list(reserved.values()):
                            #temp = Node(tok, tok.lower(), current_level_of_nesting, leaf = 1, error_node = 1)
                        
                            func_name = "t_" + tok
                            fake_t = temp_node("dummy", ")")
                            temp = eval(func_name + "(fake_t)")
                            temp = temp.value
                            print("LOG: inside add ,not reserved, temp value is ", temp.value)
                    temp.set_error_node()
                    curr.get_parent().add_child(temp)
                    s2.append(temp)
                    message=message + "Line no. " + str(curr.lno) + ": Unknown " + temp.value + " found.\\n"
                    print("LOG: inside add, message" + "Line no. " + str(curr.lno) + ": Unknown " + temp.value + " found.")
            elif type == "replace":
                print("LOG: inside replace")
                if n in reqpos:
                    reqpos.remove(n)
                    # tok = choice(tokens)
                    if curr.type == "bracket":
                        print("LOG: inside replace, bracket")
                        while 1:
                            tok = choice(bracket)
                            func_name = "t_" + tok
                            fake_t = temp_node("dummy", ")")
                            temp = eval(func_name + "(fake_t)")
                            temp = temp.value
                            if temp.value != curr.value:
                                break
                    if curr.type == "reserved":
                        print("LOG: inside replace, reserved")
                        while 1:
                            lper=["".join(perm) for perm in itertools.permutations(curr.value)]
                            tok = choice(lper)
                            func_name = "t_" + tok
                            fake_t = temp_node("dummy", ")")
                            temp = eval(func_name + "(fake_t)")
                            temp = temp.value
                            if temp.value != curr.value:
                                break
                    elif curr.type == "arithoperator":
                        print("LOG: inside replace, arithop")
                        while 1:
                            tok = choice(symbol)
                            func_name = "t_" + tok
                            fake_t = temp_node("dummy", ")")
                            temp = eval(func_name + "(fake_t)")
                            temp = temp.value
                            if temp.value != curr.value:
                                break
                    elif curr.type == "eqoperator":
                        print("LOG: inside replace, eqop")
                        while 1:
                            tok = choice(symbol)
                            func_name = "t_" + tok
                            fake_t = temp_node("dummy", ")")
                            temp = eval(func_name + "(fake_t)")
                            temp = temp.value
                            if temp.value != curr.value:
                                break
                    elif curr.type == "loop":
                        print("LOG: inside replace, loop")
                        while 1:
                            tok = choice(loop)
                            func_name = "t_" + tok
                            fake_t = temp_node("dummy", ")")
                            temp = eval(func_name + "(fake_t)")
                            temp = temp.value
                            if temp.value != curr.value:
                                break
                    elif curr.type == "selection":
                        print("LOG: inside replace, selection")
                        while 1:
                            tok = choice(selection)
                            func_name = "t_" + tok
                            fake_t = temp_node("dummy", ")")
                            temp = eval(func_name + "(fake_t)")
                            temp = temp.value
                            if temp.value != curr.value:
                                break
                    elif curr.type == "symbol":
                        print("LOG: inside replace, symbol")
                        while 1:
                            tok = choice(symbol)
                            func_name = "t_" + tok
                            fake_t = temp_node("dummy", ")")
                            temp = eval(func_name + "(fake_t)")
                            temp = temp.value
                            if temp.value != curr.value:
                                break

                    else:
                        print("LOG: inside replace, else")
                        newl = bracket
                        newl.extend(arithoperator)
                        newl.extend(symbol)
                        newl.extend(booloperator)
                        tok = choice(newl)
                        func_name = "t_" + tok
                        fake_t = temp_node("dummy", ")")
                        temp = eval(func_name + "(fake_t)")
                        temp = temp.value
                    temp.set_error_node()
                    curr.set_missing()
                    curr.get_parent().remove_child(curr)
                    curr.get_parent().add_child(temp)
                    s2.append(temp)
                    message=message +"Line no. " + str(curr.lno) + ": Unknown " + temp.value + " found.\\n"
                    print("LOG: inside replace, message" + "Line no. " + str(curr.lno) + ": Unknown " + temp.value + " found")
                    message=message +"Line no. " + str(curr.lno) + ": " + curr.value + " missing\\n"
                    print("LOG: inside replace, message" + "Line no. " + str(curr.lno) + ": " + curr.value + " missing")


                else:
                    s2.append(curr)

    # Print all the leaf nodes
    level = 0
    code = ""
    code_error_colors = ""
    line_no = 0
    time_for_tabs = 0
    while len(s2) != 0:
        val = s2.pop()
        if val.lno > line_no:
            line_no = val.lno
            code += "\\n"
            code_error_colors += "\\n"
            time_for_tabs = 1
        if time_for_tabs:
            for i in range(0, val.nesting):
                code += "\\t"
                code_error_colors += "\\t"
            time_for_tabs = 0
        if val.value == "n+":
            time_for_tabs = 1
        if val.get_missing() == 1:
            code_error_colors = code_error_colors + ' <span style="color:red">' + val.value + '</span> '
        else:
            if val.error == 0:
                code_error_colors = code_error_colors + "" + val.value + " "
            else:
                code_error_colors = code_error_colors + ' <span style="color:red">' + val.value + '</span> '
            code = code + "" + val.value + " "
    code = code[1:]
    code_error_colors = code_error_colors[1:]
    return code, code_error_colors, message, root


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


#### now we will try to introduce errors in the above syntax tree
newroot = yacc.parse(data)
pgmLen = getPgmLen(newroot)
percstring= \'{2}\'
percint=int(percstring)
error_len =  percint / 100 * pgmLen
#print("error_len" + str(error_len))
pgms =  5
directory= \'{0}\'

fname = \'{1}\'.split(".")[0]
extension = \'{1}\'.split(".")[1]

error_val= int(error_len/3)
#n_add_errors = 1
#n_remove_errors = 3
#n_replace_errors = 1

n_add_errors = int(error_val/3)
n_remove_errors = int(error_val/3)
n_replace_errors = int(error_val/3)
if(n_add_errors < 1):
    n_add_errors=1
if(n_remove_errors < 1):
    n_remove_errors=1
if(n_replace_errors < 1):
    n_replace_errors=1

error_dict = {{"remove": n_remove_errors, "replace" : n_replace_errors, "add" : n_add_errors}}
for i in range(0,pgms):
    newroot = yacc.parse(data)
    pgmLen = getPgmLen(newroot)
    positions = [i for i in range(1,pgmLen-2)]
    message = ""
    pgm = ""
    for key in error_dict.keys():
        reqpos = []
        for j in range(0,error_dict[key]):
            c = choice(positions)
            reqpos.append(c)
            positions.remove(c)
        pgm, pgm_errors_marked, message1, newroot = printYield(newroot, reqpos, key)
        message += message1
    pgm = pgm.replace("n+", "")
#    pgm_errors_marked = pgm_errors_marked.replace("n+","<br/>")
    pgm_errors_marked = pgm_errors_marked.replace("\\n","<br/>")
    pgm_errors_marked = pgm_errors_marked.replace("\\t", "&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp")
    error_list = message.split("\\n")
    sorted_list = []
    sorted_message =""
    for line in error_list:
        thisline =[]
        linenum = line.split(":")
        if len(linenum )>=2:
            error_text = line[line.find(':')+1:]
            linenum = linenum[0].split(".")
            if len(linenum)>=2:
                linenum = linenum[1]
                thisline.append(int(linenum))
                thisline.append( error_text)
                sorted_list.append(thisline)
    sorted_list.sort(key = lambda x: x[0])
    for e in sorted_list :
        sorted_message += "Line no. "+str(e[0])+" : "+e[1]+"\\n"

    f = open(directory + fname + "_" + str(i) + "." + extension , "w")
    f_err_cols = open(directory + fname + "_" + str(i) +"_errors_marked" + "." + extension , "w")
    fe=open(directory + "errors/" + fname + "_" + str(i) + "_error." + extension , "w")
    fe.write(sorted_message)
    fe.close()
    f.write(pgm)
    f_err_cols.write(pgm_errors_marked)
    f.close()
    f_err_cols.close()

'''.format(output_directory, i, perc)
tokens = list(dict.fromkeys(tokens))
for key in final_lists.keys():
    ply_file_str += key + " = " + str(final_lists[key])

    ply_file_str += "\n"
ply_file_str += "selection=['if', 'else', 'switch', 'case']"
ply_file_str += "\n"
ply_file_str += "loop=['while', 'do', 'for']"
ply_file_str += "\n"
ply_file_str += "reserved = " + str(reserved) +"\n"+"selection = " + str(selection) + "\n" +"loop = " + str(loop) + "\n" + "tokens = " + str(tokens) + "\n" + action_funcs + rest_of_ply_code

f = open("ply_program.py", "w")
f.write(ply_file_str)
f.close()
#print("keer" + str((perc)))
# exec(execute_code)
#exec(open('ply_program.py').read())
import os
import subprocess
# os.system("/usr/bin/python3 ply_program.py>>ply.out")
os.system("python3 ply_program.py")
#subprocess.call(['/usr/bin/python3', os.getcwd() + '/ply_program.py'])
