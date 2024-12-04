import ply.lex as lex

reserved = {
    'actor': 'ACTOR',
    'as': 'AS',
    'usecase': 'USECASE',
    'package': 'PACKAGE',
    'includes': 'INCLUDES',
    'extends': 'EXTENDS',
    '@startuml': 'STARTUML',
    '@enduml': 'ENDUML'
}

tokens = [
    'COLON',
    'RIGHT_ARROW_1',
    'RIGHT_ARROW_2',
    'LBRACE',
    'RBRACE',
    'INHERIT',
    'EOL',
    'STRING',
    'STEREO',
    'ACTOR_TEXT',
    'USE_CASE_TEXT',
    'ID',
] + list(reserved.values())

t_COLON = r':'
t_RIGHT_ARROW_1 = r'-->|->'
t_RIGHT_ARROW_2 = r'\.\.>|\.\.|\.>'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_INHERIT = r'<\|--'
t_ignore = ' \t'  


def t_EOL(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t


def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value.strip('"')
    return t


def t_STEREO(t):
    r'<<[^>>]+>>'
    t.value = t.value.strip('<>')
    return t


def t_ACTOR_TEXT(t):
    r':[^:]+:'
    t.value = t.value.strip(':')
    return t


def t_USE_CASE_TEXT(t):
    r'[^()]+'
    t.value = t.value.strip('()')
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  
    return t


def t_error(t):
    print(f"Caractère invalide : {t.value[0]}")
    t.lexer.skip(1)


lexer = lex.lex()

if _name_ == "_main_":
    data = '''
    @startuml System
    actor :User:
    usecase (Define travel)
    usecase (Set VIP options)
    :User: --> (Define travel)
    :User: --> (Set VIP options)
    @enduml
    '''

    lexer.input(data)
    for tok in lexer:
        print(tok)
