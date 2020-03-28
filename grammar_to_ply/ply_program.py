from random import choice
line_number = 0
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

eqoperator = ['EQUALS', 'RIGHT_ASSIGN', 'LEFT_ASSIGN', 'ADD_ASSIGN', 'SUB_ASSIGN', 'MUL_ASSIGN', 'DIV_ASSIGN', 'MOD_ASSIGN', 'AND_ASSIGN', 'XOR_ASSIGN', 'OR_ASSIGN', 'LE_OP', 'GE_OP', 'EQ_OP', 'NE_OP', 'GT_OP', 'LT_OP']
arithoperator = ['PLUS', 'MINUS', 'DIVIDES', 'TIMES', 'MODULUS', 'RIGHT_OP', 'LEFT_OP', 'INC_OP', 'DEC_OP']
booloperator = ['AMP', 'OR', 'AND_OP', 'OR_OP']
bracket = ['LPAREN', 'RPAREN', 'LFPAREN', 'RFPAREN', 'LSQUARE', 'RSQUARE']
token = ['TAB', 'ELLIPSIS', 'ALIGNAS', 'ALIGNOF', 'ATOMIC', 'COMPLEX', 'GENERIC', 'IMAGINARY', 'NORETURN', 'STATIC_ASSERT', 'THREAD_LOCAL', 'FUNC_NAME']
symbol = ['COMMA', 'COLON', 'SCOLON', 'DOT', 'TILDE', 'XOR', 'NOT', 'QMARK', 'PTR_OP']
ignore = ['NEWLINE']
reserved = {'void': 'VOID', 'int': 'INT', 'float': 'FLOAT', 'bool': 'BOOL', 'char': 'CHAR', 'double': 'DOUBLE', 'else': 'ELSE', 'if': 'IF', 'while': 'WHILE', 'do': 'DO', 'for': 'FOR', 'auto': 'AUTO', 'break': 'BREAK', 'case': 'CASE', 'const': 'CONST', 'continue': 'CONTINUE', 'default': 'DEFAULT', 'goto': 'GOTO', 'enum': 'ENUM', 'extern': 'EXTERN', 'long': 'LONG', 'register': 'REGISTER', 'return': 'RETURN', 'short': 'SHORT', 'signed': 'SIGNED', 'sizeof': 'SIZEOF', 'static': 'STATIC', 'struct': 'STRUCT', 'typedef': 'TYPEDEF', 'switch': 'SWITCH', 'union': 'UNION', 'unsigned': 'UNSIGNED', 'volatile': 'VOLATILE'}
tokens = ['VOID', 'INT', 'FLOAT', 'BOOL', 'CHAR', 'DOUBLE', 'ELSE', 'IF', 'WHILE', 'DO', 'FOR', 'AUTO', 'BREAK', 'CASE', 'CONST', 'CONTINUE', 'DEFAULT', 'GOTO', 'ENUM', 'EXTERN', 'LONG', 'REGISTER', 'RETURN', 'SHORT', 'SIGNED', 'SIZEOF', 'STATIC', 'STRUCT', 'TYPEDEF', 'SWITCH', 'UNION', 'UNSIGNED', 'VOLATILE', 'EQUALS', 'RIGHT_ASSIGN', 'LEFT_ASSIGN', 'ADD_ASSIGN', 'SUB_ASSIGN', 'MUL_ASSIGN', 'DIV_ASSIGN', 'MOD_ASSIGN', 'AND_ASSIGN', 'XOR_ASSIGN', 'OR_ASSIGN', 'LE_OP', 'GE_OP', 'EQ_OP', 'NE_OP', 'GT_OP', 'LT_OP', 'PLUS', 'MINUS', 'DIVIDES', 'TIMES', 'MODULUS', 'RIGHT_OP', 'LEFT_OP', 'INC_OP', 'DEC_OP', 'AMP', 'OR', 'AND_OP', 'OR_OP', 'LPAREN', 'RPAREN', 'LFPAREN', 'RFPAREN', 'LSQUARE', 'RSQUARE', 'TAB', 'ELLIPSIS', 'ALIGNAS', 'ALIGNOF', 'ATOMIC', 'COMPLEX', 'GENERIC', 'IMAGINARY', 'NORETURN', 'STATIC_ASSERT', 'THREAD_LOCAL', 'FUNC_NAME', 'COMMA', 'COLON', 'SCOLON', 'DOT', 'TILDE', 'XOR', 'NOT', 'QMARK', 'PTR_OP', 'NEWLINE', 'NUMBER', 'IDENTIFIER', 'STRING_LITERAL', 'I_CONSTANT', 'F_CONSTANT']

def t_NUMBER(t):
	r'\d+'
	t.type=reserved.get(t.value,'NUMBER')
	t.value = Node('NUMBER', t.value, leaf = 1)
	return t

<<<<<<< HEAD
def t_IDENTIFIER(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	t.type=reserved.get(t.value,'IDENTIFIER')
	t.value = Node('IDENTIFIER', t.value, leaf = 1)
	return t

def t_STRING_LITERAL(t):
	r'\"(\\.|[^"\\])*\"'
	t.type=reserved.get(t.value,'STRING_LITERAL')
	t.value = Node('STRING_LITERAL', t.value, leaf = 1)
	return t

def t_I_CONSTANT(t):
	r'{(0[xX])}{[a-fA-F0-9]}+{(((u|U)(l|[a-zA-Z_]|ll|[a-zA-Z_][a-zA-Z_])?)|((l|[a-zA-Z_]|ll|[a-zA-Z_][a-zA-Z_])(u|U)?))}? | {[1-9]}{[0-9]}*{(((u|U)(l|[a-zA-Z_]|ll|[a-zA-Z_][a-zA-Z_])?)|((l|[a-zA-Z_]|ll|[a-zA-Z_][a-zA-Z_])(u|U)?))}? | "0"{[0-7]}*{(((u|U)(l|[a-zA-Z_]|ll|[a-zA-Z_][a-zA-Z_])?)|((l|[a-zA-Z_]|ll|[a-zA-Z_][a-zA-Z_])(u|U)?))}? | {(u|U|[a-zA-Z_])}?"\'"([^\'\\\n]|{(\\([\'"\?\\abfnrtv]|[0-7]{1,3}|x[a-fA-F0-9]+))})+"\'"'
	t.type=reserved.get(t.value,'I_CONSTANT')
	t.value = Node('I_CONSTANT', t.value, leaf = 1)
	return t

def t_F_CONSTANT(t):
	r'{[0-9]}+{([Ee][+-]?{[0-9]}+)}{(f|F|l|[a-zA-Z_])}? | {[0-9]}*"."{[0-9]}+{([Ee][+-]?{[0-9]}+)}?{(f|F|l|[a-zA-Z_])}? | {[0-9]}+"."{([Ee][+-]?{[0-9]}+)}?{(f|F|l|[a-zA-Z_])}? | {(0[xX])}{[a-fA-F0-9]}+{([Pp][+-]?{[0-9]}+)}{(f|F|l|[a-zA-Z_])}? | {(0[xX])}{[a-fA-F0-9]}*"."{[a-fA-F0-9]}+{([Pp][+-]?{[0-9]}+)}{(f|F|l|[a-zA-Z_])}? | {(0[xX])}{[a-fA-F0-9]}+"."{([Pp][+-]?{[0-9]}+)}{(f|F|l|[a-zA-Z_])}?'
	t.type=reserved.get(t.value,'F_CONSTANT')
	t.value = Node('F_CONSTANT', t.value, leaf = 1)
	return t

def t_EQUALS(t):
	r'\='
	t.value = Node('eqoperator', '=', leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_RIGHT_ASSIGN(t):
	r'\>>='
	t.value = Node('eqoperator', '>>=', leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_LEFT_ASSIGN(t):
	r'\<<='
	t.value = Node('eqoperator', '<<=', leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_ADD_ASSIGN(t):
	r'\+='
	t.value = Node('eqoperator', '+=', leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_SUB_ASSIGN(t):
	r'\-='
	t.value = Node('eqoperator', '-=', leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_MUL_ASSIGN(t):
	r'\*='
	t.value = Node('eqoperator', '*=', leaf = 1)
=======
def t_EQ_OP(t):
	r'\=='
	t.type=reserved.get(t.value,'EQ_OP')
	t.value = Node('EQ_OP', t.value, leaf = 1)
	return t

def t_MUL_ASSIGN(t):
	r'\*='
	t.type=reserved.get(t.value,'MUL_ASSIGN')
	t.value = Node('MUL_ASSIGN', t.value, leaf = 1)
	return t

def t_NE_OP(t):
	r'\!='
	t.type=reserved.get(t.value,'NE_OP')
	t.value = Node('NE_OP', t.value, leaf = 1)
	return t

def t_GE_OP(t):
	r'\>='
	t.type=reserved.get(t.value,'GE_OP')
	t.value = Node('GE_OP', t.value, leaf = 1)
	return t

def t_LE_OP(t):
	r'\<='
	t.type=reserved.get(t.value,'LE_OP')
	t.value = Node('LE_OP', t.value, leaf = 1)
	return t

def t_IDENTIFIER(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	t.type=reserved.get(t.value,'IDENTIFIER')
	t.value = Node('IDENTIFIER', t.value, leaf = 1)
	return t

def t_STRING_LITERAL(t):
	r'\"(\\.|[^"\\])*\"'
	t.type=reserved.get(t.value,'STRING_LITERAL')
	t.value = Node('STRING_LITERAL', t.value, leaf = 1)
	return t

def t_I_CONSTANT(t):
	r'{(0[xX])}{[a-fA-F0-9]}+{(((u|U)(l|[a-zA-Z_]|ll|[a-zA-Z_][a-zA-Z_])?)|((l|[a-zA-Z_]|ll|[a-zA-Z_][a-zA-Z_])(u|U)?))}? | {[1-9]}{[0-9]}*{(((u|U)(l|[a-zA-Z_]|ll|[a-zA-Z_][a-zA-Z_])?)|((l|[a-zA-Z_]|ll|[a-zA-Z_][a-zA-Z_])(u|U)?))}? | "0"{[0-7]}*{(((u|U)(l|[a-zA-Z_]|ll|[a-zA-Z_][a-zA-Z_])?)|((l|[a-zA-Z_]|ll|[a-zA-Z_][a-zA-Z_])(u|U)?))}? | {(u|U|[a-zA-Z_])}?"\'"([^\'\\\n]|{(\\([\'"\?\\abfnrtv]|[0-7]{1,3}|x[a-fA-F0-9]+))})+"\'"'
	t.type=reserved.get(t.value,'I_CONSTANT')
	t.value = Node('I_CONSTANT', t.value, leaf = 1)
	return t

def t_F_CONSTANT(t):
	r'{[0-9]}+{([Ee][+-]?{[0-9]}+)}{(f|F|l|[a-zA-Z_])}? | {[0-9]}*"."{[0-9]}+{([Ee][+-]?{[0-9]}+)}?{(f|F|l|[a-zA-Z_])}? | {[0-9]}+"."{([Ee][+-]?{[0-9]}+)}?{(f|F|l|[a-zA-Z_])}? | {(0[xX])}{[a-fA-F0-9]}+{([Pp][+-]?{[0-9]}+)}{(f|F|l|[a-zA-Z_])}? | {(0[xX])}{[a-fA-F0-9]}*"."{[a-fA-F0-9]}+{([Pp][+-]?{[0-9]}+)}{(f|F|l|[a-zA-Z_])}? | {(0[xX])}{[a-fA-F0-9]}+"."{([Pp][+-]?{[0-9]}+)}{(f|F|l|[a-zA-Z_])}?'
	t.type=reserved.get(t.value,'F_CONSTANT')
	t.value = Node('F_CONSTANT', t.value, leaf = 1)
	return t

def t_EQUALS(t):
	r'\='
	t.value = Node('eqoperator', '=', leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_RIGHT_ASSIGN(t):
	r'\>>='
	t.value = Node('eqoperator', '>>=', leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_LEFT_ASSIGN(t):
	r'\<<='
	t.value = Node('eqoperator', '<<=', leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_ADD_ASSIGN(t):
	r'\+='
	t.value = Node('eqoperator', '+=', leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_SUB_ASSIGN(t):
	r'\-='
	t.value = Node('eqoperator', '-=', leaf = 1)
>>>>>>> 7c6f999532c1b74f20bf85c099711e67edd8f705
	t.typee = 'eqoperator'
	return t

def t_DIV_ASSIGN(t):
	r'\/='
	t.value = Node('eqoperator', '/=', leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_MOD_ASSIGN(t):
	r'\%='
	t.value = Node('eqoperator', '%=', leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_AND_ASSIGN(t):
	r'\&='
	t.value = Node('eqoperator', '&=', leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_XOR_ASSIGN(t):
	r'\^='
	t.value = Node('eqoperator', '^=', leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_OR_ASSIGN(t):
	r'\|='
	t.value = Node('eqoperator', '|=', leaf = 1)
	t.typee = 'eqoperator'
	return t

<<<<<<< HEAD
def t_LE_OP(t):
	r'\<='
	t.value = Node('eqoperator', '<=', leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_GE_OP(t):
	r'\>='
	t.value = Node('eqoperator', '>=', leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_EQ_OP(t):
	r'\=='
	t.value = Node('eqoperator', '==', leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_NE_OP(t):
	r'\!='
	t.value = Node('eqoperator', '!=', leaf = 1)
	t.typee = 'eqoperator'
	return t

=======
>>>>>>> 7c6f999532c1b74f20bf85c099711e67edd8f705
def t_GT_OP(t):
	r'\>'
	t.value = Node('eqoperator', '>', leaf = 1)
	t.typee = 'eqoperator'
	return t

def t_LT_OP(t):
	r'\<'
	t.value = Node('eqoperator', '<', leaf = 1)
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

def t_DIVIDES(t):
	r'\/'
	t.value = Node('arithoperator', '/', leaf = 1)
	t.typee = 'arithoperator'
	return t

def t_TIMES(t):
	r'\*'
	t.value = Node('arithoperator', '*', leaf = 1)
	t.typee = 'arithoperator'
	return t

def t_MODULUS(t):
	r'\%'
	t.value = Node('arithoperator', '%', leaf = 1)
	t.typee = 'arithoperator'
	return t

def t_RIGHT_OP(t):
	r'>>'
	t.value = Node('arithoperator', '>', leaf = 1)
	t.typee = 'arithoperator'
	return t

def t_LEFT_OP(t):
	r'<<'
	t.value = Node('arithoperator', '<', leaf = 1)
	t.typee = 'arithoperator'
	return t

def t_INC_OP(t):
	r'\++'
	t.value = Node('arithoperator', '++', leaf = 1)
	t.typee = 'arithoperator'
	return t

def t_DEC_OP(t):
	r'\--'
	t.value = Node('arithoperator', '--', leaf = 1)
	t.typee = 'arithoperator'
	return t

def t_AMP(t):
	r'\&'
	t.value = Node('booloperator', '&', leaf = 1)
	t.typee = 'booloperator'
	return t

def t_OR(t):
	r'\|'
	t.value = Node('booloperator', '|', leaf = 1)
	t.typee = 'booloperator'
	return t

def t_AND_OP(t):
	r'\&&'
	t.value = Node('booloperator', '&&', leaf = 1)
	t.typee = 'booloperator'
	return t

def t_OR_OP(t):
	r'\|\|'
	t.value = Node('booloperator', '|\|', leaf = 1)
	t.typee = 'booloperator'
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

def t_LFPAREN(t):
	r'\{'
	t.value = Node('bracket', '{', leaf = 1)
	t.typee = 'bracket'
	return t

def t_RFPAREN(t):
	r'\}'
	t.value = Node('bracket', '}', leaf = 1)
	t.typee = 'bracket'
	return t

def t_LSQUARE(t):
	r'\['
	t.value = Node('bracket', '[', leaf = 1)
	t.typee = 'bracket'
	return t

def t_RSQUARE(t):
	r'\]'
	t.value = Node('bracket', ']', leaf = 1)
	t.typee = 'bracket'
	return t

def t_TAB(t):
	r'\t'
	t.value = Node('token', '\t', leaf = 1)
	t.typee = 'token'
	return t

def t_ELLIPSIS(t):
	r'\...'
	t.value = Node('token', '...', leaf = 1)
	t.typee = 'token'
	return t

def t_ALIGNAS(t):
	r'_Alignas'
	t.value = Node('token', 'Alignas', leaf = 1)
	t.typee = 'token'
	return t

def t_ALIGNOF(t):
	r'_Alignof'
	t.value = Node('token', 'Alignof', leaf = 1)
	t.typee = 'token'
	return t

def t_ATOMIC(t):
	r'_Atomic'
	t.value = Node('token', 'Atomic', leaf = 1)
	t.typee = 'token'
	return t

def t_COMPLEX(t):
	r'_Complex'
	t.value = Node('token', 'Complex', leaf = 1)
	t.typee = 'token'
	return t

def t_GENERIC(t):
	r'_Generic'
	t.value = Node('token', 'Generic', leaf = 1)
	t.typee = 'token'
	return t

def t_IMAGINARY(t):
	r'_Imaginary'
	t.value = Node('token', 'Imaginary', leaf = 1)
	t.typee = 'token'
	return t

def t_NORETURN(t):
	r'_Noreturn'
	t.value = Node('token', 'Noreturn', leaf = 1)
	t.typee = 'token'
	return t

def t_STATIC_ASSERT(t):
	r'_Static_assert'
	t.value = Node('token', 'Static_assert', leaf = 1)
	t.typee = 'token'
	return t

def t_THREAD_LOCAL(t):
	r'_Thread_local'
	t.value = Node('token', 'Thread_local', leaf = 1)
	t.typee = 'token'
	return t

def t_FUNC_NAME(t):
	r'__func__'
	t.value = Node('token', '_func__', leaf = 1)
	t.typee = 'token'
	return t

def t_COMMA(t):
	r'\,'
	t.value = Node('symbol', ',', leaf = 1)
	t.typee = 'symbol'
	return t

def t_COLON(t):
	r'\:'
	t.value = Node('symbol', ':', leaf = 1)
	t.typee = 'symbol'
	return t

def t_SCOLON(t):
	r'\;'
	t.value = Node('symbol', ';', leaf = 1)
	t.typee = 'symbol'
	return t

def t_DOT(t):
	r'\.'
	t.value = Node('symbol', '.', leaf = 1)
	t.typee = 'symbol'
	return t

def t_TILDE(t):
	r'\~'
	t.value = Node('symbol', '~', leaf = 1)
	t.typee = 'symbol'
	return t

def t_XOR(t):
	r'\^'
	t.value = Node('symbol', '^', leaf = 1)
	t.typee = 'symbol'
	return t

def t_NOT(t):
	r'\!'
	t.value = Node('symbol', '!', leaf = 1)
	t.typee = 'symbol'
	return t

def t_QMARK(t):
	r'\?'
	t.value = Node('symbol', '?', leaf = 1)
	t.typee = 'symbol'
	return t

def t_PTR_OP(t):
	r'\->'
	t.value = Node('symbol', '->', leaf = 1)
	t.typee = 'symbol'
	return t

def t_NEWLINE(t):
	r'\n'
	global line_number
	line_number += 1
<<<<<<< HEAD
	print('LEXING with line_number: ', line_number)
=======
	print(line_number)
>>>>>>> 7c6f999532c1b74f20bf85c099711e67edd8f705
	t.value = Node('ignore', 'n', leaf = 1)
	pass

def p_start(t):
	'''start : translation_unit''' 
<<<<<<< HEAD
	global line_number
	line_number = 0
	print("beginning yacc")
=======
>>>>>>> 7c6f999532c1b74f20bf85c099711e67edd8f705
	t[0] = Node("start", "start", t[1:], leaf = 0)


def p_translation_unit(t):
	'''translation_unit : external_declaration
	| translation_unit external_declaration''' 
	t[0] = Node("translation_unit", "translation_unit", t[1:], leaf = 0)


def p_external_declaration(t):
	'''external_declaration : function_definition
	| declaration''' 
	t[0] = Node("external_declaration", "external_declaration", t[1:], leaf = 0)
<<<<<<< HEAD


def p_function_definition(t):
	'''function_definition : declaration_specifiers declarator declaration_list compound_statement
	| declaration_specifiers declarator compound_statement''' 
	t[0] = Node("function_definition", "function_definition", t[1:], leaf = 0)


def p_declaration_list(t):
	'''declaration_list : declaration
	| declaration_list declaration''' 
	t[0] = Node("declaration_list", "declaration_list", t[1:], leaf = 0)


def p_primary_expression(t):
	'''primary_expression : IDENTIFIER
	| constant 
	| string 
	| LPAREN expression RPAREN
	| generic_selection 
	| NUMBER''' 
	t[0] = Node("primary_expression", "primary_expression", t[1:], leaf = 0)


def p_constant(t):
	'''constant : I_CONSTANT 
	| F_CONSTANT''' 
	t[0] = Node("constant", "constant", t[1:], leaf = 0)


def p_enumeration_constant(t):
	'''enumeration_constant : IDENTIFIER''' 
	t[0] = Node("enumeration_constant", "enumeration_constant", t[1:], leaf = 0)


def p_string(t):
	'''string : STRING_LITERAL
	| FUNC_NAME''' 
	t[0] = Node("string", "string", t[1:], leaf = 0)


def p_generic_selection(t):
	'''generic_selection : GENERIC LPAREN assignment_expression COMMA generic_assoc_list RPAREN''' 
	t[0] = Node("generic_selection", "generic_selection", t[1:], leaf = 0)


def p_generic_assoc_list(t):
	'''generic_assoc_list : generic_association
	| generic_assoc_list COMMA generic_association''' 
	t[0] = Node("generic_assoc_list", "generic_assoc_list", t[1:], leaf = 0)


def p_generic_association(t):
	'''generic_association : type_name COLON assignment_expression
	| DEFAULT COLON assignment_expression''' 
	t[0] = Node("generic_association", "generic_association", t[1:], leaf = 0)


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
	t[0] = Node("postfix_expression", "postfix_expression", t[1:], leaf = 0)


def p_argument_expression_list(t):
	'''argument_expression_list : assignment_expression
	| argument_expression_list COMMA assignment_expression''' 
	t[0] = Node("argument_expression_list", "argument_expression_list", t[1:], leaf = 0)


def p_unary_expression(t):
	'''unary_expression : postfix_expression
	| INC_OP unary_expression
	| DEC_OP unary_expression
	| unary_oper cast_expression
	| SIZEOF unary_expression
	| SIZEOF LPAREN type_name RPAREN
	| ALIGNOF LPAREN type_name RPAREN''' 
	t[0] = Node("unary_expression", "unary_expression", t[1:], leaf = 0)


def p_unary_oper(t):
	'''unary_oper : AMP 
	| TIMES 
	| PLUS 
	| MINUS 
	| TILDE 
	| NOT''' 
	t[0] = Node("unary_oper", "unary_oper", t[1:], leaf = 0)


def p_cast_expression(t):
	'''cast_expression : unary_expression
	| LPAREN type_name RPAREN cast_expression''' 
	t[0] = Node("cast_expression", "cast_expression", t[1:], leaf = 0)


def p_multiplicative_expression(t):
	'''multiplicative_expression : cast_expression
	| multiplicative_expression TIMES cast_expression
	| multiplicative_expression DIVIDES cast_expression
	| multiplicative_expression MODULUS cast_expression''' 
	t[0] = Node("multiplicative_expression", "multiplicative_expression", t[1:], leaf = 0)


def p_additive_expression(t):
	'''additive_expression : multiplicative_expression
	| additive_expression PLUS multiplicative_expression
	| additive_expression MINUS multiplicative_expression''' 
	t[0] = Node("additive_expression", "additive_expression", t[1:], leaf = 0)


def p_shift_expression(t):
	'''shift_expression : additive_expression
	| shift_expression LEFT_OP additive_expression
	| shift_expression RIGHT_OP additive_expression''' 
	t[0] = Node("shift_expression", "shift_expression", t[1:], leaf = 0)


def p_relational_expression(t):
	'''relational_expression : shift_expression
	| relational_expression LT_OP shift_expression
	| relational_expression GT_OP shift_expression
	| relational_expression LE_OP shift_expression
	| relational_expression GE_OP shift_expression''' 
	t[0] = Node("relational_expression", "relational_expression", t[1:], leaf = 0)


def p_equality_expression(t):
	'''equality_expression : relational_expression
	| equality_expression EQ_OP relational_expression
	| equality_expression NE_OP relational_expression''' 
	t[0] = Node("equality_expression", "equality_expression", t[1:], leaf = 0)


def p_and_expression(t):
	'''and_expression : equality_expression
	| and_expression AMP equality_expression''' 
	t[0] = Node("and_expression", "and_expression", t[1:], leaf = 0)


def p_exclusive_or_expression(t):
	'''exclusive_or_expression : and_expression
	| exclusive_or_expression XOR and_expression''' 
	t[0] = Node("exclusive_or_expression", "exclusive_or_expression", t[1:], leaf = 0)


def p_inclusive_or_expression(t):
	'''inclusive_or_expression : exclusive_or_expression
	| inclusive_or_expression OR exclusive_or_expression''' 
	t[0] = Node("inclusive_or_expression", "inclusive_or_expression", t[1:], leaf = 0)


def p_logical_and_expression(t):
	'''logical_and_expression : inclusive_or_expression
	| logical_and_expression AND_OP inclusive_or_expression''' 
	t[0] = Node("logical_and_expression", "logical_and_expression", t[1:], leaf = 0)


def p_logical_or_expression(t):
	'''logical_or_expression : logical_and_expression
	| logical_or_expression OR_OP logical_and_expression''' 
	t[0] = Node("logical_or_expression", "logical_or_expression", t[1:], leaf = 0)


def p_conditional_expression(t):
	'''conditional_expression : logical_or_expression
	| logical_or_expression QMARK expression COLON conditional_expression''' 
	t[0] = Node("conditional_expression", "conditional_expression", t[1:], leaf = 0)


def p_assignment_expression(t):
	'''assignment_expression : conditional_expression
	| unary_expression assignment_oper assignment_expression''' 
	t[0] = Node("assignment_expression", "assignment_expression", t[1:], leaf = 0)


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
	t[0] = Node("assignment_oper", "assignment_oper", t[1:], leaf = 0)


def p_expression(t):
	'''expression : assignment_expression
	| expression COMMA assignment_expression''' 
	t[0] = Node("expression", "expression", t[1:], leaf = 0)


def p_constant_expression(t):
	'''constant_expression : conditional_expression''' 
	t[0] = Node("constant_expression", "constant_expression", t[1:], leaf = 0)


def p_declaration(t):
	'''declaration : declaration_specifiers SCOLON 
	| declaration_specifiers init_declarator_list SCOLON 
	| static_assert_declaration''' 
	t[0] = Node("declaration", "declaration", t[1:], leaf = 0)


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
	t[0] = Node("declaration_specifiers", "declaration_specifiers", t[1:], leaf = 0)


def p_init_declarator_list(t):
	'''init_declarator_list : init_declarator
	| init_declarator_list COMMA init_declarator''' 
	t[0] = Node("init_declarator_list", "init_declarator_list", t[1:], leaf = 0)


def p_init_declarator(t):
	'''init_declarator : declarator EQUALS initializer
	| declarator''' 
	t[0] = Node("init_declarator", "init_declarator", t[1:], leaf = 0)


def p_storage_class_specifier(t):
	'''storage_class_specifier : TYPEDEF 
	| EXTERN 
	| STATIC 
	| THREAD_LOCAL 
	| AUTO 
	| REGISTER''' 
	t[0] = Node("storage_class_specifier", "storage_class_specifier", t[1:], leaf = 0)


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
	t[0] = Node("type_specifier", "type_specifier", t[1:], leaf = 0)


def p_struct_or_union_specifier(t):
	'''struct_or_union_specifier : struct_or_union LFPAREN struct_declaration_list RFPAREN
	| struct_or_union IDENTIFIER LFPAREN struct_declaration_list RFPAREN
	| struct_or_union IDENTIFIER''' 
	t[0] = Node("struct_or_union_specifier", "struct_or_union_specifier", t[1:], leaf = 0)


def p_struct_or_union(t):
	'''struct_or_union : STRUCT
	| UNION''' 
	t[0] = Node("struct_or_union", "struct_or_union", t[1:], leaf = 0)


def p_struct_declaration_list(t):
	'''struct_declaration_list : struct_declaration
	| struct_declaration_list struct_declaration''' 
	t[0] = Node("struct_declaration_list", "struct_declaration_list", t[1:], leaf = 0)


def p_struct_declaration(t):
	'''struct_declaration : specifier_qualifier_list SCOLON
	| specifier_qualifier_list struct_declarator_list SCOLON
	| static_assert_declaration''' 
	t[0] = Node("struct_declaration", "struct_declaration", t[1:], leaf = 0)


def p_specifier_qualifier_list(t):
	'''specifier_qualifier_list : type_specifier specifier_qualifier_list
	| type_specifier
	| type_qualifier specifier_qualifier_list
	| type_qualifier''' 
	t[0] = Node("specifier_qualifier_list", "specifier_qualifier_list", t[1:], leaf = 0)


def p_struct_declarator_list(t):
	'''struct_declarator_list : struct_declarator
	| struct_declarator_list COMMA struct_declarator''' 
	t[0] = Node("struct_declarator_list", "struct_declarator_list", t[1:], leaf = 0)


def p_struct_declarator(t):
	'''struct_declarator : COLON constant_expression
	| declarator COLON constant_expression
	| declarator''' 
	t[0] = Node("struct_declarator", "struct_declarator", t[1:], leaf = 0)


def p_enum_specifier(t):
	'''enum_specifier : ENUM LFPAREN enumerator_list RFPAREN
	| ENUM LFPAREN enumerator_list COMMA RFPAREN
	| ENUM IDENTIFIER LFPAREN enumerator_list RFPAREN
	| ENUM IDENTIFIER LFPAREN enumerator_list COMMA RFPAREN
	| ENUM IDENTIFIER''' 
	t[0] = Node("enum_specifier", "enum_specifier", t[1:], leaf = 0)


def p_enumerator_list(t):
	'''enumerator_list : enumerator
	| enumerator_list COMMA enumerator''' 
	t[0] = Node("enumerator_list", "enumerator_list", t[1:], leaf = 0)


def p_enumerator(t):
	'''enumerator : enumeration_constant EQUALS constant_expression
	| enumeration_constant''' 
	t[0] = Node("enumerator", "enumerator", t[1:], leaf = 0)


def p_atomic_type_specifier(t):
	'''atomic_type_specifier : ATOMIC LPAREN type_name RPAREN''' 
	t[0] = Node("atomic_type_specifier", "atomic_type_specifier", t[1:], leaf = 0)


def p_type_qualifier(t):
	'''type_qualifier : CONST
	| VOLATILE
	| ATOMIC''' 
	t[0] = Node("type_qualifier", "type_qualifier", t[1:], leaf = 0)


def p_function_specifier(t):
	'''function_specifier : NORETURN''' 
	t[0] = Node("function_specifier", "function_specifier", t[1:], leaf = 0)


def p_alignment_specifier(t):
	'''alignment_specifier : ALIGNAS LPAREN type_name RPAREN
	| ALIGNAS LPAREN constant_expression RPAREN''' 
	t[0] = Node("alignment_specifier", "alignment_specifier", t[1:], leaf = 0)


def p_declarator(t):
	'''declarator : pointer direct_declarator
	| direct_declarator''' 
	t[0] = Node("declarator", "declarator", t[1:], leaf = 0)


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
	t[0] = Node("direct_declarator", "direct_declarator", t[1:], leaf = 0)


def p_pointer(t):
	'''pointer : TIMES type_qualifier_list pointer
	| TIMES type_qualifier_list
	| TIMES pointer
	| TIMES''' 
	t[0] = Node("pointer", "pointer", t[1:], leaf = 0)


def p_type_qualifier_list(t):
	'''type_qualifier_list : type_qualifier
	| type_qualifier_list type_qualifier''' 
	t[0] = Node("type_qualifier_list", "type_qualifier_list", t[1:], leaf = 0)


def p_parameter_type_list(t):
	'''parameter_type_list : parameter_list COMMA ELLIPSIS
	| parameter_list''' 
	t[0] = Node("parameter_type_list", "parameter_type_list", t[1:], leaf = 0)


def p_parameter_list(t):
	'''parameter_list : parameter_declaration
	| parameter_list COMMA parameter_declaration''' 
	t[0] = Node("parameter_list", "parameter_list", t[1:], leaf = 0)


def p_parameter_declaration(t):
	'''parameter_declaration : declaration_specifiers declarator
	| declaration_specifiers abstract_declarator
	| declaration_specifiers''' 
	t[0] = Node("parameter_declaration", "parameter_declaration", t[1:], leaf = 0)


def p_identifier_list(t):
	'''identifier_list : IDENTIFIER
	| identifier_list COMMA IDENTIFIER''' 
	t[0] = Node("identifier_list", "identifier_list", t[1:], leaf = 0)


def p_type_name(t):
	'''type_name : specifier_qualifier_list abstract_declarator
	| specifier_qualifier_list''' 
	t[0] = Node("type_name", "type_name", t[1:], leaf = 0)


def p_abstract_declarator(t):
	'''abstract_declarator : pointer direct_abstract_declarator
	| pointer
	| direct_abstract_declarator''' 
	t[0] = Node("abstract_declarator", "abstract_declarator", t[1:], leaf = 0)


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
	t[0] = Node("direct_abstract_declarator", "direct_abstract_declarator", t[1:], leaf = 0)


def p_initializer(t):
	'''initializer : LFPAREN initializer_list RFPAREN
	| LFPAREN initializer_list COMMA RFPAREN
	| assignment_expression''' 
	t[0] = Node("initializer", "initializer", t[1:], leaf = 0)


def p_initializer_list(t):
	'''initializer_list : designation initializer
	| initializer
	| initializer_list COMMA designation initializer
	| initializer_list COMMA initializer''' 
	t[0] = Node("initializer_list", "initializer_list", t[1:], leaf = 0)


def p_designation(t):
	'''designation : designator_list EQUALS''' 
	t[0] = Node("designation", "designation", t[1:], leaf = 0)


def p_designator_list(t):
	'''designator_list : designator
	| designator_list designator''' 
	t[0] = Node("designator_list", "designator_list", t[1:], leaf = 0)


def p_designator(t):
	'''designator : RSQUARE constant_expression LSQUARE
	| DOT IDENTIFIER''' 
	t[0] = Node("designator", "designator", t[1:], leaf = 0)


def p_static_assert_declaration(t):
	'''static_assert_declaration : STATIC_ASSERT LPAREN constant_expression COMMA STRING_LITERAL RPAREN SCOLON''' 
	t[0] = Node("static_assert_declaration", "static_assert_declaration", t[1:], leaf = 0)


def p_statement(t):
	'''statement : labeled_statement
	| compound_statement
	| expression_statement
	| selection_statement
	| iteration_statement
	| jump_statement''' 
	t[0] = Node("statement", "statement", t[1:], leaf = 0)


def p_labeled_statement(t):
	'''labeled_statement : IDENTIFIER COLON statement
	| CASE constant_expression COLON statement 
	| DEFAULT COLON statement''' 
	t[0] = Node("labeled_statement", "labeled_statement", t[1:], leaf = 0)


def p_compound_statement(t):
	'''compound_statement : LFPAREN RFPAREN
	| LFPAREN  block_item_list RFPAREN''' 
	t[0] = Node("compound_statement", "compound_statement", t[1:], leaf = 0)


def p_block_item_list(t):
	'''block_item_list : block_item
	| block_item_list block_item''' 
	t[0] = Node("block_item_list", "block_item_list", t[1:], leaf = 0)


def p_block_item(t):
	'''block_item : declaration
	| statement''' 
	t[0] = Node("block_item", "block_item", t[1:], leaf = 0)


def p_expression_statement(t):
	'''expression_statement : SCOLON
	| expression SCOLON''' 
	t[0] = Node("expression_statement", "expression_statement", t[1:], leaf = 0)


def p_selection_statement(t):
	'''selection_statement : IF LPAREN expression RPAREN statement ELSE statement
	| IF LPAREN expression RPAREN statement
	| SWITCH LPAREN expression RPAREN statement''' 
	t[0] = Node("selection_statement", "selection_statement", t[1:], leaf = 0)


def p_iteration_statement(t):
	'''iteration_statement : WHILE LPAREN expression RPAREN statement
	| DO statement WHILE LPAREN expression RPAREN SCOLON
	| FOR LPAREN expression_statement expression_statement RPAREN statement
	| FOR LPAREN expression_statement expression_statement expression RPAREN statement
	| FOR LPAREN declaration expression_statement RPAREN statement
	| FOR LPAREN declaration expression_statement expression RPAREN statement''' 
	t[0] = Node("iteration_statement", "iteration_statement", t[1:], leaf = 0)


=======


def p_function_definition(t):
	'''function_definition : declaration_specifiers declarator declaration_list compound_statement
	| declaration_specifiers declarator compound_statement''' 
	t[0] = Node("function_definition", "function_definition", t[1:], leaf = 0)


def p_declaration_list(t):
	'''declaration_list : declaration
	| declaration_list declaration''' 
	t[0] = Node("declaration_list", "declaration_list", t[1:], leaf = 0)


def p_primary_expression(t):
	'''primary_expression : IDENTIFIER
	| constant 
	| string 
	| LPAREN expression RPAREN
	| generic_selection 
	| NUMBER''' 
	t[0] = Node("primary_expression", "primary_expression", t[1:], leaf = 0)


def p_constant(t):
	'''constant : I_CONSTANT 
	| F_CONSTANT''' 
	t[0] = Node("constant", "constant", t[1:], leaf = 0)


def p_enumeration_constant(t):
	'''enumeration_constant : IDENTIFIER''' 
	t[0] = Node("enumeration_constant", "enumeration_constant", t[1:], leaf = 0)


def p_string(t):
	'''string : STRING_LITERAL
	| FUNC_NAME''' 
	t[0] = Node("string", "string", t[1:], leaf = 0)


def p_generic_selection(t):
	'''generic_selection : GENERIC LPAREN assignment_expression COMMA generic_assoc_list RPAREN''' 
	t[0] = Node("generic_selection", "generic_selection", t[1:], leaf = 0)


def p_generic_assoc_list(t):
	'''generic_assoc_list : generic_association
	| generic_assoc_list COMMA generic_association''' 
	t[0] = Node("generic_assoc_list", "generic_assoc_list", t[1:], leaf = 0)


def p_generic_association(t):
	'''generic_association : type_name COLON assignment_expression
	| DEFAULT COLON assignment_expression''' 
	t[0] = Node("generic_association", "generic_association", t[1:], leaf = 0)


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
	t[0] = Node("postfix_expression", "postfix_expression", t[1:], leaf = 0)


def p_argument_expression_list(t):
	'''argument_expression_list : assignment_expression
	| argument_expression_list COMMA assignment_expression''' 
	t[0] = Node("argument_expression_list", "argument_expression_list", t[1:], leaf = 0)


def p_unary_expression(t):
	'''unary_expression : postfix_expression
	| INC_OP unary_expression
	| DEC_OP unary_expression
	| unary_oper cast_expression
	| SIZEOF unary_expression
	| SIZEOF LPAREN type_name RPAREN
	| ALIGNOF LPAREN type_name RPAREN''' 
	t[0] = Node("unary_expression", "unary_expression", t[1:], leaf = 0)


def p_unary_oper(t):
	'''unary_oper : AMP 
	| TIMES 
	| PLUS 
	| MINUS 
	| TILDE 
	| NOT''' 
	t[0] = Node("unary_oper", "unary_oper", t[1:], leaf = 0)


def p_cast_expression(t):
	'''cast_expression : unary_expression
	| LPAREN type_name RPAREN cast_expression''' 
	t[0] = Node("cast_expression", "cast_expression", t[1:], leaf = 0)


def p_multiplicative_expression(t):
	'''multiplicative_expression : cast_expression
	| multiplicative_expression TIMES cast_expression
	| multiplicative_expression DIVIDES cast_expression
	| multiplicative_expression MODULUS cast_expression''' 
	t[0] = Node("multiplicative_expression", "multiplicative_expression", t[1:], leaf = 0)


def p_additive_expression(t):
	'''additive_expression : multiplicative_expression
	| additive_expression PLUS multiplicative_expression
	| additive_expression MINUS multiplicative_expression''' 
	t[0] = Node("additive_expression", "additive_expression", t[1:], leaf = 0)


def p_shift_expression(t):
	'''shift_expression : additive_expression
	| shift_expression LEFT_OP additive_expression
	| shift_expression RIGHT_OP additive_expression''' 
	t[0] = Node("shift_expression", "shift_expression", t[1:], leaf = 0)


def p_relational_expression(t):
	'''relational_expression : shift_expression
	| relational_expression LT_OP shift_expression
	| relational_expression GT_OP shift_expression
	| relational_expression LE_OP shift_expression
	| relational_expression GE_OP shift_expression''' 
	t[0] = Node("relational_expression", "relational_expression", t[1:], leaf = 0)


def p_equality_expression(t):
	'''equality_expression : relational_expression
	| equality_expression EQ_OP relational_expression
	| equality_expression NE_OP relational_expression''' 
	t[0] = Node("equality_expression", "equality_expression", t[1:], leaf = 0)


def p_and_expression(t):
	'''and_expression : equality_expression
	| and_expression AMP equality_expression''' 
	t[0] = Node("and_expression", "and_expression", t[1:], leaf = 0)


def p_exclusive_or_expression(t):
	'''exclusive_or_expression : and_expression
	| exclusive_or_expression XOR and_expression''' 
	t[0] = Node("exclusive_or_expression", "exclusive_or_expression", t[1:], leaf = 0)


def p_inclusive_or_expression(t):
	'''inclusive_or_expression : exclusive_or_expression
	| inclusive_or_expression OR exclusive_or_expression''' 
	t[0] = Node("inclusive_or_expression", "inclusive_or_expression", t[1:], leaf = 0)


def p_logical_and_expression(t):
	'''logical_and_expression : inclusive_or_expression
	| logical_and_expression AND_OP inclusive_or_expression''' 
	t[0] = Node("logical_and_expression", "logical_and_expression", t[1:], leaf = 0)


def p_logical_or_expression(t):
	'''logical_or_expression : logical_and_expression
	| logical_or_expression OR_OP logical_and_expression''' 
	t[0] = Node("logical_or_expression", "logical_or_expression", t[1:], leaf = 0)


def p_conditional_expression(t):
	'''conditional_expression : logical_or_expression
	| logical_or_expression QMARK expression COLON conditional_expression''' 
	t[0] = Node("conditional_expression", "conditional_expression", t[1:], leaf = 0)


def p_assignment_expression(t):
	'''assignment_expression : conditional_expression
	| unary_expression assignment_oper assignment_expression''' 
	t[0] = Node("assignment_expression", "assignment_expression", t[1:], leaf = 0)


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
	t[0] = Node("assignment_oper", "assignment_oper", t[1:], leaf = 0)


def p_expression(t):
	'''expression : assignment_expression
	| expression COMMA assignment_expression''' 
	t[0] = Node("expression", "expression", t[1:], leaf = 0)


def p_constant_expression(t):
	'''constant_expression : conditional_expression''' 
	t[0] = Node("constant_expression", "constant_expression", t[1:], leaf = 0)


def p_declaration(t):
	'''declaration : declaration_specifiers SCOLON 
	| declaration_specifiers init_declarator_list SCOLON 
	| static_assert_declaration''' 
	t[0] = Node("declaration", "declaration", t[1:], leaf = 0)


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
	t[0] = Node("declaration_specifiers", "declaration_specifiers", t[1:], leaf = 0)


def p_init_declarator_list(t):
	'''init_declarator_list : init_declarator
	| init_declarator_list COMMA init_declarator''' 
	t[0] = Node("init_declarator_list", "init_declarator_list", t[1:], leaf = 0)


def p_init_declarator(t):
	'''init_declarator : declarator EQUALS initializer
	| declarator''' 
	t[0] = Node("init_declarator", "init_declarator", t[1:], leaf = 0)


def p_storage_class_specifier(t):
	'''storage_class_specifier : TYPEDEF 
	| EXTERN 
	| STATIC 
	| THREAD_LOCAL 
	| AUTO 
	| REGISTER''' 
	t[0] = Node("storage_class_specifier", "storage_class_specifier", t[1:], leaf = 0)


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
	t[0] = Node("type_specifier", "type_specifier", t[1:], leaf = 0)


def p_struct_or_union_specifier(t):
	'''struct_or_union_specifier : struct_or_union LFPAREN struct_declaration_list RFPAREN
	| struct_or_union IDENTIFIER LFPAREN struct_declaration_list RFPAREN
	| struct_or_union IDENTIFIER''' 
	t[0] = Node("struct_or_union_specifier", "struct_or_union_specifier", t[1:], leaf = 0)


def p_struct_or_union(t):
	'''struct_or_union : STRUCT
	| UNION''' 
	t[0] = Node("struct_or_union", "struct_or_union", t[1:], leaf = 0)


def p_struct_declaration_list(t):
	'''struct_declaration_list : struct_declaration
	| struct_declaration_list struct_declaration''' 
	t[0] = Node("struct_declaration_list", "struct_declaration_list", t[1:], leaf = 0)


def p_struct_declaration(t):
	'''struct_declaration : specifier_qualifier_list SCOLON
	| specifier_qualifier_list struct_declarator_list SCOLON
	| static_assert_declaration''' 
	t[0] = Node("struct_declaration", "struct_declaration", t[1:], leaf = 0)


def p_specifier_qualifier_list(t):
	'''specifier_qualifier_list : type_specifier specifier_qualifier_list
	| type_specifier
	| type_qualifier specifier_qualifier_list
	| type_qualifier''' 
	t[0] = Node("specifier_qualifier_list", "specifier_qualifier_list", t[1:], leaf = 0)


def p_struct_declarator_list(t):
	'''struct_declarator_list : struct_declarator
	| struct_declarator_list COMMA struct_declarator''' 
	t[0] = Node("struct_declarator_list", "struct_declarator_list", t[1:], leaf = 0)


def p_struct_declarator(t):
	'''struct_declarator : COLON constant_expression
	| declarator COLON constant_expression
	| declarator''' 
	t[0] = Node("struct_declarator", "struct_declarator", t[1:], leaf = 0)


def p_enum_specifier(t):
	'''enum_specifier : ENUM LFPAREN enumerator_list RFPAREN
	| ENUM LFPAREN enumerator_list COMMA RFPAREN
	| ENUM IDENTIFIER LFPAREN enumerator_list RFPAREN
	| ENUM IDENTIFIER LFPAREN enumerator_list COMMA RFPAREN
	| ENUM IDENTIFIER''' 
	t[0] = Node("enum_specifier", "enum_specifier", t[1:], leaf = 0)


def p_enumerator_list(t):
	'''enumerator_list : enumerator
	| enumerator_list COMMA enumerator''' 
	t[0] = Node("enumerator_list", "enumerator_list", t[1:], leaf = 0)


def p_enumerator(t):
	'''enumerator : enumeration_constant EQUALS constant_expression
	| enumeration_constant''' 
	t[0] = Node("enumerator", "enumerator", t[1:], leaf = 0)


def p_atomic_type_specifier(t):
	'''atomic_type_specifier : ATOMIC LPAREN type_name RPAREN''' 
	t[0] = Node("atomic_type_specifier", "atomic_type_specifier", t[1:], leaf = 0)


def p_type_qualifier(t):
	'''type_qualifier : CONST
	| VOLATILE
	| ATOMIC''' 
	t[0] = Node("type_qualifier", "type_qualifier", t[1:], leaf = 0)


def p_function_specifier(t):
	'''function_specifier : NORETURN''' 
	t[0] = Node("function_specifier", "function_specifier", t[1:], leaf = 0)


def p_alignment_specifier(t):
	'''alignment_specifier : ALIGNAS LPAREN type_name RPAREN
	| ALIGNAS LPAREN constant_expression RPAREN''' 
	t[0] = Node("alignment_specifier", "alignment_specifier", t[1:], leaf = 0)


def p_declarator(t):
	'''declarator : pointer direct_declarator
	| direct_declarator''' 
	t[0] = Node("declarator", "declarator", t[1:], leaf = 0)


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
	t[0] = Node("direct_declarator", "direct_declarator", t[1:], leaf = 0)


def p_pointer(t):
	'''pointer : TIMES type_qualifier_list pointer
	| TIMES type_qualifier_list
	| TIMES pointer
	| TIMES''' 
	t[0] = Node("pointer", "pointer", t[1:], leaf = 0)


def p_type_qualifier_list(t):
	'''type_qualifier_list : type_qualifier
	| type_qualifier_list type_qualifier''' 
	t[0] = Node("type_qualifier_list", "type_qualifier_list", t[1:], leaf = 0)


def p_parameter_type_list(t):
	'''parameter_type_list : parameter_list COMMA ELLIPSIS
	| parameter_list''' 
	t[0] = Node("parameter_type_list", "parameter_type_list", t[1:], leaf = 0)


def p_parameter_list(t):
	'''parameter_list : parameter_declaration
	| parameter_list COMMA parameter_declaration''' 
	t[0] = Node("parameter_list", "parameter_list", t[1:], leaf = 0)


def p_parameter_declaration(t):
	'''parameter_declaration : declaration_specifiers declarator
	| declaration_specifiers abstract_declarator
	| declaration_specifiers''' 
	t[0] = Node("parameter_declaration", "parameter_declaration", t[1:], leaf = 0)


def p_identifier_list(t):
	'''identifier_list : IDENTIFIER
	| identifier_list COMMA IDENTIFIER''' 
	t[0] = Node("identifier_list", "identifier_list", t[1:], leaf = 0)


def p_type_name(t):
	'''type_name : specifier_qualifier_list abstract_declarator
	| specifier_qualifier_list''' 
	t[0] = Node("type_name", "type_name", t[1:], leaf = 0)


def p_abstract_declarator(t):
	'''abstract_declarator : pointer direct_abstract_declarator
	| pointer
	| direct_abstract_declarator''' 
	t[0] = Node("abstract_declarator", "abstract_declarator", t[1:], leaf = 0)


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
	t[0] = Node("direct_abstract_declarator", "direct_abstract_declarator", t[1:], leaf = 0)


def p_initializer(t):
	'''initializer : LFPAREN initializer_list RFPAREN
	| LFPAREN initializer_list COMMA RFPAREN
	| assignment_expression''' 
	t[0] = Node("initializer", "initializer", t[1:], leaf = 0)


def p_initializer_list(t):
	'''initializer_list : designation initializer
	| initializer
	| initializer_list COMMA designation initializer
	| initializer_list COMMA initializer''' 
	t[0] = Node("initializer_list", "initializer_list", t[1:], leaf = 0)


def p_designation(t):
	'''designation : designator_list EQUALS''' 
	t[0] = Node("designation", "designation", t[1:], leaf = 0)


def p_designator_list(t):
	'''designator_list : designator
	| designator_list designator''' 
	t[0] = Node("designator_list", "designator_list", t[1:], leaf = 0)


def p_designator(t):
	'''designator : RSQUARE constant_expression LSQUARE
	| DOT IDENTIFIER''' 
	t[0] = Node("designator", "designator", t[1:], leaf = 0)


def p_static_assert_declaration(t):
	'''static_assert_declaration : STATIC_ASSERT LPAREN constant_expression COMMA STRING_LITERAL RPAREN SCOLON''' 
	t[0] = Node("static_assert_declaration", "static_assert_declaration", t[1:], leaf = 0)


def p_statement(t):
	'''statement : labeled_statement
	| compound_statement
	| expression_statement
	| selection_statement
	| iteration_statement
	| jump_statement''' 
	t[0] = Node("statement", "statement", t[1:], leaf = 0)


def p_labeled_statement(t):
	'''labeled_statement : IDENTIFIER COLON statement
	| CASE constant_expression COLON statement 
	| DEFAULT COLON statement''' 
	t[0] = Node("labeled_statement", "labeled_statement", t[1:], leaf = 0)


def p_compound_statement(t):
	'''compound_statement : LFPAREN RFPAREN
	| LFPAREN  block_item_list RFPAREN''' 
	t[0] = Node("compound_statement", "compound_statement", t[1:], leaf = 0)


def p_block_item_list(t):
	'''block_item_list : block_item
	| block_item_list block_item''' 
	t[0] = Node("block_item_list", "block_item_list", t[1:], leaf = 0)


def p_block_item(t):
	'''block_item : declaration
	| statement''' 
	t[0] = Node("block_item", "block_item", t[1:], leaf = 0)


def p_expression_statement(t):
	'''expression_statement : SCOLON
	| expression SCOLON''' 
	t[0] = Node("expression_statement", "expression_statement", t[1:], leaf = 0)


def p_selection_statement(t):
	'''selection_statement : IF LPAREN expression RPAREN statement ELSE statement
	| IF LPAREN expression RPAREN statement
	| SWITCH LPAREN expression RPAREN statement''' 
	t[0] = Node("selection_statement", "selection_statement", t[1:], leaf = 0)


def p_iteration_statement(t):
	'''iteration_statement : WHILE LPAREN expression RPAREN statement
	| DO statement WHILE LPAREN expression RPAREN SCOLON
	| FOR LPAREN expression_statement expression_statement RPAREN statement
	| FOR LPAREN expression_statement expression_statement expression RPAREN statement
	| FOR LPAREN declaration expression_statement RPAREN statement
	| FOR LPAREN declaration expression_statement expression RPAREN statement''' 
	t[0] = Node("iteration_statement", "iteration_statement", t[1:], leaf = 0)


>>>>>>> 7c6f999532c1b74f20bf85c099711e67edd8f705
def p_jump_statement(t):
	'''jump_statement : GOTO IDENTIFIER SCOLON
	| CONTINUE SCOLON
	| BREAK SCOLON
	| RETURN SCOLON
	| RETURN expression SCOLON''' 
	t[0] = Node("jump_statement", "jump_statement", t[1:], leaf = 0)


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

<<<<<<< HEAD
data = open('../programs/c/toy_programs/input_programs/floatsum.c',"r").read()
=======
data = open('../programs/c/toy_programs/input_programs/struct.c',"r").read()
>>>>>>> 7c6f999532c1b74f20bf85c099711e67edd8f705

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
directory= '../programs/c/toy_programs/output_programs/'
#directory = "../programs/python/functions/output_programs/"
#directory2 = "../programs/python/functions/output_programs/errors"

<<<<<<< HEAD
fname = 'floatsum.c'.split(".")[0]
extension = 'floatsum.c'.split(".")[1]
=======
fname = 'struct.c'.split(".")[0]
extension = 'struct.c'.split(".")[1]
positions = [i for i in range(1,pgmLen)]
>>>>>>> 7c6f999532c1b74f20bf85c099711e67edd8f705
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
    f = open(directory + fname + "_" + str(i) + "." + extension , "w")
    fe=open(directory + "errors/" + fname + "_" + str(i) + "_error." + extension , "w")
    fe.write(message)
    fe.close()
    f.write(pgm)
    f.close()

