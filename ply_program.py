from random import choice
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
        ret = "	"*level+repr(self.value)+"\n"
        for child in self.children:
            ret += child.__repr__(level+1)
        return ret


class temp_node:
    def __init__(self, value, type):
        self.value = value
        self.type = type

selection = []
loop = []
eqoperator = ['EQEQUAL', 'NOTEQUAL', 'LESSEQUAL', 'PLUSEQUAL', 'MINEQUAL', 'STAREQUAL', 'SLASHEQUAL', 'PERCENTEQUAL', 'GREATEREQUAL', 'STARSTAREQUAL', 'SLASHSLASHEQUAL', 'LESS', 'GREATER', 'EQUAL']
arithoperator = ['PLUS', 'MINUS', 'STAR', 'SLASH', 'LEFTSHIFT', 'RIGHTSHIFT', 'STARSTAR', 'SLASHSLASH']
booloperator = ['VBAR', 'AMPER']
symbol = ['COLON', 'COMMA', 'SEMI', 'DOT', 'PERCENT', 'BACKQUOTE', 'CIRCUMFLEX', 'TILDE', 'AT']
bracket = ['LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LSQB', 'RSQB']
token = ['NEWLINE']
selection=['if', 'else', 'switch', 'case']
loop=['while', 'do', 'for']
reserved = {'and': 'AND', 'as': 'AS', 'assert': 'ASSERT', 'break': 'BREAK', 'class': 'CLASS', 'continue': 'CONTINUE', 'def': 'DEF', 'del': 'DEL', 'elif': 'ELIF', 'else': 'ELSE', 'except': 'EXCEPT', 'exec': 'EXEC', 'finally': 'FINALLY', 'for': 'FOR', 'from': 'FROM', 'global': 'GLOBAL', 'if': 'IF', 'import': 'IMPORT', 'in': 'IN', 'is': 'IS', 'lambda': 'LAMBDA', 'not': 'NOT', 'or': 'OR', 'pass': 'PASS', 'print': 'PRINT', 'raise': 'RAISE', 'return': 'RETURN', 'try': 'TRY', 'while': 'WHILE', 'with': 'WITH', 'yield': 'YIELD'}
selection = {'if': 'IF', 'else': 'ELSE'}
loop = {'do': 'DO', 'while': 'WHILE', 'for': 'FOR'}
tokens = ['AND', 'AS', 'ASSERT', 'BREAK', 'CLASS', 'CONTINUE', 'DEF', 'DEL', 'ELIF', 'ELSE', 'EXCEPT', 'EXEC', 'FINALLY', 'FOR', 'FROM', 'GLOBAL', 'IF', 'IMPORT', 'IN', 'IS', 'LAMBDA', 'NOT', 'OR', 'PASS', 'PRINT', 'RAISE', 'RETURN', 'TRY', 'WHILE', 'WITH', 'YIELD', 'EQEQUAL', 'NOTEQUAL', 'LESSEQUAL', 'PLUSEQUAL', 'MINEQUAL', 'STAREQUAL', 'SLASHEQUAL', 'PERCENTEQUAL', 'GREATEREQUAL', 'STARSTAREQUAL', 'SLASHSLASHEQUAL', 'LESS', 'GREATER', 'EQUAL', 'PLUS', 'MINUS', 'STAR', 'SLASH', 'LEFTSHIFT', 'RIGHTSHIFT', 'STARSTAR', 'SLASHSLASH', 'VBAR', 'AMPER', 'COLON', 'COMMA', 'SEMI', 'DOT', 'PERCENT', 'BACKQUOTE', 'CIRCUMFLEX', 'TILDE', 'AT', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LSQB', 'RSQB', 'NEWLINE', 'NUMBER', 'TRIPLESTRING', 'STRING', 'RAWSTRING', 'UNICODESTRING', 'BINARYNUMBER', 'OCTALNUMBER', 'HEXADECIMALNUMBER', 'NAME']

def t_NUMBER(t):
	r'\d+'
	t.type=reserved.get(t.value,'NUMBER')
	global current_level_of_nesting
	t.value = Node('NUMBER', t.value, current_level_of_nesting, leaf = 1)
	return t

def t_TRIPLESTRING(t):
	r'"{3}([\s\S]*?"{3}) | \'{3}([\s\S]*?\'{3})'
	t.type=reserved.get(t.value,'TRIPLESTRING')
	global current_level_of_nesting
	t.value = Node('TRIPLESTRING', t.value, current_level_of_nesting, leaf = 1)
	return t

def t_STRING(t):
	r'(\"(\\.|[^\"\n]|(\\\n))*\") | (\'(\\.|[^\'\n]|(\\\n))*\')'
	t.type=reserved.get(t.value,'STRING')
	global current_level_of_nesting
	t.value = Node('STRING', t.value, current_level_of_nesting, leaf = 1)
	return t

def t_RAWSTRING(t):
	r'[rR](\"(\\.|[^\"\n]|(\\\n))*\") | [rR](\'(\\.|[^\'\n]|(\\\n))*\')'
	t.type=reserved.get(t.value,'RAWSTRING')
	global current_level_of_nesting
	t.value = Node('RAWSTRING', t.value, current_level_of_nesting, leaf = 1)
	return t

def t_UNICODESTRING(t):
	r'[uU](\"(\\.|[^\"\n]|(\\\n))*\") | [uU](\'(\\.|[^\'\n]|(\\\n))*\')'
	t.type=reserved.get(t.value,'UNICODESTRING')
	global current_level_of_nesting
	t.value = Node('UNICODESTRING', t.value, current_level_of_nesting, leaf = 1)
	return t

def t_BINARYNUMBER(t):
	r'0[bB]([0-1]+)'
	t.type=reserved.get(t.value,'BINARYNUMBER')
	global current_level_of_nesting
	t.value = Node('BINARYNUMBER', t.value, current_level_of_nesting, leaf = 1)
	return t

def t_OCTALNUMBER(t):
	r'0[oO]([0-7]+)'
	t.type=reserved.get(t.value,'OCTALNUMBER')
	global current_level_of_nesting
	t.value = Node('OCTALNUMBER', t.value, current_level_of_nesting, leaf = 1)
	return t

def t_HEXADECIMALNUMBER(t):
	r'0[xX]([0-9a-fA-F]+)'
	t.type=reserved.get(t.value,'HEXADECIMALNUMBER')
	global current_level_of_nesting
	t.value = Node('HEXADECIMALNUMBER', t.value, current_level_of_nesting, leaf = 1)
	return t

def t_NAME(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	t.type=reserved.get(t.value,'NAME')
	global current_level_of_nesting
	t.value = Node('NAME', t.value, current_level_of_nesting, leaf = 1)
	return t

def t_EQEQUAL(t):
	r'\=='
	global current_level_of_nesting
	t.value = Node('eqoperator', '==', current_level_of_nesting, leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_NOTEQUAL(t):
	r'\!='
	global current_level_of_nesting
	t.value = Node('eqoperator', '!=', current_level_of_nesting, leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_LESSEQUAL(t):
	r'\<='
	global current_level_of_nesting
	t.value = Node('eqoperator', '<=', current_level_of_nesting, leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_PLUSEQUAL(t):
	r'\\+='
	global current_level_of_nesting
	t.value = Node('eqoperator', '\+=', current_level_of_nesting, leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_MINEQUAL(t):
	r'\-='
	global current_level_of_nesting
	t.value = Node('eqoperator', '-=', current_level_of_nesting, leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_STAREQUAL(t):
	r'\*='
	global current_level_of_nesting
	t.value = Node('eqoperator', '*=', current_level_of_nesting, leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_SLASHEQUAL(t):
	r'\/='
	global current_level_of_nesting
	t.value = Node('eqoperator', '/=', current_level_of_nesting, leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_PERCENTEQUAL(t):
	r'\%='
	global current_level_of_nesting
	t.value = Node('eqoperator', '%=', current_level_of_nesting, leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_GREATEREQUAL(t):
	r'\>='
	global current_level_of_nesting
	t.value = Node('eqoperator', '>=', current_level_of_nesting, leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_STARSTAREQUAL(t):
	r'\*\*='
	global current_level_of_nesting
	t.value = Node('eqoperator', '*\*=', current_level_of_nesting, leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_SLASHSLASHEQUAL(t):
	r'\//='
	global current_level_of_nesting
	t.value = Node('eqoperator', '//=', current_level_of_nesting, leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_LESS(t):
	r'\<'
	global current_level_of_nesting
	t.value = Node('eqoperator', '<', current_level_of_nesting, leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_GREATER(t):
	r'\>'
	global current_level_of_nesting
	t.value = Node('eqoperator', '>', current_level_of_nesting, leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_EQUAL(t):
	r'\='
	global current_level_of_nesting
	t.value = Node('eqoperator', '=', current_level_of_nesting, leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_PLUS(t):
	r'\+'
	global current_level_of_nesting
	t.value = Node('arithoperator', '+', current_level_of_nesting, leaf = 1)
	t.typee = 'arithoperator'
	return t

def t_MINUS(t):
	r'\-'
	global current_level_of_nesting
	t.value = Node('arithoperator', '-', current_level_of_nesting, leaf = 1)
	t.typee = 'arithoperator'
	return t

def t_STAR(t):
	r'\*'
	global current_level_of_nesting
	t.value = Node('arithoperator', '*', current_level_of_nesting, leaf = 1)
	t.typee = 'arithoperator'
	return t

def t_SLASH(t):
	r'\/'
	global current_level_of_nesting
	t.value = Node('arithoperator', '/', current_level_of_nesting, leaf = 1)
	t.typee = 'arithoperator'
	return t

def t_LEFTSHIFT(t):
	r'\<<'
	global current_level_of_nesting
	t.value = Node('arithoperator', '<<', current_level_of_nesting, leaf = 1)
	t.typee = 'arithoperator'
	return t

def t_RIGHTSHIFT(t):
	r'\>>'
	global current_level_of_nesting
	t.value = Node('arithoperator', '>>', current_level_of_nesting, leaf = 1)
	t.typee = 'arithoperator'
	return t

def t_STARSTAR(t):
	r'\*\*'
	global current_level_of_nesting
	t.value = Node('arithoperator', '*\*', current_level_of_nesting, leaf = 1)
	t.typee = 'arithoperator'
	return t

def t_SLASHSLASH(t):
	r'\//'
	global current_level_of_nesting
	t.value = Node('arithoperator', '//', current_level_of_nesting, leaf = 1)
	t.typee = 'arithoperator'
	return t

def t_VBAR(t):
	r'\|'
	global current_level_of_nesting
	t.value = Node('booloperator', '|', current_level_of_nesting, leaf = 1)
	t.typee = 'booloperator'
	return t

def t_AMPER(t):
	r'\&'
	global current_level_of_nesting
	t.value = Node('booloperator', '&', current_level_of_nesting, leaf = 1)
	t.typee = 'booloperator'
	return t

def t_COLON(t):
	r'\:'
	global current_level_of_nesting
	t.value = Node('symbol', ':', current_level_of_nesting, leaf = 1)
	t.typee = 'symbol'
	return t

def t_COMMA(t):
	r'\,'
	global current_level_of_nesting
	t.value = Node('symbol', ',', current_level_of_nesting, leaf = 1)
	t.typee = 'symbol'
	return t

def t_SEMI(t):
	r'\;'
	global current_level_of_nesting
	t.value = Node('symbol', ';', current_level_of_nesting, leaf = 1)
	t.typee = 'symbol'
	return t

def t_DOT(t):
	r'\.'
	global current_level_of_nesting
	t.value = Node('symbol', '.', current_level_of_nesting, leaf = 1)
	t.typee = 'symbol'
	return t

def t_PERCENT(t):
	r'\%'
	global current_level_of_nesting
	t.value = Node('symbol', '%', current_level_of_nesting, leaf = 1)
	t.typee = 'symbol'
	return t

def t_BACKQUOTE(t):
	r'\`'
	global current_level_of_nesting
	t.value = Node('symbol', '`', current_level_of_nesting, leaf = 1)
	t.typee = 'symbol'
	return t

def t_CIRCUMFLEX(t):
	r'\^'
	global current_level_of_nesting
	t.value = Node('symbol', '^', current_level_of_nesting, leaf = 1)
	t.typee = 'symbol'
	return t

def t_TILDE(t):
	r'\~'
	global current_level_of_nesting
	t.value = Node('symbol', '~', current_level_of_nesting, leaf = 1)
	t.typee = 'symbol'
	return t

def t_AT(t):
	r'\@'
	global current_level_of_nesting
	t.value = Node('symbol', '@', current_level_of_nesting, leaf = 1)
	t.typee = 'symbol'
	return t

def t_LPAREN(t):
	r'\('
	global current_level_of_nesting
	t.value = Node('bracket', '(', current_level_of_nesting, leaf = 1)
	t.typee = 'bracket'
	return t

def t_RPAREN(t):
	r'\)'
	global current_level_of_nesting
	t.value = Node('bracket', ')', current_level_of_nesting, leaf = 1)
	t.typee = 'bracket'
	return t

def t_LBRACE(t):
	r'\{'
	global current_level_of_nesting
	t.value = Node('bracket', '{', current_level_of_nesting, leaf = 1)
	t.typee = 'bracket'
	return t

def t_RBRACE(t):
	r'\}'
	global current_level_of_nesting
	t.value = Node('bracket', '}', current_level_of_nesting, leaf = 1)
	t.typee = 'bracket'
	return t

def t_LSQB(t):
	r'\['
	global current_level_of_nesting
	t.value = Node('bracket', '[', current_level_of_nesting, leaf = 1)
	t.typee = 'bracket'
	return t

def t_RSQB(t):
	r'\]'
	global current_level_of_nesting
	t.value = Node('bracket', ']', current_level_of_nesting, leaf = 1)
	t.typee = 'bracket'
	return t

def t_NEWLINE(t):
	r'\n+'
	global current_level_of_nesting
	global line_number
	global just_saw_newline
	just_saw_newline = 1
	current_level_of_nesting = 0
	line_number += 1
	t.value = Node('token', 'n+', current_level_of_nesting, leaf = 1)
	t.typee = 'token'
	return t

def p_start(t):
	'''start : file_input''' 
	global line_number
	global current_level_of_nesting
	line_number = 1
	print("beginning yacc")
	t[0] = Node("start", "start", current_level_of_nesting, t[1:], leaf = 0)


def p_file_input(t):
	'''file_input : single_stmt''' 
	t[0] = Node("file_input", "file_input", current_level_of_nesting, t[1:], leaf = 0)


def p_single_stmt(t):
	'''single_stmt : single_stmt NEWLINE 
	| single_stmt stmt 
	|''' 
	t[0] = Node("single_stmt", "single_stmt", current_level_of_nesting, t[1:], leaf = 0)


def p_funcdef(t):
	'''funcdef : DEF NAME parameters COLON suite''' 
	t[0] = Node("funcdef", "funcdef", current_level_of_nesting, t[1:], leaf = 0)


def p_parameters(t):
	'''parameters : LPAREN varargslist RPAREN''' 
	t[0] = Node("parameters", "parameters", current_level_of_nesting, t[1:], leaf = 0)


def p_varargslist(t):
	'''varargslist : 
	| fpdef EQUAL test fpdeflist COMMA 
	| fpdef EQUAL test fpdeflist 
	| fpdef fpdeflist COMMA 
	| fpdef fpdeflist''' 
	t[0] = Node("varargslist", "varargslist", current_level_of_nesting, t[1:], leaf = 0)


def p_fpdeflist(t):
	'''fpdeflist : 
	| fpdeflist COMMA fpdef 
	| fpdeflist COMMA fpdef EQUAL test''' 
	t[0] = Node("fpdeflist", "fpdeflist", current_level_of_nesting, t[1:], leaf = 0)


def p_fpdef(t):
	'''fpdef : NAME  
	| LPAREN fplist RPAREN''' 
	t[0] = Node("fpdef", "fpdef", current_level_of_nesting, t[1:], leaf = 0)


def p_fplist(t):
	'''fplist : fpdef fplist1 COMMA 
	| fpdef fplist1''' 
	t[0] = Node("fplist", "fplist", current_level_of_nesting, t[1:], leaf = 0)


def p_fplist1(t):
	'''fplist1 : 
	| fplist1 COMMA fpdef''' 
	t[0] = Node("fplist1", "fplist1", current_level_of_nesting, t[1:], leaf = 0)


def p_stmt(t):
	'''stmt : simple_stmt 
	| compound_stmt''' 
	t[0] = Node("stmt", "stmt", current_level_of_nesting, t[1:], leaf = 0)


def p_simple_stmt(t):
	'''simple_stmt : small_stmts NEWLINE 
	| small_stmts SEMI NEWLINE''' 
	t[0] = Node("simple_stmt", "simple_stmt", current_level_of_nesting, t[1:], leaf = 0)


def p_small_stmts(t):
	'''small_stmts : small_stmts SEMI small_stmt 
	| small_stmt''' 
	t[0] = Node("small_stmts", "small_stmts", current_level_of_nesting, t[1:], leaf = 0)


def p_small_stmt(t):
	'''small_stmt : flow_stmt 
	| expr_stmt 
	| print_stmt 
	| pass_stmt 
	| import_stmt 
	| global_stmt 
	| assert_stmt''' 
	t[0] = Node("small_stmt", "small_stmt", current_level_of_nesting, t[1:], leaf = 0)


def p_expr_stmt(t):
	'''expr_stmt : testlist augassign testlist 
	| testlist eqtestlist''' 
	t[0] = Node("expr_stmt", "expr_stmt", current_level_of_nesting, t[1:], leaf = 0)


def p_eqtestlist(t):
	'''eqtestlist : 
	| eqtestlist EQUAL testlist''' 
	t[0] = Node("eqtestlist", "eqtestlist", current_level_of_nesting, t[1:], leaf = 0)


def p_augassign(t):
	'''augassign : PLUSEQUAL  
	| MINEQUAL  
	| STAREQUAL  
	| SLASHEQUAL  
	| PERCENTEQUAL  
	| STARSTAREQUAL  
	| SLASHSLASHEQUAL''' 
	t[0] = Node("augassign", "augassign", current_level_of_nesting, t[1:], leaf = 0)


def p_print_stmt(t):
	'''print_stmt : PRINT 
	| PRINT testlist''' 
	t[0] = Node("print_stmt", "print_stmt", current_level_of_nesting, t[1:], leaf = 0)


def p_pass_stmt(t):
	'''pass_stmt : PASS''' 
	t[0] = Node("pass_stmt", "pass_stmt", current_level_of_nesting, t[1:], leaf = 0)


def p_flow_stmt(t):
	'''flow_stmt : break_stmt 
	| continue_stmt 
	| return_stmt''' 
	t[0] = Node("flow_stmt", "flow_stmt", current_level_of_nesting, t[1:], leaf = 0)


def p_break_stmt(t):
	'''break_stmt : BREAK''' 
	t[0] = Node("break_stmt", "break_stmt", current_level_of_nesting, t[1:], leaf = 0)


def p_continue_stmt(t):
	'''continue_stmt : CONTINUE''' 
	t[0] = Node("continue_stmt", "continue_stmt", current_level_of_nesting, t[1:], leaf = 0)


def p_return_stmt(t):
	'''return_stmt : RETURN  
	| RETURN testlist''' 
	t[0] = Node("return_stmt", "return_stmt", current_level_of_nesting, t[1:], leaf = 0)


def p_import_stmt(t):
	'''import_stmt : IMPORT NAME 
	| IMPORT NAME AS NAME''' 
	t[0] = Node("import_stmt", "import_stmt", current_level_of_nesting, t[1:], leaf = 0)


def p_global_stmt(t):
	'''global_stmt : GLOBAL NAME namelist''' 
	t[0] = Node("global_stmt", "global_stmt", current_level_of_nesting, t[1:], leaf = 0)


def p_namelist(t):
	'''namelist : 
	| COMMA NAME namelist''' 
	t[0] = Node("namelist", "namelist", current_level_of_nesting, t[1:], leaf = 0)


def p_assert_stmt(t):
	'''assert_stmt : ASSERT testlist''' 
	t[0] = Node("assert_stmt", "assert_stmt", current_level_of_nesting, t[1:], leaf = 0)


def p_compound_stmt(t):
	'''compound_stmt : if_stmt 
	| for_stmt 
	| while_stmt 
	| funcdef 
	| classdef''' 
	t[0] = Node("compound_stmt", "compound_stmt", current_level_of_nesting, t[1:], leaf = 0)


def p_if_stmt(t):
	'''if_stmt : IF test COLON suite elif_list 
	| IF test COLON suite elif_list ELSE COLON suite''' 
	t[0] = Node("if_stmt", "if_stmt", current_level_of_nesting, t[1:], leaf = 0)


def p_elif_list(t):
	'''elif_list : 
	| ELIF test COLON suite elif_list''' 
	t[0] = Node("elif_list", "elif_list", current_level_of_nesting, t[1:], leaf = 0)


def p_while_stmt(t):
	'''while_stmt : WHILE test COLON suite  
	| WHILE test COLON suite ELSE COLON suite''' 
	t[0] = Node("while_stmt", "while_stmt", current_level_of_nesting, t[1:], leaf = 0)


def p_for_stmt(t):
	'''for_stmt : FOR exprlist IN testlist COLON suite 
	| FOR exprlist IN testlist COLON suite ELSE COLON suite''' 
	t[0] = Node("for_stmt", "for_stmt", current_level_of_nesting, t[1:], leaf = 0)


def p_suite(t):
	'''suite : simple_stmt 
	| NEWLINE stmts''' 
	t[0] = Node("suite", "suite", current_level_of_nesting, t[1:], leaf = 0)


def p_test(t):
	'''test : or_test 
	| or_test IF or_test ELSE test''' 
	t[0] = Node("test", "test", current_level_of_nesting, t[1:], leaf = 0)


def p_or_test(t):
	'''or_test : and_test ortestlist''' 
	t[0] = Node("or_test", "or_test", current_level_of_nesting, t[1:], leaf = 0)


def p_ortestlist(t):
	'''ortestlist : 
	| OR and_test ortestlist''' 
	t[0] = Node("ortestlist", "ortestlist", current_level_of_nesting, t[1:], leaf = 0)


def p_and_test(t):
	'''and_test : not_test andtestlist''' 
	t[0] = Node("and_test", "and_test", current_level_of_nesting, t[1:], leaf = 0)


def p_andtestlist(t):
	'''andtestlist : 
	| AND not_test andtestlist''' 
	t[0] = Node("andtestlist", "andtestlist", current_level_of_nesting, t[1:], leaf = 0)


def p_not_test(t):
	'''not_test : NOT not_test 
	| comparison''' 
	t[0] = Node("not_test", "not_test", current_level_of_nesting, t[1:], leaf = 0)


def p_comparison(t):
	'''comparison : expr compexprlist''' 
	t[0] = Node("comparison", "comparison", current_level_of_nesting, t[1:], leaf = 0)


def p_compexprlist(t):
	'''compexprlist : 
	| comp_op expr compexprlist''' 
	t[0] = Node("compexprlist", "compexprlist", current_level_of_nesting, t[1:], leaf = 0)


def p_comp_op(t):
	'''comp_op : LESS 
	| GREATER 
	| EQEQUAL 
	| GREATEREQUAL 
	| LESSEQUAL 
	| NOTEQUAL 
	| IN 
	| NOT IN 
	| IS 
	| IS NOT''' 
	t[0] = Node("comp_op", "comp_op", current_level_of_nesting, t[1:], leaf = 0)


def p_expr(t):
	'''expr : xor_expr xorexprlist''' 
	t[0] = Node("expr", "expr", current_level_of_nesting, t[1:], leaf = 0)


def p_xorexprlist(t):
	'''xorexprlist : 
	| VBAR xor_expr xorexprlist''' 
	t[0] = Node("xorexprlist", "xorexprlist", current_level_of_nesting, t[1:], leaf = 0)


def p_xor_expr(t):
	'''xor_expr : and_expr andexprlist''' 
	t[0] = Node("xor_expr", "xor_expr", current_level_of_nesting, t[1:], leaf = 0)


def p_andexprlist(t):
	'''andexprlist : 
	| CIRCUMFLEX and_expr andexprlist''' 
	t[0] = Node("andexprlist", "andexprlist", current_level_of_nesting, t[1:], leaf = 0)


def p_and_expr(t):
	'''and_expr : shift_expr shiftexprlist''' 
	t[0] = Node("and_expr", "and_expr", current_level_of_nesting, t[1:], leaf = 0)


def p_shiftexprlist(t):
	'''shiftexprlist : 
	| AMPER shift_expr shiftexprlist''' 
	t[0] = Node("shiftexprlist", "shiftexprlist", current_level_of_nesting, t[1:], leaf = 0)


def p_shift_expr(t):
	'''shift_expr : arith_expr arithexprlist''' 
	t[0] = Node("shift_expr", "shift_expr", current_level_of_nesting, t[1:], leaf = 0)


def p_arithexprlist(t):
	'''arithexprlist : 
	| LEFTSHIFT arith_expr arithexprlist 
	| RIGHTSHIFT arith_expr arithexprlist''' 
	t[0] = Node("arithexprlist", "arithexprlist", current_level_of_nesting, t[1:], leaf = 0)


def p_arith_expr(t):
	'''arith_expr : term termlist''' 
	t[0] = Node("arith_expr", "arith_expr", current_level_of_nesting, t[1:], leaf = 0)


def p_termlist(t):
	'''termlist : 
	| PLUS term termlist 
	| MINUS term termlist''' 
	t[0] = Node("termlist", "termlist", current_level_of_nesting, t[1:], leaf = 0)


def p_term(t):
	'''term : factor factorlist''' 
	t[0] = Node("term", "term", current_level_of_nesting, t[1:], leaf = 0)


def p_factorlist(t):
	'''factorlist : 
	| STAR factor factorlist 
	| SLASH factor factorlist 
	| PERCENT factor factorlist 
	| SLASHSLASH factor factorlist''' 
	t[0] = Node("factorlist", "factorlist", current_level_of_nesting, t[1:], leaf = 0)


def p_factor(t):
	'''factor : power 
	| PLUS factor 
	| MINUS factor 
	| TILDE factor''' 
	t[0] = Node("factor", "factor", current_level_of_nesting, t[1:], leaf = 0)


def p_power(t):
	'''power : atom trailerlist 
	| atom trailerlist STARSTAR factor''' 
	t[0] = Node("power", "power", current_level_of_nesting, t[1:], leaf = 0)


def p_trailerlist(t):
	'''trailerlist : 
	| trailer trailerlist''' 
	t[0] = Node("trailerlist", "trailerlist", current_level_of_nesting, t[1:], leaf = 0)


def p_atom(t):
	'''atom : LPAREN RPAREN 
	| LPAREN testlist_comp RPAREN 
	| LSQB RSQB 
	| LSQB listmaker RSQB 
	| LBRACE RBRACE 
	| LBRACE dictorsetmaker RBRACE 
	| BACKQUOTE testlist1 BACKQUOTE 
	| NAME 
	| NUMBER 
	| stringlist''' 
	t[0] = Node("atom", "atom", current_level_of_nesting, t[1:], leaf = 0)


def p_stringlist(t):
	'''stringlist : STRING  
	| STRING stringlist 
	| TRIPLESTRING 
	| TRIPLESTRING stringlist''' 
	t[0] = Node("stringlist", "stringlist", current_level_of_nesting, t[1:], leaf = 0)


def p_listmaker(t):
	'''listmaker : testlist''' 
	t[0] = Node("listmaker", "listmaker", current_level_of_nesting, t[1:], leaf = 0)


def p_testlist_comp(t):
	'''testlist_comp : testlist''' 
	t[0] = Node("testlist_comp", "testlist_comp", current_level_of_nesting, t[1:], leaf = 0)


def p_trailer(t):
	'''trailer : LPAREN RPAREN 
	| LPAREN arglist RPAREN 
	| LSQB subscriptlist RSQB 
	| DOT NAME''' 
	t[0] = Node("trailer", "trailer", current_level_of_nesting, t[1:], leaf = 0)


def p_subscriptlist(t):
	'''subscriptlist : subscript 
	| subscript COMMA 
	| subscript COMMA subscriptlist''' 
	t[0] = Node("subscriptlist", "subscriptlist", current_level_of_nesting, t[1:], leaf = 0)


def p_subscript(t):
	'''subscript : DOT DOT DOT 
	| test 
	| test COLON test sliceop 
	| COLON test sliceop 
	| test COLON sliceop 
	| test COLON test 
	| test COLON 
	| COLON test 
	| COLON sliceop 
	| COLON''' 
	t[0] = Node("subscript", "subscript", current_level_of_nesting, t[1:], leaf = 0)


def p_sliceop(t):
	'''sliceop : COLON 
	| COLON test''' 
	t[0] = Node("sliceop", "sliceop", current_level_of_nesting, t[1:], leaf = 0)


def p_exprlist(t):
	'''exprlist : expr 
	| expr COMMA 
	| expr COMMA exprlist''' 
	t[0] = Node("exprlist", "exprlist", current_level_of_nesting, t[1:], leaf = 0)


def p_testlist(t):
	'''testlist : test 
	| test COMMA 
	| test COMMA testlist''' 
	t[0] = Node("testlist", "testlist", current_level_of_nesting, t[1:], leaf = 0)


def p_dictorsetmaker(t):
	'''dictorsetmaker : testcolonlist 
	| testlist''' 
	t[0] = Node("dictorsetmaker", "dictorsetmaker", current_level_of_nesting, t[1:], leaf = 0)


def p_testcolonlist(t):
	'''testcolonlist : test COLON test 
	| test COLON test COMMA 
	| test COLON test COMMA testcolonlist''' 
	t[0] = Node("testcolonlist", "testcolonlist", current_level_of_nesting, t[1:], leaf = 0)


def p_classdef(t):
	'''classdef : CLASS NAME COLON suite 
	| CLASS NAME LPAREN RPAREN COLON suite 
	| CLASS NAME LPAREN testlist RPAREN COLON suite''' 
	t[0] = Node("classdef", "classdef", current_level_of_nesting, t[1:], leaf = 0)


def p_arglist(t):
	'''arglist : argument 
	| argument COMMA 
	| argument COMMA arglist''' 
	t[0] = Node("arglist", "arglist", current_level_of_nesting, t[1:], leaf = 0)


def p_argument(t):
	'''argument : test 
	| test EQUAL test''' 
	t[0] = Node("argument", "argument", current_level_of_nesting, t[1:], leaf = 0)


def p_testlist1(t):
	'''testlist1 : test 
	| test COMMA testlist1''' 
	t[0] = Node("testlist1", "testlist1", current_level_of_nesting, t[1:], leaf = 0)


def p_stmts(t):
	'''stmts : stmts stmt 
	| stmt''' 
	t[0] = Node("stmts", "stmts", current_level_of_nesting, t[1:], leaf = 0)


# Ignored characters
t_ignore = " "

def t_TAB(t):
    r'\t'
    global just_saw_newline
    global current_level_of_nesting
    if just_saw_newline:
        current_level_of_nesting = 1
        just_saw_newline = 0
    else:
        current_level_of_nesting += 1

    pass

def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
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

data = open('programs/python/toy_programs/input_programs/factorial.py',"r").read()

#root = yacc.parse(data)
number=0

def printYield(root, reqpos, type):
    # Stack to store all the nodes
    # of tree
    s1 = []
    global number
    number=number+1
    global line_number
    print("Global Line Number: " + type + " " + str(line_number))
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
                        reqpos.remove(n)
                        reqpos.append(n+1)
                        s2.append(curr)
                        continue

            if type == "remove" and n in reqpos:
                # curr.get_parent().remove_child(curr)
                curr.set_missing()
                reqpos.remove(n)
                message=message + "Line no. " + str(curr.lno) + ": " + curr.value + " missing\n";

            elif type == "remove" and n not in reqpos:
                s2.append(curr)

            elif curr.get_missing() == 1:
                s2.append(curr)

            elif type == "add":
                s2.append(curr)
                if n in reqpos:

                    if curr.type=="bracket" or curr.type=="symbol":
                        temp=curr
                    if(random.random()>0.5):
                        temp=curr
                    else:
                        reqpos.remove(n)
                        valid_to_add = arithoperator
                        valid_to_add.extend(booloperator)
                        valid_to_add.extend(symbol)
                        valid_to_add.extend(bracket)
                        try:
                            valid_to_add.remove("SCOLON")
                        except:
                            pass
                        tok = choice(valid_to_add)
                        if tok in list(reserved.values()):
                            temp = Node(tok, tok.lower(), current_level_of_nesting, leaf = 1, error_node = 1)
                        else:
                            func_name = "t_" + tok
                            fake_t = temp_node("dummy", "dummy")
                            temp = eval(func_name + "(fake_t)")
                            temp = temp.value
                    temp.set_error_node()
                    curr.get_parent().add_child(temp)
                    s2.append(temp)
                    message=message + "Line no. " + str(curr.lno) + ": Unknown " + temp.value + " found.\n"
            elif type == "replace":
                if n in reqpos:
                    reqpos.remove(n)
                    # tok = choice(tokens)
                    if curr.type == "bracket":
                        while 1:
                            tok = choice(bracket)
                            func_name = "t_" + tok
                            fake_t = temp_node("dummy", "dummy")
                            temp = eval(func_name + "(fake_t)")
                            temp = temp.value
                            if temp.value != curr.value:
                                break
                    if curr.type == "reserved":
                        while 1:
                            lper=["".join(perm) for perm in itertools.permutations(curr.value)]
                            tok = choice(lper)
                            func_name = "t_" + tok
                            fake_t = temp_node("dummy", "dummy")
                            temp = eval(func_name + "(fake_t)")
                            temp = temp.value
                            if temp.value != curr.value:
                                break
                    elif curr.type == "arithoperator":
                        while 1:
                            tok = choice(symbol)
                            func_name = "t_" + tok
                            fake_t = temp_node("dummy", "dummy")
                            temp = eval(func_name + "(fake_t)")
                            temp = temp.value
                            if temp.value != curr.value:
                                break
                    elif curr.type == "eqoperator":
                        while 1:
                            tok = choice(symbol)
                            func_name = "t_" + tok
                            fake_t = temp_node("dummy", "dummy")
                            temp = eval(func_name + "(fake_t)")
                            temp = temp.value
                            if temp.value != curr.value:
                                break
                    elif curr.type == "loop":
                        while 1:
                            tok = choice(loop)
                            func_name = "t_" + tok
                            fake_t = temp_node("dummy", "dummy")
                            temp = eval(func_name + "(fake_t)")
                            temp = temp.value
                            if temp.value != curr.value:
                                break
                    elif curr.type == "selection":
                        while 1:
                            tok = choice(selection)
                            func_name = "t_" + tok
                            fake_t = temp_node("dummy", "dummy")
                            temp = eval(func_name + "(fake_t)")
                            temp = temp.value
                            if temp.value != curr.value:
                                break
                    elif curr.type == "symbol":
                        while 1:
                            tok = choice(symbol)
                            func_name = "t_" + tok
                            fake_t = temp_node("dummy", "dummy")
                            temp = eval(func_name + "(fake_t)")
                            temp = temp.value
                            if temp.value != curr.value:
                                break

                    else:
                        newl = bracket
                        newl.extend(arithoperator)
                        newl.extend(symbol)
                        newl.extend(booloperator)
                        tok = choice(newl)
                        func_name = "t_" + tok
                        fake_t = temp_node("dummy", "dummy")
                        temp = eval(func_name + "(fake_t)")
                        temp = temp.value
                    temp.set_error_node()
                    curr.get_parent().remove_child(curr)
                    curr.get_parent().add_child(temp)
                    s2.append(temp)
                    message=message +"Line no. " + str(curr.lno) + ": Unknown " + temp.value + " found.\n"
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
            code += "\n"
            code_error_colors += "\n"
            time_for_tabs = 1
        if time_for_tabs:
            for i in range(0, val.nesting):
                code += "\t"
                code_error_colors += "\t"
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
percstring= '3'
percint=int(percstring)
error_len =  percint / 100 * pgmLen
print("error_len" + str(error_len))
pgms =  8
directory= 'programs/python/toy_programs/output_programs/'

fname = 'factorial.py'.split(".")[0]
extension = 'factorial.py'.split(".")[1]

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

error_dict = {"remove": n_remove_errors, "replace" : n_replace_errors, "add" : n_add_errors}
for i in range(0,pgms):
    newroot = yacc.parse(data)
    pgmLen = getPgmLen(newroot)
    positions = [i for i in range(1,pgmLen)]
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
    pgm_errors_marked = pgm_errors_marked.replace("\n","<br/>")
    pgm_errors_marked = pgm_errors_marked.replace("\t", "&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp")
    error_list = message.split("\n")
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
        sorted_message += "Line no. "+str(e[0])+" : "+e[1]+"\n"

    f = open(directory + fname + "_" + str(i) + "." + extension , "w")
    f_err_cols = open(directory + fname + "_" + str(i) +"_errors_marked" + "." + extension , "w")
    fe=open(directory + "errors/" + fname + "_" + str(i) + "_error." + extension , "w")
    fe.write(sorted_message)
    fe.close()
    f.write(pgm)
    f_err_cols.write(pgm_errors_marked)
    f.close()
    f_err_cols.close()

