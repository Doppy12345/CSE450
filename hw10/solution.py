# Homework 10
# Student name: 

def question01(text):
    # Use RPLY to write a compiler for a simple markup language
    # that recognizes links in the format [[URL]]((TEXT)) and 
    # converts them into HTML hyperlinks. In this language, the URL
    # is enclosed in double square brackets, and the link text is
    # enclosed in double parentheses. The link should be converted
    # by the compiler into an HTML hyperlink. For example, the 
    # following input text:
    # 
    # Class website: [[https://www.cse.msu.edu/~cse450/]]((here))
    #
    # should compile into the following output:
    #
    # Class website: <a href='https://www.cse.msu.edu/~cse450/'>here</a>
    #
    # We assume the URL is properly formatted.
    #
    # Remember, you should use RPLY lexing and parsing for that.
    # Bypassing this requirement will result in 0 points for the
    # assignment, even if all tests pass.
    #
    # As always, see the unit tests to better understand the 
    # assignment.
    # 
    # Tip: Representing links through grammar rules is possible
    # but fraught with challenges. Tracking opening and closing
    # sets of brackets and parentheses is possible but not easy 
    # either. I suggest to catch the link as a whole lexeme, and
    # then perform manual textual analysis of the corresponding tokens.

    from rply import LexerGenerator, ParserGenerator, Token
    import re
    
    hrefPattern = r"(?!(\[\[))[^\[\]\(\)]+(?=(\]\]))"
    linkTextPattern = r"(?!(\(\())[^\[\]\(\)]+(?=(\)\)))"

    LexGen = LexerGenerator()
    LexGen.add("LINK", r"\[\[[^\[\]\(\)]+\]\]\(\([^\[\]\(\)]+\)\)")
    LexGen.add("LEFT_PARENS", r"\(")
    LexGen.add("RIGHT_PARENS", r"\)+")
    LexGen.add("WORD", r"[^\[\]\(\)]+")
    
    lexer = LexGen.build()
    
    ParseGen = ParserGenerator(["WORD", "LINK", "RIGHT_PARENS", "LEFT_PARENS"], precedence=[('left', ["LINK", "LEFT_PARENS", "RIGHT_PARENS", "WORD"])] )  
    
    @ParseGen.production('strings : strings string')
    def string_concat(p: list[Token]):   
        return p[0] + p[1]
        
    @ParseGen.production('strings : string')
    def strings(p: list[Token]):   
        return p[0]
        
    @ParseGen.production('string : LINK ')
    def string_capitalize(p: list[Token]): 
        link = p[0].getstr()
        print(link)
        return f"<a href='{re.search(hrefPattern, link)[0]}'>{re.search(linkTextPattern, link)[0]}</a>"
    
    @ParseGen.production('string : WORD')
    @ParseGen.production('string : LEFT_PARENS')
    @ParseGen.production('string : RIGHT_PARENS')
    def string(p: list[Token]):   
        return p[0].getstr()
    
    
    @ParseGen.error
    def error(token):
        print(token)
        
    parser = ParseGen.build()
        
    return parser.parse(lexer.lex(text))

