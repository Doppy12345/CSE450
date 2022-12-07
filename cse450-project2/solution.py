from rply import LexerGenerator, LexingError, ParserGenerator

def lex_spartytalk(program):
    lexer =  createLexer()
    tokens = []
    try:
        for token in lexer.lex(program):
            tokens.append(token)
        return (tokens, -1, -1)
    except LexingError as lexErr:
        print(lexErr)
        return (None, lexErr.source_pos.lineno, lexErr.source_pos.colno)
    

def createLexer():
    LexGen = LexerGenerator()
    LexGen.add("GOGREEN", r"gogreen")
    LexGen.add("GOWHITE", r"gowhite")
    LexGen.add("SPARTYSAYS", r"spartysays")
    LexGen.add("SEMICOLON", r";")
    LexGen.add("NVAR", r"nvar")
    LexGen.add("SVAR", r"svar")
    LexGen.add("IDENTIFIER", r"[a-zA-Z]+[\da-zA-Z]*")
    LexGen.add("NUMBER", r"[+-]?[0-9]+([.]?\d+|)")
    LexGen.add("STRING", r"\"[^\"]*\"")
    LexGen.add("PLUS", r"\+(?!\d)")
    LexGen.add("MINUS", r"\-(?!\d)")
    LexGen.add("MUL", r"\*")
    LexGen.add("DIV", r"\/")
    LexGen.add("ASSIGNMENT", r"=")
    LexGen.add("OPEN_PARENS", r"\(")
    LexGen.add("CLOSE_PARENS", r'\)')
    LexGen.ignore(r'\s+')
    return LexGen.build()

def parse_spartytalk(program):
    lexer = createLexer()
    parser = createParser()
    parser.parse(lexer.lex(program))
        
    

def createParser():
    ParseGen = ParserGenerator(
        ['GOGREEN','GOWHITE','SPARTYSAYS','SEMICOLON','NVAR','SVAR',
         'IDENTIFIER','NUMBER', 'STRING', 'PLUS', 'MINUS', 'MUL', 'DIV','ASSIGNMENT'
         ,'OPEN_PARENS', 'CLOSE_PARENS' ],
        precedence=[('left',['PLUS', 'MINUS', 'NUMBER']),
                    ('left', ['MUL', 'DIV'])]
    )
    
    @ParseGen.production('program : GOGREEN SEMICOLON statements GOWHITE SEMICOLON')
    def program(p):
        print(f'<program> ::= {p[0]} {p[1]} <statements> {p[3]} {p[4]}')
    
    @ParseGen.production('statements : statement')
    def single_statement(p):
        print('<statements> ::= <statement>')
    @ParseGen.production('statements : statements statement')
    def statements(p):
        print('<statements> ::= <statements> <statement>')
    
    @ParseGen.production('statement : SPARTYSAYS expression SEMICOLON')
    def statement_spartysays(p):
        print(f'<statement> ::= {str(p[0])} <expression> {str(p[2])}')
    
    @ParseGen.production('statement : NVAR IDENTIFIER ASSIGNMENT expression SEMICOLON')
    @ParseGen.production('statement : SVAR IDENTIFIER ASSIGNMENT expression SEMICOLON')
    def statement_delcaration(p):
        print(f'<statement> ::= {str(p[0])} {str(p[1])} {str(p[2])} <expression> {str(p[4])}')
    
    @ParseGen.production('statement : IDENTIFIER ASSIGNMENT expression SEMICOLON')
    def statement_assignment(p):
        print(f'<statement> ::= {str(p[0])} {str(p[1])} <expression> {str(p[3])}')
    
    @ParseGen.production('expression : IDENTIFIER' )
    @ParseGen.production('expression : NUMBER' )
    @ParseGen.production('expression : STRING' )
    def expression_token(p):
        print(f'<expression> ::= {str(p[0])}')
    
    @ParseGen.production('expression : OPEN_PARENS expression CLOSE_PARENS')
    def paren_expression(p):
        print(f'<expression> ::= {str(p[0])} <expression> {str(p[2])}')
    
    @ParseGen.production('expression : expression PLUS expression')
    @ParseGen.production('expression : expression MINUS expression')
    @ParseGen.production('expression : expression DIV expression')
    @ParseGen.production('expression : expression MUL expression')
    def expression_arithmetic(p):
            print(f'<expression> ::= <expression> {str(p[1])} <expression>')
    
    @ParseGen.error
    def error_handler(token):
        raise ValueError
    
    return ParseGen.build()
   
parse_spartytalk(""""
gogreen;
spartysays "hi";
nvar b = 7;
nvar a = 10 + 20 - 10 * (b * 255) + (a + b);
spartysays a;
spartysays a + b;
spartysays (n + k);
gowhite;
""")