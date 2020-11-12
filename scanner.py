import ply.lex as lex

reserved = {
    'program': 'PRO',
    'if' : 'IF',
    'then' : 'THEN',
    'else': 'ELSE',
    'write' : 'WRITE',
    'read' : 'READ',
    'int' : 'INT',
    'float' : 'FLT',
    'char' : 'CHAR',
    'void' : 'VOID',
    'module' :  "MODULE",
    'var' : 'VARTOKEN',
    'main' : 'MAIN',
    'while' : 'WHILE',
    'do' : 'DO',
    'for' : 'FOR',
    'to' : 'TO',
    'return' : 'RETURN'
}

# List of token names. This is always required
tokens = [
    'ID',
    'PARIZQ',
    'PARDER',
    'PTOCOM',
    'DOSPTS',
    'CORIZQ',
    'CORDER',
    'COMA',
    'KEYIZQ',
    'KEYDER',
    'IGU',
    'MAY',
    'MEN',
    'IGUIGU',
    'DIF',
    'AND',
    'OR',
    'CTEI',
    'CTEF',
    'CTE_STRING',
    'MAS',
    'MENOS',
    'MULT',
    'DIV',
    'MAYIGU',
    'MENIGU'
] + list(reserved.values())



# Regular expression rules for simple tokens
t_KEYIZQ = r'{'
t_KEYDER = r'}'
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_IGU = r'='
t_IGUIGU = r'=='
t_AND = r'&'
t_OR = r'\|'
t_COMA = r','
t_PTOCOM =  r';'
t_MAS = r'\+'
t_MENOS = r'-'
t_MULT = r'\*'
t_DOSPTS = r':'
t_MAY = r'>'
t_MEN = r'<'
t_DIV  = r'/'
t_PARIZQ  = r'\('
t_PARDER  = r'\)'
t_DIF = r'!='
t_CTE_STRING = r'\"[A-Za-z0-9\s]*\"'
t_MAYIGU = r'>='
t_MENIGU = r'<='

def t_ID(t):
    r'[A-Za-z]+[A-Za-z0-9]*'
    t.type = reserved.get(t.value,'ID') #Checks for reserved words
    return t

def t_CTEF(t):
    r'\d+(\.)\d+'
    t.value = float(t.value)
    return t


def t_CTEI(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()