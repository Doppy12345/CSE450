class ParserState(object):
        def __init__(self, filename):
            self.filename = filename

def question01(text):
    
    # Implement this function that takes a string and checks that the three sets of braces "()<>{}" are all matched properly.
    # Any characters other than the 6 characters for braces should raise an Exception exception.
    # Any mismatched braces should raise an Exception exception.
    # If the string is fine, nothing need be done.
    # You must use rply's LexerGenerator and ParserGenerator to solve this problem.

    from rply import LexerGenerator, ParserGenerator, LexingError

    # Your code goes here
    lg = LexerGenerator() 
    lg.add('OPEN_PARENS', r"\(")
    lg.add('CLOSE_PARENS', r"\)")
    lg.add('OPEN_ANGLE', r"<")
    lg.add('CLOSE_ANGLE', r">")
    lg.add('OPEN_BRACKET', r"{")
    lg.add('CLOSE_BRACKET', r"}")
    lexer = lg.build()
    
    
    pg = ParserGenerator(['OPEN_PARENS','CLOSE_PARENS', 'OPEN_ANGLE', 
                          'CLOSE_ANGLE', 'OPEN_BRACKET', 'CLOSE_BRACKET' ]) # Use proper argument(s)
    
    # Your code goes here
    @pg.production('expression : expression expression')
    @pg.production('expression : OPEN_PARENS expression CLOSE_PARENS')
    @pg.production('expression : OPEN_ANGLE expression CLOSE_ANGLE')
    @pg.production('expression : OPEN_BRACKET expression CLOSE_BRACKET')
    @pg.production('expression : bracePair')
    def expr(p):
        return True
    
    @pg.production('bracePair : OPEN_PARENS CLOSE_PARENS')
    @pg.production('bracePair : OPEN_ANGLE CLOSE_ANGLE')
    @pg.production('bracePair : OPEN_BRACKET CLOSE_BRACKET')
    def brace_pair(p):
        return True

    @pg.error
    def error(token):
        
        raise Exception(f'Ran into a {token.gettokentype()} where it was not expected ') from AssertionError
        
        
    parser = pg.build()
    
    print(parser.parse(lexer.lex(text))) # Use proper argument(s)

    
    
    
        

