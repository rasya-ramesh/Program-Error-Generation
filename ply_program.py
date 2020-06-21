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
eqoperator = ['EQUALS', 'RIGHT_ASSIGN', 'LEFT_ASSIGN', 'ADD_ASSIGN', 'SUB_ASSIGN', 'MUL_ASSIGN', 'DIV_ASSIGN', 'MOD_ASSIGN', 'AND_ASSIGN', 'XOR_ASSIGN', 'OR_ASSIGN', 'LE_OP', 'GE_OP', 'EQ_OP', 'NE_OP', 'GT_OP', 'LT_OP']
arithoperator = ['PLUS', 'MINUS', 'DIVIDES', 'TIMES', 'MODULUS', 'RIGHT_OP', 'LEFT_OP', 'INC_OP', 'DEC_OP']
booloperator = ['AMP', 'OR', 'AND_OP', 'OR_OP']
bracket = ['LPAREN', 'RPAREN', 'LFPAREN', 'RFPAREN', 'LSQUARE', 'RSQUARE']
token = ['ELLIPSIS', 'ALIGNAS', 'ALIGNOF', 'ATOMIC', 'COMPLEX', 'GENERIC', 'IMAGINARY', 'NORETURN', 'STATIC_ASSERT', 'THREAD_LOCAL', 'FUNC_NAME']
symbol = ['COMMA', 'COLON', 'SCOLON', 'DOT', 'TILDE', 'XOR', 'NOT', 'QMARK', 'PTR_OP']
ignore = ['NEWLINE']
selection=['if', 'else', 'switch', 'case']
loop=['while', 'do', 'for']
reserved = {'void': 'VOID', 'int': 'INT', 'float': 'FLOAT', 'bool': 'BOOL', 'char': 'CHAR', 'double': 'DOUBLE', 'else': 'ELSE', 'if': 'IF', 'while': 'WHILE', 'do': 'DO', 'for': 'FOR', 'auto': 'AUTO', 'break': 'BREAK', 'case': 'CASE', 'const': 'CONST', 'continue': 'CONTINUE', 'default': 'DEFAULT', 'goto': 'GOTO', 'enum': 'ENUM', 'extern': 'EXTERN', 'long': 'LONG', 'register': 'REGISTER', 'return': 'RETURN', 'short': 'SHORT', 'signed': 'SIGNED', 'sizeof': 'SIZEOF', 'static': 'STATIC', 'struct': 'STRUCT', 'typedef': 'TYPEDEF', 'switch': 'SWITCH', 'union': 'UNION', 'unsigned': 'UNSIGNED', 'volatile': 'VOLATILE'}
selection = {'if': 'IF', 'else': 'ELSE', 'switch': 'SWITCH', 'case': 'CASE'}
loop = {'for': 'FOR', 'while': 'WHILE', 'do': 'DO'}
tokens = ['VOID', 'INT', 'FLOAT', 'BOOL', 'CHAR', 'DOUBLE', 'ELSE', 'IF', 'WHILE', 'DO', 'FOR', 'AUTO', 'BREAK', 'CASE', 'CONST', 'CONTINUE', 'DEFAULT', 'GOTO', 'ENUM', 'EXTERN', 'LONG', 'REGISTER', 'RETURN', 'SHORT', 'SIGNED', 'SIZEOF', 'STATIC', 'STRUCT', 'TYPEDEF', 'SWITCH', 'UNION', 'UNSIGNED', 'VOLATILE', 'EQUALS', 'RIGHT_ASSIGN', 'LEFT_ASSIGN', 'ADD_ASSIGN', 'SUB_ASSIGN', 'MUL_ASSIGN', 'DIV_ASSIGN', 'MOD_ASSIGN', 'AND_ASSIGN', 'XOR_ASSIGN', 'OR_ASSIGN', 'LE_OP', 'GE_OP', 'EQ_OP', 'NE_OP', 'GT_OP', 'LT_OP', 'PLUS', 'MINUS', 'DIVIDES', 'TIMES', 'MODULUS', 'RIGHT_OP', 'LEFT_OP', 'INC_OP', 'DEC_OP', 'AMP', 'OR', 'AND_OP', 'OR_OP', 'LPAREN', 'RPAREN', 'LFPAREN', 'RFPAREN', 'LSQUARE', 'RSQUARE', 'ELLIPSIS', 'ALIGNAS', 'ALIGNOF', 'ATOMIC', 'COMPLEX', 'GENERIC', 'IMAGINARY', 'NORETURN', 'STATIC_ASSERT', 'THREAD_LOCAL', 'FUNC_NAME', 'COMMA', 'COLON', 'SCOLON', 'DOT', 'TILDE', 'XOR', 'NOT', 'QMARK', 'PTR_OP', 'NEWLINE', 'NUMBER', 'IDENTIFIER', 'STRING_LITERAL', 'I_CONSTANT', 'F_CONSTANT']

def t_NUMBER(t):
	r'\d+'
	t.type=reserved.get(t.value,'NUMBER')
	global current_level_of_nesting
	t.value = Node('NUMBER', t.value, current_level_of_nesting, leaf = 1)
	return t

def t_EQ_OP(t):
	r'\=='
	t.type=reserved.get(t.value,'EQ_OP')
	global current_level_of_nesting
	t.value = Node('EQ_OP', t.value, current_level_of_nesting, leaf = 1)
	return t

def t_MUL_ASSIGN(t):
	r'\*='
	t.type=reserved.get(t.value,'MUL_ASSIGN')
	global current_level_of_nesting
	t.value = Node('MUL_ASSIGN', t.value, current_level_of_nesting, leaf = 1)
	return t

def t_NE_OP(t):
	r'\!='
	t.type=reserved.get(t.value,'NE_OP')
	global current_level_of_nesting
	t.value = Node('NE_OP', t.value, current_level_of_nesting, leaf = 1)
	return t

def t_GE_OP(t):
	r'\>='
	t.type=reserved.get(t.value,'GE_OP')
	global current_level_of_nesting
	t.value = Node('GE_OP', t.value, current_level_of_nesting, leaf = 1)
	return t

def t_LE_OP(t):
	r'\<='
	t.type=reserved.get(t.value,'LE_OP')
	global current_level_of_nesting
	t.value = Node('LE_OP', t.value, current_level_of_nesting, leaf = 1)
	return t

def t_DOT(t):
	r'\.'
	t.type=reserved.get(t.value,'DOT')
	global current_level_of_nesting
	t.value = Node('DOT', t.value, current_level_of_nesting, leaf = 1)
	return t

def t_PTR_OP(t):
	r'\->'
	t.type=reserved.get(t.value,'PTR_OP')
	global current_level_of_nesting
	t.value = Node('PTR_OP', t.value, current_level_of_nesting, leaf = 1)
	return t

def t_IDENTIFIER(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	t.type=reserved.get(t.value,'IDENTIFIER')
	global current_level_of_nesting
	t.value = Node('IDENTIFIER', t.value, current_level_of_nesting, leaf = 1)
	return t

def t_STRING_LITERAL(t):
	r'\"(\\.|[^"\\])*\"'
	t.type=reserved.get(t.value,'STRING_LITERAL')
	global current_level_of_nesting
	t.value = Node('STRING_LITERAL', t.value, current_level_of_nesting, leaf = 1)
	return t

def t_I_CONSTANT(t):
	r'{(0[xX])}{[a-fA-F0-9]}+{(((u|U)(l|[a-zA-Z_]|ll|[a-zA-Z_][a-zA-Z_])?)|((l|[a-zA-Z_]|ll|[a-zA-Z_][a-zA-Z_])(u|U)?))}? | {[1-9]}{[0-9]}*{(((u|U)(l|[a-zA-Z_]|ll|[a-zA-Z_][a-zA-Z_])?)|((l|[a-zA-Z_]|ll|[a-zA-Z_][a-zA-Z_])(u|U)?))}? | "0"{[0-7]}*{(((u|U)(l|[a-zA-Z_]|ll|[a-zA-Z_][a-zA-Z_])?)|((l|[a-zA-Z_]|ll|[a-zA-Z_][a-zA-Z_])(u|U)?))}? | {(u|U|[a-zA-Z_])}?"\'"([^\'\\\n]|{(\\([\'"\?\\abfnrtv]|[0-7]{1,3}|x[a-fA-F0-9]+))})+"\'"'
	t.type=reserved.get(t.value,'I_CONSTANT')
	global current_level_of_nesting
	t.value = Node('I_CONSTANT', t.value, current_level_of_nesting, leaf = 1)
	return t

def t_F_CONSTANT(t):
	r'{[0-9]}+{([Ee][+-]?{[0-9]}+)}{(f|F|l|[a-zA-Z_])}? | {[0-9]}*"."{[0-9]}+{([Ee][+-]?{[0-9]}+)}?{(f|F|l|[a-zA-Z_])}? | {[0-9]}+"."{([Ee][+-]?{[0-9]}+)}?{(f|F|l|[a-zA-Z_])}? | {(0[xX])}{[a-fA-F0-9]}+{([Pp][+-]?{[0-9]}+)}{(f|F|l|[a-zA-Z_])}? | {(0[xX])}{[a-fA-F0-9]}*"."{[a-fA-F0-9]}+{([Pp][+-]?{[0-9]}+)}{(f|F|l|[a-zA-Z_])}? | {(0[xX])}{[a-fA-F0-9]}+"."{([Pp][+-]?{[0-9]}+)}{(f|F|l|[a-zA-Z_])}?'
	t.type=reserved.get(t.value,'F_CONSTANT')
	global current_level_of_nesting
	t.value = Node('F_CONSTANT', t.value, current_level_of_nesting, leaf = 1)
	return t

def t_EQUALS(t):
	r'\='
	global current_level_of_nesting
	t.value = Node('eqoperator', '=', current_level_of_nesting, leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_RIGHT_ASSIGN(t):
	r'\>>='
	global current_level_of_nesting
	t.value = Node('eqoperator', '>>=', current_level_of_nesting, leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_LEFT_ASSIGN(t):
	r'\<<='
	global current_level_of_nesting
	t.value = Node('eqoperator', '<<=', current_level_of_nesting, leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_ADD_ASSIGN(t):
	r'\+='
	global current_level_of_nesting
	t.value = Node('eqoperator', '+=', current_level_of_nesting, leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_SUB_ASSIGN(t):
	r'\-='
	global current_level_of_nesting
	t.value = Node('eqoperator', '-=', current_level_of_nesting, leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_DIV_ASSIGN(t):
	r'\/='
	global current_level_of_nesting
	t.value = Node('eqoperator', '/=', current_level_of_nesting, leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_MOD_ASSIGN(t):
	r'\%='
	global current_level_of_nesting
	t.value = Node('eqoperator', '%=', current_level_of_nesting, leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_AND_ASSIGN(t):
	r'\&='
	global current_level_of_nesting
	t.value = Node('eqoperator', '&=', current_level_of_nesting, leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_XOR_ASSIGN(t):
	r'\^='
	global current_level_of_nesting
	t.value = Node('eqoperator', '^=', current_level_of_nesting, leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_OR_ASSIGN(t):
	r'\|='
	global current_level_of_nesting
	t.value = Node('eqoperator', '|=', current_level_of_nesting, leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_GT_OP(t):
	r'\>'
	global current_level_of_nesting
	t.value = Node('eqoperator', '>', current_level_of_nesting, leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_LT_OP(t):
	r'\<'
	global current_level_of_nesting
	t.value = Node('eqoperator', '<', current_level_of_nesting, leaf = 1)
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

def t_DIVIDES(t):
	r'\/'
	global current_level_of_nesting
	t.value = Node('arithoperator', '/', current_level_of_nesting, leaf = 1)
	t.typee = 'arithoperator'
	return t

def t_TIMES(t):
	r'\*'
	global current_level_of_nesting
	t.value = Node('arithoperator', '*', current_level_of_nesting, leaf = 1)
	t.typee = 'arithoperator'
	return t

def t_MODULUS(t):
	r'\%'
	global current_level_of_nesting
	t.value = Node('arithoperator', '%', current_level_of_nesting, leaf = 1)
	t.typee = 'arithoperator'
	return t

def t_RIGHT_OP(t):
	r'>>'
	global current_level_of_nesting
	t.value = Node('arithoperator', '>', current_level_of_nesting, leaf = 1)
	t.typee = 'arithoperator'
	return t

def t_LEFT_OP(t):
	r'<<'
	global current_level_of_nesting
	t.value = Node('arithoperator', '<', current_level_of_nesting, leaf = 1)
	t.typee = 'arithoperator'
	return t

def t_INC_OP(t):
	r'\++'
	global current_level_of_nesting
	t.value = Node('arithoperator', '++', current_level_of_nesting, leaf = 1)
	t.typee = 'arithoperator'
	return t

def t_DEC_OP(t):
	r'\--'
	global current_level_of_nesting
	t.value = Node('arithoperator', '--', current_level_of_nesting, leaf = 1)
	t.typee = 'arithoperator'
	return t

def t_AMP(t):
	r'\&'
	global current_level_of_nesting
	t.value = Node('booloperator', '&', current_level_of_nesting, leaf = 1)
	t.typee = 'booloperator'
	return t

def t_OR(t):
	r'\|'
	global current_level_of_nesting
	t.value = Node('booloperator', '|', current_level_of_nesting, leaf = 1)
	t.typee = 'booloperator'
	return t

def t_AND_OP(t):
	r'\&&'
	global current_level_of_nesting
	t.value = Node('booloperator', '&&', current_level_of_nesting, leaf = 1)
	t.typee = 'booloperator'
	return t

def t_OR_OP(t):
	r'\|\|'
	global current_level_of_nesting
	t.value = Node('booloperator', '|\|', current_level_of_nesting, leaf = 1)
	t.typee = 'booloperator'
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

def t_LFPAREN(t):
	r'\{'
	global current_level_of_nesting
	t.value = Node('bracket', '{', current_level_of_nesting, leaf = 1)
	t.typee = 'bracket'
	return t

def t_RFPAREN(t):
	r'\}'
	global current_level_of_nesting
	t.value = Node('bracket', '}', current_level_of_nesting, leaf = 1)
	t.typee = 'bracket'
	return t

def t_LSQUARE(t):
	r'\['
	global current_level_of_nesting
	t.value = Node('bracket', '[', current_level_of_nesting, leaf = 1)
	t.typee = 'bracket'
	return t

def t_RSQUARE(t):
	r'\]'
	global current_level_of_nesting
	t.value = Node('bracket', ']', current_level_of_nesting, leaf = 1)
	t.typee = 'bracket'
	return t

def t_ELLIPSIS(t):
	r'\...'
	global current_level_of_nesting
	t.value = Node('token', '...', current_level_of_nesting, leaf = 1)
	t.typee = 'token'
	return t

def t_ALIGNAS(t):
	r'_Alignas'
	global current_level_of_nesting
	t.value = Node('token', 'Alignas', current_level_of_nesting, leaf = 1)
	t.typee = 'token'
	return t

def t_ALIGNOF(t):
	r'_Alignof'
	global current_level_of_nesting
	t.value = Node('token', 'Alignof', current_level_of_nesting, leaf = 1)
	t.typee = 'token'
	return t

def t_ATOMIC(t):
	r'_Atomic'
	global current_level_of_nesting
	t.value = Node('token', 'Atomic', current_level_of_nesting, leaf = 1)
	t.typee = 'token'
	return t

def t_COMPLEX(t):
	r'_Complex'
	global current_level_of_nesting
	t.value = Node('token', 'Complex', current_level_of_nesting, leaf = 1)
	t.typee = 'token'
	return t

def t_GENERIC(t):
	r'_Generic'
	global current_level_of_nesting
	t.value = Node('token', 'Generic', current_level_of_nesting, leaf = 1)
	t.typee = 'token'
	return t

def t_IMAGINARY(t):
	r'_Imaginary'
	global current_level_of_nesting
	t.value = Node('token', 'Imaginary', current_level_of_nesting, leaf = 1)
	t.typee = 'token'
	return t

def t_NORETURN(t):
	r'_Noreturn'
	global current_level_of_nesting
	t.value = Node('token', 'Noreturn', current_level_of_nesting, leaf = 1)
	t.typee = 'token'
	return t

def t_STATIC_ASSERT(t):
	r'_Static_assert'
	global current_level_of_nesting
	t.value = Node('token', 'Static_assert', current_level_of_nesting, leaf = 1)
	t.typee = 'token'
	return t

def t_THREAD_LOCAL(t):
	r'_Thread_local'
	global current_level_of_nesting
	t.value = Node('token', 'Thread_local', current_level_of_nesting, leaf = 1)
	t.typee = 'token'
	return t

def t_FUNC_NAME(t):
	r'__func__'
	global current_level_of_nesting
	t.value = Node('token', '_func__', current_level_of_nesting, leaf = 1)
	t.typee = 'token'
	return t

def t_COMMA(t):
	r'\,'
	global current_level_of_nesting
	t.value = Node('symbol', ',', current_level_of_nesting, leaf = 1)
	t.typee = 'symbol'
	return t

def t_COLON(t):
	r'\:'
	global current_level_of_nesting
	t.value = Node('symbol', ':', current_level_of_nesting, leaf = 1)
	t.typee = 'symbol'
	return t

def t_SCOLON(t):
	r'\;'
	global current_level_of_nesting
	t.value = Node('symbol', ';', current_level_of_nesting, leaf = 1)
	t.typee = 'symbol'
	return t

def t_TILDE(t):
	r'\~'
	global current_level_of_nesting
	t.value = Node('symbol', '~', current_level_of_nesting, leaf = 1)
	t.typee = 'symbol'
	return t

def t_XOR(t):
	r'\^'
	global current_level_of_nesting
	t.value = Node('symbol', '^', current_level_of_nesting, leaf = 1)
	t.typee = 'symbol'
	return t

def t_NOT(t):
	r'\!'
	global current_level_of_nesting
	t.value = Node('symbol', '!', current_level_of_nesting, leaf = 1)
	t.typee = 'symbol'
	return t

def t_QMARK(t):
	r'\?'
	global current_level_of_nesting
	t.value = Node('symbol', '?', current_level_of_nesting, leaf = 1)
	t.typee = 'symbol'
	return t

def t_NEWLINE(t):
	r'\n'
	global current_level_of_nesting
	global line_number
	global just_saw_newline
	just_saw_newline = 1
	current_level_of_nesting = 0
	line_number += 1
	t.value = Node('ignore', 'n', current_level_of_nesting, leaf = 1)
	pass

def p_start(t):
	'''start : translation_unit''' 
	global line_number
	global current_level_of_nesting
	line_number = 1
	print("beginning yacc")
	t[0] = Node("start", "start", current_level_of_nesting, t[1:], leaf = 0)


def p_translation_unit(t):
	'''translation_unit : external_declaration
	| translation_unit external_declaration''' 
	t[0] = Node("translation_unit", "translation_unit", current_level_of_nesting, t[1:], leaf = 0)


def p_external_declaration(t):
	'''external_declaration : function_definition
	| declaration''' 
	t[0] = Node("external_declaration", "external_declaration", current_level_of_nesting, t[1:], leaf = 0)


def p_function_definition(t):
	'''function_definition : declaration_specifiers declarator declaration_list compound_statement
	| declaration_specifiers declarator compound_statement''' 
	t[0] = Node("function_definition", "function_definition", current_level_of_nesting, t[1:], leaf = 0)


def p_declaration_list(t):
	'''declaration_list : declaration
	| declaration_list declaration''' 
	t[0] = Node("declaration_list", "declaration_list", current_level_of_nesting, t[1:], leaf = 0)


def p_primary_expression(t):
	'''primary_expression : IDENTIFIER
	| constant 
	| string 
	| LPAREN expression RPAREN
	| generic_selection 
	| NUMBER''' 
	t[0] = Node("primary_expression", "primary_expression", current_level_of_nesting, t[1:], leaf = 0)


def p_constant(t):
	'''constant : I_CONSTANT 
	| F_CONSTANT''' 
	t[0] = Node("constant", "constant", current_level_of_nesting, t[1:], leaf = 0)


def p_enumeration_constant(t):
	'''enumeration_constant : IDENTIFIER''' 
	t[0] = Node("enumeration_constant", "enumeration_constant", current_level_of_nesting, t[1:], leaf = 0)


def p_string(t):
	'''string : STRING_LITERAL
	| FUNC_NAME''' 
	t[0] = Node("string", "string", current_level_of_nesting, t[1:], leaf = 0)


def p_generic_selection(t):
	'''generic_selection : GENERIC LPAREN assignment_expression COMMA generic_assoc_list RPAREN''' 
	t[0] = Node("generic_selection", "generic_selection", current_level_of_nesting, t[1:], leaf = 0)


def p_generic_assoc_list(t):
	'''generic_assoc_list : generic_association
	| generic_assoc_list COMMA generic_association''' 
	t[0] = Node("generic_assoc_list", "generic_assoc_list", current_level_of_nesting, t[1:], leaf = 0)


def p_generic_association(t):
	'''generic_association : type_name COLON assignment_expression
	| DEFAULT COLON assignment_expression''' 
	t[0] = Node("generic_association", "generic_association", current_level_of_nesting, t[1:], leaf = 0)


def p_postfix_expression(t):
	'''postfix_expression : primary_expression
	| postfix_expression RSQUARE expression LSQUARE
	| postfix_expression LPAREN RPAREN
	| postfix_expression LPAREN argument_expression_list RPAREN
	| postfix_expression DOT IDENTIFIER
	| postfix_expression PTR_OP IDENTIFIER
	| postfix_expression INC_OP
	| postfix_expression DEC_OP
	| LPAREN type_name RPAREN LFPAREN initializer_list RFPAREN LPAREN type_name RPAREN LFPAREN initializer_list COMMA RFPAREN''' 
	t[0] = Node("postfix_expression", "postfix_expression", current_level_of_nesting, t[1:], leaf = 0)


def p_argument_expression_list(t):
	'''argument_expression_list : assignment_expression
	| argument_expression_list COMMA assignment_expression''' 
	t[0] = Node("argument_expression_list", "argument_expression_list", current_level_of_nesting, t[1:], leaf = 0)


def p_unary_expression(t):
	'''unary_expression : postfix_expression
	| INC_OP unary_expression
	| DEC_OP unary_expression
	| unary_oper cast_expression
	| SIZEOF unary_expression
	| SIZEOF LPAREN type_name RPAREN
	| ALIGNOF LPAREN type_name RPAREN''' 
	t[0] = Node("unary_expression", "unary_expression", current_level_of_nesting, t[1:], leaf = 0)


def p_unary_oper(t):
	'''unary_oper : AMP 
	| TIMES 
	| PLUS 
	| MINUS 
	| TILDE 
	| NOT''' 
	t[0] = Node("unary_oper", "unary_oper", current_level_of_nesting, t[1:], leaf = 0)


def p_cast_expression(t):
	'''cast_expression : unary_expression
	| LPAREN type_name RPAREN cast_expression''' 
	t[0] = Node("cast_expression", "cast_expression", current_level_of_nesting, t[1:], leaf = 0)


def p_multiplicative_expression(t):
	'''multiplicative_expression : cast_expression
	| multiplicative_expression TIMES cast_expression
	| multiplicative_expression DIVIDES cast_expression
	| multiplicative_expression MODULUS cast_expression''' 
	t[0] = Node("multiplicative_expression", "multiplicative_expression", current_level_of_nesting, t[1:], leaf = 0)


def p_additive_expression(t):
	'''additive_expression : multiplicative_expression
	| additive_expression PLUS multiplicative_expression
	| additive_expression MINUS multiplicative_expression''' 
	t[0] = Node("additive_expression", "additive_expression", current_level_of_nesting, t[1:], leaf = 0)


def p_shift_expression(t):
	'''shift_expression : additive_expression
	| shift_expression LEFT_OP additive_expression
	| shift_expression RIGHT_OP additive_expression''' 
	t[0] = Node("shift_expression", "shift_expression", current_level_of_nesting, t[1:], leaf = 0)


def p_relational_expression(t):
	'''relational_expression : shift_expression
	| relational_expression LT_OP shift_expression
	| relational_expression GT_OP shift_expression
	| relational_expression LE_OP shift_expression
	| relational_expression GE_OP shift_expression''' 
	t[0] = Node("relational_expression", "relational_expression", current_level_of_nesting, t[1:], leaf = 0)


def p_equality_expression(t):
	'''equality_expression : relational_expression
	| equality_expression EQ_OP relational_expression
	| equality_expression NE_OP relational_expression''' 
	t[0] = Node("equality_expression", "equality_expression", current_level_of_nesting, t[1:], leaf = 0)


def p_and_expression(t):
	'''and_expression : equality_expression
	| and_expression AMP equality_expression''' 
	t[0] = Node("and_expression", "and_expression", current_level_of_nesting, t[1:], leaf = 0)


def p_exclusive_or_expression(t):
	'''exclusive_or_expression : and_expression
	| exclusive_or_expression XOR and_expression''' 
	t[0] = Node("exclusive_or_expression", "exclusive_or_expression", current_level_of_nesting, t[1:], leaf = 0)


def p_inclusive_or_expression(t):
	'''inclusive_or_expression : exclusive_or_expression
	| inclusive_or_expression OR exclusive_or_expression''' 
	t[0] = Node("inclusive_or_expression", "inclusive_or_expression", current_level_of_nesting, t[1:], leaf = 0)


def p_logical_and_expression(t):
	'''logical_and_expression : inclusive_or_expression
	| logical_and_expression AND_OP inclusive_or_expression''' 
	t[0] = Node("logical_and_expression", "logical_and_expression", current_level_of_nesting, t[1:], leaf = 0)


def p_logical_or_expression(t):
	'''logical_or_expression : logical_and_expression
	| logical_or_expression OR_OP logical_and_expression''' 
	t[0] = Node("logical_or_expression", "logical_or_expression", current_level_of_nesting, t[1:], leaf = 0)


def p_conditional_expression(t):
	'''conditional_expression : logical_or_expression
	| logical_or_expression QMARK expression COLON conditional_expression''' 
	t[0] = Node("conditional_expression", "conditional_expression", current_level_of_nesting, t[1:], leaf = 0)


def p_assignment_expression(t):
	'''assignment_expression : conditional_expression
	| unary_expression assignment_oper assignment_expression''' 
	t[0] = Node("assignment_expression", "assignment_expression", current_level_of_nesting, t[1:], leaf = 0)


def p_assignment_oper(t):
	'''assignment_oper : EQUALS 
	| MUL_ASSIGN
	| DIV_ASSIGN 
	| MOD_ASSIGN 
	| ADD_ASSIGN 
	| SUB_ASSIGN 
	| LEFT_ASSIGN 
	| RIGHT_ASSIGN 
	| AND_ASSIGN 
	| XOR_ASSIGN 
	| OR_ASSIGN''' 
	t[0] = Node("assignment_oper", "assignment_oper", current_level_of_nesting, t[1:], leaf = 0)


def p_expression(t):
	'''expression : assignment_expression
	| expression COMMA assignment_expression''' 
	t[0] = Node("expression", "expression", current_level_of_nesting, t[1:], leaf = 0)


def p_constant_expression(t):
	'''constant_expression : conditional_expression''' 
	t[0] = Node("constant_expression", "constant_expression", current_level_of_nesting, t[1:], leaf = 0)


def p_declaration(t):
	'''declaration : declaration_specifiers SCOLON 
	| declaration_specifiers init_declarator_list SCOLON 
	| static_assert_declaration''' 
	t[0] = Node("declaration", "declaration", current_level_of_nesting, t[1:], leaf = 0)


def p_declaration_specifiers(t):
	'''declaration_specifiers : storage_class_specifier declaration_specifiers
	| storage_class_specifier
	| type_specifier declaration_specifiers
	| type_specifier
	| type_qualifier declaration_specifiers
	| type_qualifier
	| function_specifier declaration_specifiers
	| function_specifier
	| alignment_specifier declaration_specifiers
	| alignment_specifier 
	|''' 
	t[0] = Node("declaration_specifiers", "declaration_specifiers", current_level_of_nesting, t[1:], leaf = 0)


def p_init_declarator_list(t):
	'''init_declarator_list : init_declarator
	| init_declarator_list COMMA init_declarator''' 
	t[0] = Node("init_declarator_list", "init_declarator_list", current_level_of_nesting, t[1:], leaf = 0)


def p_init_declarator(t):
	'''init_declarator : declarator EQUALS initializer
	| declarator''' 
	t[0] = Node("init_declarator", "init_declarator", current_level_of_nesting, t[1:], leaf = 0)


def p_storage_class_specifier(t):
	'''storage_class_specifier : TYPEDEF 
	| EXTERN 
	| STATIC 
	| THREAD_LOCAL 
	| AUTO 
	| REGISTER''' 
	t[0] = Node("storage_class_specifier", "storage_class_specifier", current_level_of_nesting, t[1:], leaf = 0)


def p_type_specifier(t):
	'''type_specifier : VOID
	| CHAR
	| SHORT
	| INT
	| LONG
	| FLOAT
	| DOUBLE
	| SIGNED
	| UNSIGNED
	| BOOL
	| COMPLEX
	| IMAGINARY
	| atomic_type_specifier
	| struct_or_union_specifier
	| enum_specifier''' 
	t[0] = Node("type_specifier", "type_specifier", current_level_of_nesting, t[1:], leaf = 0)


def p_struct_or_union_specifier(t):
	'''struct_or_union_specifier : struct_or_union LFPAREN struct_declaration_list RFPAREN
	| struct_or_union IDENTIFIER LFPAREN struct_declaration_list RFPAREN
	| struct_or_union IDENTIFIER''' 
	t[0] = Node("struct_or_union_specifier", "struct_or_union_specifier", current_level_of_nesting, t[1:], leaf = 0)


def p_struct_or_union(t):
	'''struct_or_union : STRUCT
	| UNION''' 
	t[0] = Node("struct_or_union", "struct_or_union", current_level_of_nesting, t[1:], leaf = 0)


def p_struct_declaration_list(t):
	'''struct_declaration_list : struct_declaration
	| struct_declaration_list struct_declaration''' 
	t[0] = Node("struct_declaration_list", "struct_declaration_list", current_level_of_nesting, t[1:], leaf = 0)


def p_struct_declaration(t):
	'''struct_declaration : specifier_qualifier_list SCOLON
	| specifier_qualifier_list struct_declarator_list SCOLON
	| static_assert_declaration''' 
	t[0] = Node("struct_declaration", "struct_declaration", current_level_of_nesting, t[1:], leaf = 0)


def p_specifier_qualifier_list(t):
	'''specifier_qualifier_list : type_specifier specifier_qualifier_list
	| type_specifier
	| type_qualifier specifier_qualifier_list
	| type_qualifier''' 
	t[0] = Node("specifier_qualifier_list", "specifier_qualifier_list", current_level_of_nesting, t[1:], leaf = 0)


def p_struct_declarator_list(t):
	'''struct_declarator_list : struct_declarator
	| struct_declarator_list COMMA struct_declarator''' 
	t[0] = Node("struct_declarator_list", "struct_declarator_list", current_level_of_nesting, t[1:], leaf = 0)


def p_struct_declarator(t):
	'''struct_declarator : COLON constant_expression
	| declarator COLON constant_expression
	| declarator''' 
	t[0] = Node("struct_declarator", "struct_declarator", current_level_of_nesting, t[1:], leaf = 0)


def p_enum_specifier(t):
	'''enum_specifier : ENUM LFPAREN enumerator_list RFPAREN
	| ENUM LFPAREN enumerator_list COMMA RFPAREN
	| ENUM IDENTIFIER LFPAREN enumerator_list RFPAREN
	| ENUM IDENTIFIER LFPAREN enumerator_list COMMA RFPAREN
	| ENUM IDENTIFIER''' 
	t[0] = Node("enum_specifier", "enum_specifier", current_level_of_nesting, t[1:], leaf = 0)


def p_enumerator_list(t):
	'''enumerator_list : enumerator
	| enumerator_list COMMA enumerator''' 
	t[0] = Node("enumerator_list", "enumerator_list", current_level_of_nesting, t[1:], leaf = 0)


def p_enumerator(t):
	'''enumerator : enumeration_constant EQUALS constant_expression
	| enumeration_constant''' 
	t[0] = Node("enumerator", "enumerator", current_level_of_nesting, t[1:], leaf = 0)


def p_atomic_type_specifier(t):
	'''atomic_type_specifier : ATOMIC LPAREN type_name RPAREN''' 
	t[0] = Node("atomic_type_specifier", "atomic_type_specifier", current_level_of_nesting, t[1:], leaf = 0)


def p_type_qualifier(t):
	'''type_qualifier : CONST
	| VOLATILE
	| ATOMIC''' 
	t[0] = Node("type_qualifier", "type_qualifier", current_level_of_nesting, t[1:], leaf = 0)


def p_function_specifier(t):
	'''function_specifier : NORETURN''' 
	t[0] = Node("function_specifier", "function_specifier", current_level_of_nesting, t[1:], leaf = 0)


def p_alignment_specifier(t):
	'''alignment_specifier : ALIGNAS LPAREN type_name RPAREN
	| ALIGNAS LPAREN constant_expression RPAREN''' 
	t[0] = Node("alignment_specifier", "alignment_specifier", current_level_of_nesting, t[1:], leaf = 0)


def p_declarator(t):
	'''declarator : pointer direct_declarator
	| direct_declarator''' 
	t[0] = Node("declarator", "declarator", current_level_of_nesting, t[1:], leaf = 0)


def p_direct_declarator(t):
	'''direct_declarator : IDENTIFIER 
	| IDENTIFIER LSQUARE NUMBER RSQUARE 
	| LPAREN declarator RPAREN 
	| direct_declarator RSQUARE LSQUARE 
	| direct_declarator RSQUARE TIMES LSQUARE 
	| direct_declarator RSQUARE STATIC type_qualifier_list assignment_expression LSQUARE 
	| direct_declarator RSQUARE STATIC assignment_expression LSQUARE 
	| direct_declarator RSQUARE type_qualifier_list TIMES LSQUARE
	| direct_declarator RSQUARE type_qualifier_list STATIC assignment_expression LSQUARE 
	| direct_declarator RSQUARE type_qualifier_list assignment_expression LSQUARE 
	| direct_declarator RSQUARE type_qualifier_list LSQUARE
	| direct_declarator RSQUARE assignment_expression LSQUARE 
	| direct_declarator LPAREN parameter_type_list RPAREN 
	| direct_declarator LPAREN RPAREN 
	| direct_declarator LPAREN identifier_list RPAREN''' 
	t[0] = Node("direct_declarator", "direct_declarator", current_level_of_nesting, t[1:], leaf = 0)


def p_pointer(t):
	'''pointer : TIMES type_qualifier_list pointer
	| TIMES type_qualifier_list
	| TIMES pointer
	| TIMES''' 
	t[0] = Node("pointer", "pointer", current_level_of_nesting, t[1:], leaf = 0)


def p_type_qualifier_list(t):
	'''type_qualifier_list : type_qualifier
	| type_qualifier_list type_qualifier''' 
	t[0] = Node("type_qualifier_list", "type_qualifier_list", current_level_of_nesting, t[1:], leaf = 0)


def p_parameter_type_list(t):
	'''parameter_type_list : parameter_list COMMA ELLIPSIS
	| parameter_list''' 
	t[0] = Node("parameter_type_list", "parameter_type_list", current_level_of_nesting, t[1:], leaf = 0)


def p_parameter_list(t):
	'''parameter_list : parameter_declaration
	| parameter_list COMMA parameter_declaration''' 
	t[0] = Node("parameter_list", "parameter_list", current_level_of_nesting, t[1:], leaf = 0)


def p_parameter_declaration(t):
	'''parameter_declaration : declaration_specifiers declarator
	| declaration_specifiers abstract_declarator
	| declaration_specifiers''' 
	t[0] = Node("parameter_declaration", "parameter_declaration", current_level_of_nesting, t[1:], leaf = 0)


def p_identifier_list(t):
	'''identifier_list : IDENTIFIER
	| identifier_list COMMA IDENTIFIER''' 
	t[0] = Node("identifier_list", "identifier_list", current_level_of_nesting, t[1:], leaf = 0)


def p_type_name(t):
	'''type_name : specifier_qualifier_list abstract_declarator
	| specifier_qualifier_list''' 
	t[0] = Node("type_name", "type_name", current_level_of_nesting, t[1:], leaf = 0)


def p_abstract_declarator(t):
	'''abstract_declarator : pointer direct_abstract_declarator
	| pointer
	| direct_abstract_declarator''' 
	t[0] = Node("abstract_declarator", "abstract_declarator", current_level_of_nesting, t[1:], leaf = 0)


def p_direct_abstract_declarator(t):
	'''direct_abstract_declarator : LPAREN abstract_declarator RPAREN
	| RSQUARE LSQUARE
	| RSQUARE TIMES LSQUARE
	| RSQUARE STATIC type_qualifier_list assignment_expression LSQUARE
	| RSQUARE STATIC assignment_expression LSQUARE
	| RSQUARE type_qualifier_list STATIC assignment_expression LSQUARE
	| RSQUARE type_qualifier_list assignment_expression LSQUARE
	| RSQUARE type_qualifier_list LSQUARE 
	| RSQUARE assignment_expression LSQUARE
	| direct_abstract_declarator RSQUARE LSQUARE
	| direct_abstract_declarator RSQUARE TIMES LSQUARE
	| direct_abstract_declarator RSQUARE STATIC type_qualifier_list assignment_expression LSQUARE
	| direct_abstract_declarator RSQUARE STATIC assignment_expression LSQUARE
	| direct_abstract_declarator RSQUARE type_qualifier_list assignment_expression LSQUARE
	| direct_abstract_declarator RSQUARE type_qualifier_list STATIC assignment_expression LSQUARE
	| direct_abstract_declarator RSQUARE type_qualifier_list LSQUARE
	| direct_abstract_declarator RSQUARE assignment_expression LSQUARE
	| LPAREN RPAREN
	| LPAREN parameter_type_list RPAREN
	| direct_abstract_declarator LPAREN RPAREN
	| direct_abstract_declarator LPAREN parameter_type_list RPAREN''' 
	t[0] = Node("direct_abstract_declarator", "direct_abstract_declarator", current_level_of_nesting, t[1:], leaf = 0)


def p_initializer(t):
	'''initializer : LFPAREN initializer_list RFPAREN
	| LFPAREN initializer_list COMMA RFPAREN
	| assignment_expression''' 
	t[0] = Node("initializer", "initializer", current_level_of_nesting, t[1:], leaf = 0)


def p_initializer_list(t):
	'''initializer_list : designation initializer
	| initializer
	| initializer_list COMMA designation initializer
	| initializer_list COMMA initializer''' 
	t[0] = Node("initializer_list", "initializer_list", current_level_of_nesting, t[1:], leaf = 0)


def p_designation(t):
	'''designation : designator_list EQUALS''' 
	t[0] = Node("designation", "designation", current_level_of_nesting, t[1:], leaf = 0)


def p_designator_list(t):
	'''designator_list : designator
	| designator_list designator''' 
	t[0] = Node("designator_list", "designator_list", current_level_of_nesting, t[1:], leaf = 0)


def p_designator(t):
	'''designator : RSQUARE constant_expression LSQUARE''' 
	t[0] = Node("designator", "designator", current_level_of_nesting, t[1:], leaf = 0)


def p_static_assert_declaration(t):
	'''static_assert_declaration : STATIC_ASSERT LPAREN constant_expression COMMA STRING_LITERAL RPAREN SCOLON''' 
	t[0] = Node("static_assert_declaration", "static_assert_declaration", current_level_of_nesting, t[1:], leaf = 0)


def p_statement(t):
	'''statement : labeled_statement
	| compound_statement
	| expression_statement
	| selection_statement
	| iteration_statement
	| jump_statement''' 
	t[0] = Node("statement", "statement", current_level_of_nesting, t[1:], leaf = 0)


def p_labeled_statement(t):
	'''labeled_statement : IDENTIFIER COLON statement
	| CASE constant_expression COLON statement 
	| DEFAULT COLON statement''' 
	t[0] = Node("labeled_statement", "labeled_statement", current_level_of_nesting, t[1:], leaf = 0)


def p_compound_statement(t):
	'''compound_statement : LFPAREN RFPAREN
	| LFPAREN  block_item_list RFPAREN''' 
	t[0] = Node("compound_statement", "compound_statement", current_level_of_nesting, t[1:], leaf = 0)


def p_block_item_list(t):
	'''block_item_list : block_item
	| block_item_list block_item''' 
	t[0] = Node("block_item_list", "block_item_list", current_level_of_nesting, t[1:], leaf = 0)


def p_block_item(t):
	'''block_item : declaration
	| statement''' 
	t[0] = Node("block_item", "block_item", current_level_of_nesting, t[1:], leaf = 0)


def p_expression_statement(t):
	'''expression_statement : SCOLON
	| expression SCOLON''' 
	t[0] = Node("expression_statement", "expression_statement", current_level_of_nesting, t[1:], leaf = 0)


def p_selection_statement(t):
	'''selection_statement : IF LPAREN expression RPAREN statement ELSE statement
	| IF LPAREN expression RPAREN statement
	| SWITCH LPAREN expression RPAREN statement''' 
	t[0] = Node("selection_statement", "selection_statement", current_level_of_nesting, t[1:], leaf = 0)


def p_iteration_statement(t):
	'''iteration_statement : WHILE LPAREN expression RPAREN statement
	| DO statement WHILE LPAREN expression RPAREN SCOLON
	| FOR LPAREN expression_statement expression_statement RPAREN statement
	| FOR LPAREN expression_statement expression_statement expression RPAREN statement
	| FOR LPAREN declaration expression_statement RPAREN statement
	| FOR LPAREN declaration expression_statement expression RPAREN statement''' 
	t[0] = Node("iteration_statement", "iteration_statement", current_level_of_nesting, t[1:], leaf = 0)


def p_jump_statement(t):
	'''jump_statement : GOTO IDENTIFIER SCOLON
	| CONTINUE SCOLON
	| BREAK SCOLON
	| RETURN SCOLON
	| RETURN expression SCOLON''' 
	t[0] = Node("jump_statement", "jump_statement", current_level_of_nesting, t[1:], leaf = 0)


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

data = open('programs/c/toy_programs/input_programs/power.c',"r").read()

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
percstring= '0'
percint=int(percstring)
error_len =  percint / 100 * pgmLen
print("error_len" + str(error_len))
pgms =  10
directory= 'programs/c/toy_programs/output_programs/'

fname = 'power.c'.split(".")[0]
extension = 'power.c'.split(".")[1]

error_val= int(error_len/3)
#n_add_errors = 1
#n_remove_errors = 3
#n_replace_errors = 1

n_add_errors = int(error_val/3)
n_remove_errors = int(error_val/3)
n_replace_errors = int(error_val/3)

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
    pgm_errors_marked = pgm_errors_marked.replace("n+","<br/>")
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

