from rply import LexerGenerator, LexingError, ParserGenerator, Token

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
    return parser.parse(lexer.lex(program))
        
    

def createParser():
    ParseGen = ParserGenerator(
        ['GOGREEN','GOWHITE','SPARTYSAYS','SEMICOLON','NVAR','SVAR',
         'IDENTIFIER','NUMBER', 'STRING', 'PLUS', 'MINUS', 'MUL', 'DIV','ASSIGNMENT'
         ,'OPEN_PARENS', 'CLOSE_PARENS' ],
        precedence=[('left',['PLUS', 'MINUS', 'NUMBER']),
                    ('left', ['MUL', 'DIV'])]
    )
    
    @ParseGen.production('program : GOGREEN SEMICOLON statements GOWHITE SEMICOLON')
    def program(p: list[Token]):   
        return {
            "type": "program",
            "statements": p[2]
        }
        
    
    @ParseGen.production('statements : statements statement')
    def statements(p: list[Token]):
        return [*p[0], p[1]]

    
    @ParseGen.production('statements : statement')
    def single_statement(p: list[Token]):
        return [p[0]]
   
        
    @ParseGen.production('statement : SPARTYSAYS expression SEMICOLON')
    def statement_spartysays(p: list[Token]):
        return {
            "type": "statement",
            "statement_type": "spartysays",
            "expression": p[1]
        }
    
    @ParseGen.production('statement : NVAR IDENTIFIER ASSIGNMENT expression SEMICOLON')
    @ParseGen.production('statement : SVAR IDENTIFIER ASSIGNMENT expression SEMICOLON')
    def statement_delcaration(p: list[Token]):
        statementType = str(p[0].gettokentype()).lower()
        return {
            "type": "statement",
            "statement_type": statementType,
            "identifier": p[1].getstr(),
            "expression": p[3]
        }
   
    @ParseGen.production('statement : IDENTIFIER ASSIGNMENT expression SEMICOLON')
    def statement_assignment(p: list[Token]):
        return {
            "type": "statement",
            "statement_type": "assignment",
            "identifier": p[0].getstr(),
            "expression": p[2],
        }
        
    @ParseGen.production('expression : IDENTIFIER' )
    @ParseGen.production('expression : NUMBER' )
    @ParseGen.production('expression : STRING' )
    def expression_token(p: list[Token]):
        key = 'identifier' if (str(p[0].gettokentype()) == 'IDENTIFIER') else "value"
        value = p[0].getstr() if p[0].gettokentype() == 'NUMBER' else p[0].getstr().replace('"', '') 
        return {
                "type": "expression",
                "expression_type": p[0].gettokentype().lower(),
                key: value
            }
    
    @ParseGen.production('expression : OPEN_PARENS expression CLOSE_PARENS')
    def paren_expression(p: list[Token]):
        return {
            "type": "expression",
            "expression_type": "parentheses",
            "expression": p[1]
        }
    
    @ParseGen.production('expression : expression PLUS expression')
    @ParseGen.production('expression : expression MINUS expression')
    @ParseGen.production('expression : expression DIV expression')
    @ParseGen.production('expression : expression MUL expression')
    def expression_arithmetic(p: list[Token]):
            return {
                "type": "expression",
                "expression_type": str(p[1].gettokentype()).lower(),
                "left": p[0],
                "right": p[2],
            }
    
    @ParseGen.error
    def error_handler(token: Token):
        raise ValueError({
            "type": "error",
            "tokentype": token.gettokentype(),
            "line": token.getsourcepos().lineno,
            "column": token.getsourcepos().colno,
        }) from AssertionError
        
    
    return ParseGen.build()
   

