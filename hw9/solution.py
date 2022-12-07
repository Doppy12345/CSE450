# Homework 9
# Student name: 

def question01(text):
    # Use RPLY to write a compiler for a simple markup language
    # that recognizes URLs and converts them into HTML hyperlinks.
    # In this language, a URL enclosed in double square brackets
    # should be converted by the compiler into an HTML hyperlink
    # with the link text defaulted to [link]. For example, the 
    # following input text:
    # 
    # Nick's website: [[https://nick-ivanov.com]]
    #
    # should compile into the following output:
    #
    # Nick's website: <a href='https://nick-ivanov.com'>[link]</a>
    #
    # We assume the URL in the brackets is properly formatted.
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
    # sets of brackets is possible but not easy either. I suggest
    # to catch the link as a whole lexeme, and then perform 
    # manual analysis of the corresponding tokens.

    from rply import LexerGenerator, ParserGenerator, Token
    

    LexGen = LexerGenerator()
    LexGen.add("LEFT_BRACKET", r"\[\[")
    LexGen.add("RIGHT_BRACKET", r"\]\]")
    LexGen.add("WORD", r"[^\[\]]+")

    
    lexer = LexGen.build()
    
    ParseGen = ParserGenerator(["WORD", "LEFT_BRACKET", "RIGHT_BRACKET"], precedence=[('left', [ "LEFT_BRACKET", "RIGHT_BRACKET", "WORD"])] )  
    
    @ParseGen.production('strings : strings string')
    def string_concat(p: list[Token]):   
        return p[0] + p[1]
        
    @ParseGen.production('strings : string')
    def strings(p: list[Token]):   
        return p[0]
        
    @ParseGen.production('string : LEFT_BRACKET WORD RIGHT_BRACKET')
    def string_capitalize(p: list[Token]):   
        return f"<a href='{p[1].getstr()}'>[link]</a>"
    
    @ParseGen.production('string : WORD')
    def string(p: list[Token]):   
        return p[0].getstr()
    
    @ParseGen.production('string : LEFT_BRACKET RIGHT_BRACKET')
    def emptyString(p: list[Token]):   
        return ""
    
    @ParseGen.error
    def error(token):
        print(token)
        
    parser = ParseGen.build()
        
    return parser.parse(lexer.lex(text))

print(question01("Here is Nick's website: [[https://nick-ivanov.com]]!"))