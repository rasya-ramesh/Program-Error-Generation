# input_file = "../programs/python/functions/input_programs/functionfoo.py"
# grammar_file = "python_grammar.txt"


# Run command:
# python3 interpretgrammar.py -g python_grammar.txt -l python -i functionfoo.py -t functions
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-g", required=True, help="This is the grammar file")
parser.add_argument("-l", required=True,  help="Language")
parser.add_argument("-i", required=True, help="The syntactically correct input program segment")
parser.add_argument("-t", required=True, help="Category of program (construct)")

args = parser.parse_args()
grammar_file = args.g
l = args.l
t = args.t
i = args.i
input_file = '../programs/' + l + '/' + t + '/input_programs/' + i
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
    lr = line.split(":=")
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

action_funcs = ""
function =""
for line in dict:
    if line.startswith('t_'):
        left_production = line[2:]
        function = "\ndef "+line+"(t):\n\tr\'" +dict[line]+ "\'\n\tt.type=reserved.get(t.value,\'"+ left_production +"\')\n\treturn t"

exec(function)
action_funcs =action_funcs + function + "\n"

# def t_NAME(t):
#      r'[a-zA-Z_][a-zA-Z_0-9]*'
#      t.type = reserved.get(t.value,'NAME')    # Check for reserved words
#      return t
# #
# Build the lexer
import ply.lex as lex
lexer = lex.lex()

#defining the actions:
for line in dict:
    if (line not in ['start','reserved','tokens']) and (not line.startswith('t_')):
        function = "\ndef p_"+line+"(t):\n\t\'\'\'"+line+ " : " +dict[line] + "\'\'\' "
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


exec(execute_code)
