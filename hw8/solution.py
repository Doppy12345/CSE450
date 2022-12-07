def question01(text):
    # Use RPLY to write a compiler for a simple markup language.
    # In this language, any text between double parentheses
    # must be capitalized. For example, the following input text:
    # 
    # Hello ((world))!
    #
    # should compile into the following output:
    #
    # Hello WORLD!
    #
    # Remember, you should use RPLY lexing and parsing for that.
    # Bypassing this requirement will result in 0 points for the
    # assignment, even if all tests pass.
    #
    # As always, see the unit tests to better understand the 
    # assignment.
    # 
    # Tip 1: Parse the surrounding text symbol by symbol. Attempting
    # to capture large blocks may result in the parser never finishing.
    # Tip 2: The regular expression [\w\W\n] effectively captures 
    # what we usually refer to as "any character".
    
    from rply import LexerGenerator, ParserGenerator, Token
    LexGen = LexerGenerator()
    LexGen.add("LEFT_PARENS", r"\(\(")
    LexGen.add("RIGHT_PARENS", r"\)\)")
    LexGen.add("WORD", r"[^()]+")

    
    lexer = LexGen.build()
    
    ParseGen = ParserGenerator(["WORD", "LEFT_PARENS", "RIGHT_PARENS"], precedence=[('left', [ "LEFT_PARENS", "RIGHT_PARENS", "WORD"])] )  
    
    
    @ParseGen.production('strings : LEFT_PARENS strings RIGHT_PARENS')
    def strings_cap(p: list[Token]):   
        return p[1].upper()
    
    @ParseGen.production('strings : strings string')
    def string_concat(p: list[Token]):   
        return p[0] + p[1]
        
    @ParseGen.production('strings : string')
    def strings(p: list[Token]):   
        return p[0]
        
    @ParseGen.production('string : LEFT_PARENS string RIGHT_PARENS')
    def string_capitalize(p: list[Token]):   
        return p[1].upper()
    
    @ParseGen.production('string : WORD')
    def string(p: list[Token]):   
        return p[0].getstr()
    
    @ParseGen.production('string : LEFT_PARENS RIGHT_PARENS')
    def emptyString(p: list[Token]):   
        return ""
    
    @ParseGen.error
    def error(token):
        print(token)
        
    parser = ParseGen.build()
        
    return parser.parse(lexer.lex(text))

