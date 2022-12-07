
def question01(text):
    # Implement this function that takes a string and returns a list of tokens.
    # Each character in the string should be lexed into the tokens "UPPER", "LOWER" or "OTHER" depending on the case of the character.
    # See the open tests for better understanding of the assignment.

    from rply import LexerGenerator
    lg = LexerGenerator()

    lg.add('UPPER', r"[A-Z]")
    lg.add('LOWER', r"[a-z]")
    lg.add('OTHER', r"[^a-zA-Z]")

    lexer = lg.build()
    return list(lexer.lex(text))

def question02(text):
    # Implement this function that takes a string and returns a list of tokens.
    # The string should be tokenized into:
    #   - NON_TITLE_CASE (things like: "table", "HOUSE");
    #   - TITLE_CASE (things like: "Hat", "Josh", "A"); and 
    #   - OTHER (things like punctation, digits).
    # Whitespaces should be ignored.
    # See the open tests for better understanding of the assignment.

    from rply import LexerGenerator
    lg = LexerGenerator()
    
    lg.add('OTHER', r"[^A-z]")
    lg.add('TITLE_CASE', r"\b[A-Z][a-z]*\b")
    lg.add('NON_TITLE_CASE', r"\b[A-z]*\b")
    lg.ignore(r"\s+")
    

    lexer = lg.build()

    return list(lexer.lex(text))

