from random import choice
line_number = 1
class Node:
    def __init__(self, n_type, value, children=None, leaf=None):
        self.type = n_type
        self.value = value
        self.lno = line_number
        if children:
            self.children = children
        else:
            self.children = [ ]

        self.leaf = leaf

    def set_parent(self, parent):
        self.parent = parent

    def get_parent(self):
        return self.parent

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

eqoperator = ['EQEQUAL', 'NOTEQUAL', 'LESSEQUAL', 'PLUSEQUAL', 'MINEQUAL', 'STAREQUAL', 'SLASHEQUAL', 'PERCENTEQUAL', 'GREATEREQUAL', 'STARSTAREQUAL', 'SLASHSLASHEQUAL', 'LESS', 'GREATER', 'EQUAL']
arithoperator = ['PLUS', 'MINUS', 'STAR', 'SLASH', 'LEFTSHIFT', 'RIGHTSHIFT', 'STARSTAR', 'SLASHSLASH']
booloperator = ['VBAR', 'AMPER']
symbol = ['COLON', 'COMMA', 'SEMI', 'DOT', 'PERCENT', 'BACKQUOTE', 'CIRCUMFLEX', 'TILDE', 'AT']
bracket = ['LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LSQB', 'RSQB']
token = ['NEWLINE']
ignore = ['TAB']
reserved = {'and': 'AND', 'as': 'AS', 'assert': 'ASSERT', 'break': 'BREAK', 'class': 'CLASS', 'continue': 'CONTINUE', 'def': 'DEF', 'del': 'DEL', 'elif': 'ELIF', 'else': 'ELSE', 'except': 'EXCEPT', 'exec': 'EXEC', 'finally': 'FINALLY', 'for': 'FOR', 'from': 'FROM', 'global': 'GLOBAL', 'if': 'IF', 'import': 'IMPORT', 'in': 'IN', 'is': 'IS', 'lambda': 'LAMBDA', 'not': 'NOT', 'or': 'OR', 'pass': 'PASS', 'print': 'PRINT', 'raise': 'RAISE', 'return': 'RETURN', 'try': 'TRY', 'while': 'WHILE', 'with': 'WITH', 'yield': 'YIELD'}
tokens = ['AND', 'AS', 'ASSERT', 'BREAK', 'CLASS', 'CONTINUE', 'DEF', 'DEL', 'ELIF', 'ELSE', 'EXCEPT', 'EXEC', 'FINALLY', 'FOR', 'FROM', 'GLOBAL', 'IF', 'IMPORT', 'IN', 'IS', 'LAMBDA', 'NOT', 'OR', 'PASS', 'PRINT', 'RAISE', 'RETURN', 'TRY', 'WHILE', 'WITH', 'YIELD', 'EQEQUAL', 'NOTEQUAL', 'LESSEQUAL', 'PLUSEQUAL', 'MINEQUAL', 'STAREQUAL', 'SLASHEQUAL', 'PERCENTEQUAL', 'GREATEREQUAL', 'STARSTAREQUAL', 'SLASHSLASHEQUAL', 'LESS', 'GREATER', 'EQUAL', 'PLUS', 'MINUS', 'STAR', 'SLASH', 'LEFTSHIFT', 'RIGHTSHIFT', 'STARSTAR', 'SLASHSLASH', 'VBAR', 'AMPER', 'COLON', 'COMMA', 'SEMI', 'DOT', 'PERCENT', 'BACKQUOTE', 'CIRCUMFLEX', 'TILDE', 'AT', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LSQB', 'RSQB', 'NEWLINE', 'TAB', 'NUMBER', 'TRIPLESTRING', 'STRING', 'RAWSTRING', 'UNICODESTRING', 'BINARYNUMBER', 'OCTALNUMBER', 'HEXADECIMALNUMBER', 'NAME']

def t_NUMBER(t):
	r'\d+'
	t.type=reserved.get(t.value,'NUMBER')
	t.value = Node('NUMBER', t.value, leaf = 1)
	return t

def t_TRIPLESTRING(t):
	r'"{3}([\s\S]*?"{3}) | \'{3}([\s\S]*?\'{3})'
	t.type=reserved.get(t.value,'TRIPLESTRING')
	t.value = Node('TRIPLESTRING', t.value, leaf = 1)
	return t

def t_STRING(t):
	r'(\"(\\.|[^\"\n]|(\\\n))*\") | (\'(\\.|[^\'\n]|(\\\n))*\')'
	t.type=reserved.get(t.value,'STRING')
	t.value = Node('STRING', t.value, leaf = 1)
	return t

def t_RAWSTRING(t):
	r'[rR](\"(\\.|[^\"\n]|(\\\n))*\") | [rR](\'(\\.|[^\'\n]|(\\\n))*\')'
	t.type=reserved.get(t.value,'RAWSTRING')
	t.value = Node('RAWSTRING', t.value, leaf = 1)
	return t

def t_UNICODESTRING(t):
	r'[uU](\"(\\.|[^\"\n]|(\\\n))*\") | [uU](\'(\\.|[^\'\n]|(\\\n))*\')'
	t.type=reserved.get(t.value,'UNICODESTRING')
	t.value = Node('UNICODESTRING', t.value, leaf = 1)
	return t

def t_BINARYNUMBER(t):
	r'0[bB]([0-1]+)'
	t.type=reserved.get(t.value,'BINARYNUMBER')
	t.value = Node('BINARYNUMBER', t.value, leaf = 1)
	return t

def t_OCTALNUMBER(t):
	r'0[oO]([0-7]+)'
	t.type=reserved.get(t.value,'OCTALNUMBER')
	t.value = Node('OCTALNUMBER', t.value, leaf = 1)
	return t

def t_HEXADECIMALNUMBER(t):
	r'0[xX]([0-9a-fA-F]+)'
	t.type=reserved.get(t.value,'HEXADECIMALNUMBER')
	t.value = Node('HEXADECIMALNUMBER', t.value, leaf = 1)
	return t

def t_NAME(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	t.type=reserved.get(t.value,'NAME')
	t.value = Node('NAME', t.value, leaf = 1)
	return t

def t_EQEQUAL(t):
	r'\=='
	t.value = Node('eqoperator', '==', leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_NOTEQUAL(t):
	r'\!='
	t.value = Node('eqoperator', '!=', leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_LESSEQUAL(t):
	r'\<='
	t.value = Node('eqoperator', '<=', leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_PLUSEQUAL(t):
	r'\\+='
	t.value = Node('eqoperator', '\+=', leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_MINEQUAL(t):
	r'\-='
	t.value = Node('eqoperator', '-=', leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_STAREQUAL(t):
	r'\*='
	t.value = Node('eqoperator', '*=', leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_SLASHEQUAL(t):
	r'\/='
	t.value = Node('eqoperator', '/=', leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_PERCENTEQUAL(t):
	r'\%='
	t.value = Node('eqoperator', '%=', leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_GREATEREQUAL(t):
	r'\>='
	t.value = Node('eqoperator', '>=', leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_STARSTAREQUAL(t):
	r'\*\*='
	t.value = Node('eqoperator', '*\*=', leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_SLASHSLASHEQUAL(t):
	r'\//='
	t.value = Node('eqoperator', '//=', leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_LESS(t):
	r'\<'
	t.value = Node('eqoperator', '<', leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_GREATER(t):
	r'\>'
	t.value = Node('eqoperator', '>', leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_EQUAL(t):
	r'\='
	t.value = Node('eqoperator', '=', leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_PLUS(t):
	r'\+'
	t.value = Node('arithoperator', '+', leaf = 1)
	t.typee = 'arithoperator'
	return t

def t_MINUS(t):
	r'\-'
	t.value = Node('arithoperator', '-', leaf = 1)
	t.typee = 'arithoperator'
	return t

def t_STAR(t):
	r'\*'
	t.value = Node('arithoperator', '*', leaf = 1)
	t.typee = 'arithoperator'
	return t

def t_SLASH(t):
	r'\/'
	t.value = Node('arithoperator', '/', leaf = 1)
	t.typee = 'arithoperator'
	return t

def t_LEFTSHIFT(t):
	r'\<<'
	t.value = Node('arithoperator', '<<', leaf = 1)
	t.typee = 'arithoperator'
	return t

def t_RIGHTSHIFT(t):
	r'\>>'
	t.value = Node('arithoperator', '>>', leaf = 1)
	t.typee = 'arithoperator'
	return t

def t_STARSTAR(t):
	r'\*\*'
	t.value = Node('arithoperator', '*\*', leaf = 1)
	t.typee = 'arithoperator'
	return t

def t_SLASHSLASH(t):
	r'\//'
	t.value = Node('arithoperator', '//', leaf = 1)
	t.typee = 'arithoperator'
	return t

def t_VBAR(t):
	r'\|'
	t.value = Node('booloperator', '|', leaf = 1)
	t.typee = 'booloperator'
	return t

def t_AMPER(t):
	r'\&'
	t.value = Node('booloperator', '&', leaf = 1)
	t.typee = 'booloperator'
	return t

def t_COLON(t):
	r'\:'
	t.value = Node('symbol', ':', leaf = 1)
	t.typee = 'symbol'
	return t

def t_COMMA(t):
	r'\,'
	t.value = Node('symbol', ',', leaf = 1)
	t.typee = 'symbol'
	return t

def t_SEMI(t):
	r'\;'
	t.value = Node('symbol', ';', leaf = 1)
	t.typee = 'symbol'
	return t

def t_DOT(t):
	r'\.'
	t.value = Node('symbol', '.', leaf = 1)
	t.typee = 'symbol'
	return t

def t_PERCENT(t):
	r'\%'
	t.value = Node('symbol', '%', leaf = 1)
	t.typee = 'symbol'
	return t

def t_BACKQUOTE(t):
	r'\`'
	t.value = Node('symbol', '`', leaf = 1)
	t.typee = 'symbol'
	return t

def t_CIRCUMFLEX(t):
	r'\^'
	t.value = Node('symbol', '^', leaf = 1)
	t.typee = 'symbol'
	return t

def t_TILDE(t):
	r'\~'
	t.value = Node('symbol', '~', leaf = 1)
	t.typee = 'symbol'
	return t

def t_AT(t):
	r'\@'
	t.value = Node('symbol', '@', leaf = 1)
	t.typee = 'symbol'
	return t

def t_LPAREN(t):
	r'\('
	t.value = Node('bracket', '(', leaf = 1)
	t.typee = 'bracket'
	return t

def t_RPAREN(t):
	r'\)'
	t.value = Node('bracket', ')', leaf = 1)
	t.typee = 'bracket'
	return t

def t_LBRACE(t):
	r'\{'
	t.value = Node('bracket', '{', leaf = 1)
	t.typee = 'bracket'
	return t

def t_RBRACE(t):
	r'\}'
	t.value = Node('bracket', '}', leaf = 1)
	t.typee = 'bracket'
	return t

def t_LSQB(t):
	r'\['
	t.value = Node('bracket', '[', leaf = 1)
	t.typee = 'bracket'
	return t

def t_RSQB(t):
	r'\]'
	t.value = Node('bracket', ']', leaf = 1)
	t.typee = 'bracket'
	return t

def t_NEWLINE(t):
	r'\n+'
	global line_number
	line_number += 1
	print('LEXING with line_number: ', line_number)
	t.value = Node('token', 'n+', leaf = 1)
	t.typee = 'token'
	return t

def t_TAB(t):
	r'\t'
	t.value = Node('ignore', '\t', leaf = 1)
	pass

def p_start(t):
	'''start : file_input''' 
	global line_number
	line_number = 1
	print("beginning yacc")
	t[0] = Node("start", "start", t[1:], leaf = 0)


def p_file_input(t):
	'''file_input : single_stmt''' 
	t[0] = Node("file_input", "file_input", t[1:], leaf = 0)


def p_single_stmt(t):
	'''single_stmt : single_stmt NEWLINE 
	| single_stmt stmt 
	|''' 
	t[0] = Node("single_stmt", "single_stmt", t[1:], leaf = 0)


def p_funcdef(t):
	'''funcdef : DEF NAME parameters COLON suite''' 
	t[0] = Node("funcdef", "funcdef", t[1:], leaf = 0)


def p_parameters(t):
	'''parameters : LPAREN varargslist RPAREN''' 
	t[0] = Node("parameters", "parameters", t[1:], leaf = 0)


def p_varargslist(t):
	'''varargslist : 
	| fpdef EQUAL test fpdeflist COMMA 
	| fpdef EQUAL test fpdeflist 
	| fpdef fpdeflist COMMA 
	| fpdef fpdeflist''' 
	t[0] = Node("varargslist", "varargslist", t[1:], leaf = 0)


def p_fpdeflist(t):
	'''fpdeflist : 
	| fpdeflist COMMA fpdef 
	| fpdeflist COMMA fpdef EQUAL test''' 
	t[0] = Node("fpdeflist", "fpdeflist", t[1:], leaf = 0)


def p_fpdef(t):
	'''fpdef : NAME  
	| LPAREN fplist RPAREN''' 
	t[0] = Node("fpdef", "fpdef", t[1:], leaf = 0)


def p_fplist(t):
	'''fplist : fpdef fplist1 COMMA 
	| fpdef fplist1''' 
	t[0] = Node("fplist", "fplist", t[1:], leaf = 0)


def p_fplist1(t):
	'''fplist1 : 
	| fplist1 COMMA fpdef''' 
	t[0] = Node("fplist1", "fplist1", t[1:], leaf = 0)


def p_stmt(t):
	'''stmt : simple_stmt 
	| compound_stmt''' 
	t[0] = Node("stmt", "stmt", t[1:], leaf = 0)


def p_simple_stmt(t):
	'''simple_stmt : small_stmts NEWLINE 
	| small_stmts SEMI NEWLINE''' 
	t[0] = Node("simple_stmt", "simple_stmt", t[1:], leaf = 0)


def p_small_stmts(t):
	'''small_stmts : small_stmts SEMI small_stmt 
	| small_stmt''' 
	t[0] = Node("small_stmts", "small_stmts", t[1:], leaf = 0)


def p_small_stmt(t):
	'''small_stmt : flow_stmt 
	| expr_stmt 
	| print_stmt 
	| pass_stmt 
	| import_stmt 
	| global_stmt 
	| assert_stmt''' 
	t[0] = Node("small_stmt", "small_stmt", t[1:], leaf = 0)


def p_expr_stmt(t):
	'''expr_stmt : testlist augassign testlist 
	| testlist eqtestlist''' 
	t[0] = Node("expr_stmt", "expr_stmt", t[1:], leaf = 0)


def p_eqtestlist(t):
	'''eqtestlist : 
	| eqtestlist EQUAL testlist''' 
	t[0] = Node("eqtestlist", "eqtestlist", t[1:], leaf = 0)


def p_augassign(t):
	'''augassign : PLUSEQUAL  
	| MINEQUAL  
	| STAREQUAL  
	| SLASHEQUAL  
	| PERCENTEQUAL  
	| STARSTAREQUAL  
	| SLASHSLASHEQUAL''' 
	t[0] = Node("augassign", "augassign", t[1:], leaf = 0)


def p_print_stmt(t):
	'''print_stmt : PRINT 
	| PRINT testlist''' 
	t[0] = Node("print_stmt", "print_stmt", t[1:], leaf = 0)


def p_pass_stmt(t):
	'''pass_stmt : PASS''' 
	t[0] = Node("pass_stmt", "pass_stmt", t[1:], leaf = 0)


def p_flow_stmt(t):
	'''flow_stmt : break_stmt 
	| continue_stmt 
	| return_stmt''' 
	t[0] = Node("flow_stmt", "flow_stmt", t[1:], leaf = 0)


def p_break_stmt(t):
	'''break_stmt : BREAK''' 
	t[0] = Node("break_stmt", "break_stmt", t[1:], leaf = 0)


def p_continue_stmt(t):
	'''continue_stmt : CONTINUE''' 
	t[0] = Node("continue_stmt", "continue_stmt", t[1:], leaf = 0)


def p_return_stmt(t):
	'''return_stmt : RETURN  
	| RETURN testlist''' 
	t[0] = Node("return_stmt", "return_stmt", t[1:], leaf = 0)


def p_import_stmt(t):
	'''import_stmt : IMPORT NAME 
	| IMPORT NAME AS NAME''' 
	t[0] = Node("import_stmt", "import_stmt", t[1:], leaf = 0)


def p_global_stmt(t):
	'''global_stmt : GLOBAL NAME namelist''' 
	t[0] = Node("global_stmt", "global_stmt", t[1:], leaf = 0)


def p_namelist(t):
	'''namelist : 
	| COMMA NAME namelist''' 
	t[0] = Node("namelist", "namelist", t[1:], leaf = 0)


def p_assert_stmt(t):
	'''assert_stmt : ASSERT testlist''' 
	t[0] = Node("assert_stmt", "assert_stmt", t[1:], leaf = 0)


def p_compound_stmt(t):
	'''compound_stmt : if_stmt 
	| for_stmt 
	| while_stmt 
	| funcdef 
	| classdef''' 
	t[0] = Node("compound_stmt", "compound_stmt", t[1:], leaf = 0)


def p_if_stmt(t):
	'''if_stmt : IF test COLON suite elif_list 
	| IF test COLON suite elif_list ELSE COLON suite''' 
	t[0] = Node("if_stmt", "if_stmt", t[1:], leaf = 0)


def p_elif_list(t):
	'''elif_list : 
	| ELIF test COLON suite elif_list''' 
	t[0] = Node("elif_list", "elif_list", t[1:], leaf = 0)


def p_while_stmt(t):
	'''while_stmt : WHILE test COLON suite  
	| WHILE test COLON suite ELSE COLON suite''' 
	t[0] = Node("while_stmt", "while_stmt", t[1:], leaf = 0)


def p_for_stmt(t):
	'''for_stmt : FOR exprlist IN testlist COLON suite 
	| FOR exprlist IN testlist COLON suite ELSE COLON suite''' 
	t[0] = Node("for_stmt", "for_stmt", t[1:], leaf = 0)


def p_suite(t):
	'''suite : simple_stmt 
	| NEWLINE stmts''' 
	t[0] = Node("suite", "suite", t[1:], leaf = 0)


def p_test(t):
	'''test : or_test 
	| or_test IF or_test ELSE test''' 
	t[0] = Node("test", "test", t[1:], leaf = 0)


def p_or_test(t):
	'''or_test : and_test ortestlist''' 
	t[0] = Node("or_test", "or_test", t[1:], leaf = 0)


def p_ortestlist(t):
	'''ortestlist : 
	| OR and_test ortestlist''' 
	t[0] = Node("ortestlist", "ortestlist", t[1:], leaf = 0)


def p_and_test(t):
	'''and_test : not_test andtestlist''' 
	t[0] = Node("and_test", "and_test", t[1:], leaf = 0)


def p_andtestlist(t):
	'''andtestlist : 
	| AND not_test andtestlist''' 
	t[0] = Node("andtestlist", "andtestlist", t[1:], leaf = 0)


def p_not_test(t):
	'''not_test : NOT not_test 
	| comparison''' 
	t[0] = Node("not_test", "not_test", t[1:], leaf = 0)


def p_comparison(t):
	'''comparison : expr compexprlist''' 
	t[0] = Node("comparison", "comparison", t[1:], leaf = 0)


def p_compexprlist(t):
	'''compexprlist : 
	| comp_op expr compexprlist''' 
	t[0] = Node("compexprlist", "compexprlist", t[1:], leaf = 0)


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
	t[0] = Node("comp_op", "comp_op", t[1:], leaf = 0)


def p_expr(t):
	'''expr : xor_expr xorexprlist''' 
	t[0] = Node("expr", "expr", t[1:], leaf = 0)


def p_xorexprlist(t):
	'''xorexprlist : 
	| VBAR xor_expr xorexprlist''' 
	t[0] = Node("xorexprlist", "xorexprlist", t[1:], leaf = 0)


def p_xor_expr(t):
	'''xor_expr : and_expr andexprlist''' 
	t[0] = Node("xor_expr", "xor_expr", t[1:], leaf = 0)


def p_andexprlist(t):
	'''andexprlist : 
	| CIRCUMFLEX and_expr andexprlist''' 
	t[0] = Node("andexprlist", "andexprlist", t[1:], leaf = 0)


def p_and_expr(t):
	'''and_expr : shift_expr shiftexprlist''' 
	t[0] = Node("and_expr", "and_expr", t[1:], leaf = 0)


def p_shiftexprlist(t):
	'''shiftexprlist : 
	| AMPER shift_expr shiftexprlist''' 
	t[0] = Node("shiftexprlist", "shiftexprlist", t[1:], leaf = 0)


def p_shift_expr(t):
	'''shift_expr : arith_expr arithexprlist''' 
	t[0] = Node("shift_expr", "shift_expr", t[1:], leaf = 0)


def p_arithexprlist(t):
	'''arithexprlist : 
	| LEFTSHIFT arith_expr arithexprlist 
	| RIGHTSHIFT arith_expr arithexprlist''' 
	t[0] = Node("arithexprlist", "arithexprlist", t[1:], leaf = 0)


def p_arith_expr(t):
	'''arith_expr : term termlist''' 
	t[0] = Node("arith_expr", "arith_expr", t[1:], leaf = 0)


def p_termlist(t):
	'''termlist : 
	| PLUS term termlist 
	| MINUS term termlist''' 
	t[0] = Node("termlist", "termlist", t[1:], leaf = 0)


def p_term(t):
	'''term : factor factorlist''' 
	t[0] = Node("term", "term", t[1:], leaf = 0)


def p_factorlist(t):
	'''factorlist : 
	| STAR factor factorlist 
	| SLASH factor factorlist 
	| PERCENT factor factorlist 
	| SLASHSLASH factor factorlist''' 
	t[0] = Node("factorlist", "factorlist", t[1:], leaf = 0)


def p_factor(t):
	'''factor : power 
	| PLUS factor 
	| MINUS factor 
	| TILDE factor''' 
	t[0] = Node("factor", "factor", t[1:], leaf = 0)


def p_power(t):
	'''power : atom trailerlist 
	| atom trailerlist STARSTAR factor''' 
	t[0] = Node("power", "power", t[1:], leaf = 0)


def p_trailerlist(t):
	'''trailerlist : 
	| trailer trailerlist''' 
	t[0] = Node("trailerlist", "trailerlist", t[1:], leaf = 0)


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
	t[0] = Node("atom", "atom", t[1:], leaf = 0)


def p_stringlist(t):
	'''stringlist : STRING  
	| STRING stringlist 
	| TRIPLESTRING 
	| TRIPLESTRING stringlist''' 
	t[0] = Node("stringlist", "stringlist", t[1:], leaf = 0)


def p_listmaker(t):
	'''listmaker : testlist''' 
	t[0] = Node("listmaker", "listmaker", t[1:], leaf = 0)


def p_testlist_comp(t):
	'''testlist_comp : testlist''' 
	t[0] = Node("testlist_comp", "testlist_comp", t[1:], leaf = 0)


def p_trailer(t):
	'''trailer : LPAREN RPAREN 
	| LPAREN arglist RPAREN 
	| LSQB subscriptlist RSQB 
	| DOT NAME''' 
	t[0] = Node("trailer", "trailer", t[1:], leaf = 0)


def p_subscriptlist(t):
	'''subscriptlist : subscript 
	| subscript COMMA 
	| subscript COMMA subscriptlist''' 
	t[0] = Node("subscriptlist", "subscriptlist", t[1:], leaf = 0)


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
	t[0] = Node("subscript", "subscript", t[1:], leaf = 0)


def p_sliceop(t):
	'''sliceop : COLON 
	| COLON test''' 
	t[0] = Node("sliceop", "sliceop", t[1:], leaf = 0)


def p_exprlist(t):
	'''exprlist : expr 
	| expr COMMA 
	| expr COMMA exprlist''' 
	t[0] = Node("exprlist", "exprlist", t[1:], leaf = 0)


def p_testlist(t):
	'''testlist : test 
	| test COMMA 
	| test COMMA testlist''' 
	t[0] = Node("testlist", "testlist", t[1:], leaf = 0)


def p_dictorsetmaker(t):
	'''dictorsetmaker : testcolonlist 
	| testlist''' 
	t[0] = Node("dictorsetmaker", "dictorsetmaker", t[1:], leaf = 0)


def p_testcolonlist(t):
	'''testcolonlist : test COLON test 
	| test COLON test COMMA 
	| test COLON test COMMA testcolonlist''' 
	t[0] = Node("testcolonlist", "testcolonlist", t[1:], leaf = 0)


def p_classdef(t):
	'''classdef : CLASS NAME COLON suite 
	| CLASS NAME LPAREN RPAREN COLON suite 
	| CLASS NAME LPAREN testlist RPAREN COLON suite''' 
	t[0] = Node("classdef", "classdef", t[1:], leaf = 0)


def p_arglist(t):
	'''arglist : argument 
	| argument COMMA 
	| argument COMMA arglist''' 
	t[0] = Node("arglist", "arglist", t[1:], leaf = 0)


def p_argument(t):
	'''argument : test 
	| test EQUAL test''' 
	t[0] = Node("argument", "argument", t[1:], leaf = 0)


def p_testlist1(t):
	'''testlist1 : test 
	| test COMMA testlist1''' 
	t[0] = Node("testlist1", "testlist1", t[1:], leaf = 0)


def p_stmts(t):
	'''stmts : stmts stmt 
	| stmt''' 
	t[0] = Node("stmts", "stmts", t[1:], leaf = 0)


# Ignored characters
t_ignore = " "

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

data = open('../programs/python/toy_programs/input_programs/factorial.py',"r").read()

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
                curr.get_parent().remove_child(curr)
                reqpos.remove(n)
                message=message + "Line no. " + str(curr.lno) + ": " + curr.value + " missing\n";

            elif type == "remove" and n not in reqpos:
                s2.append(curr)

            elif type == "add":
                s2.append(curr)
                if n in reqpos:
                    reqpos.remove(n)
                    valid_to_add = arithoperator
                    valid_to_add.extend(booloperator)
                    valid_to_add.extend(symbol)
                    valid_to_add.extend(bracket)
                    tok = choice(valid_to_add)
                    if tok in list(reserved.values()):
                        temp = Node(tok, tok.lower(), leaf = 1)
                    else:
                        func_name = "t_" + tok
                        fake_t = temp_node("dummy", "dummy")
                        temp = eval(func_name + "(fake_t)")
                        temp = temp.value
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
                            lper=["".join(perm) for perm in itertools.permutations(curr)]
                            tok = choice(lper)
                            func_name = "t_" + tok
                            fake_t = temp_node("dummy", "dummy")
                            temp = eval(func_name + "(fake_t)")
                            temp = temp.value
                            if temp.value != curr.value:
                                break
                    elif curr.type == "arithoperator":
                        while 1:
                            tok = choice(arithoperator)
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
                        # temp = Node("dummy", "errnode", leaf = 1)
                    curr.get_parent().remove_child(curr)
                    curr.get_parent().add_child(temp)
                    s2.append(temp)
                    message=message +"Line no. " + str(curr.lno) + ": Unknown " + temp.value + " found.\n"
                else:
                    s2.append(curr)


    # Print all the leaf nodes
    level = 0
    s = ""
    line_no = 0
    while len(s2) != 0:
        val = s2.pop()
        if val.lno > line_no:
            line_no = val.lno
            s += "\n"
        s = s + "" + val.value + " "

    return s, message, root


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
pgms =  2
directory= '../programs/python/toy_programs/output_programs/'
#directory = "../programs/python/functions/output_programs/"
#directory2 = "../programs/python/functions/output_programs/errors"

fname = 'factorial.py'.split(".")[0]
extension = 'factorial.py'.split(".")[1]
n_add_errors = 1
n_remove_errors = 3
n_replace_errors = 1

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
        pgm, message1, newroot = printYield(newroot, reqpos, key)
        message += message1
    pgm = pgm.replace("n+", "")

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
    fe=open(directory + "errors/" + fname + "_" + str(i) + "_error." + extension , "w")
    fe.write(sorted_message)
    fe.close()
    f.write(pgm)
    f.close()

