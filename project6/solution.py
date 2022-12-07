# Project 6
# Student name: Daniel Passos

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
    LexGen.add("EQ", r"==")
    LexGen.add("NOTEQ", r"!=")
    LexGen.add("LESSEQ", r"<=")
    LexGen.add("LESS", r"<")
    LexGen.add("GREATEREQ", r">=")
    LexGen.add("GREATER", r">")
    LexGen.add("AND", r"and")
    LexGen.add("OR", r"or")
    LexGen.add("NOT", r"not")
    LexGen.add("IF", r"if")
    LexGen.add("ELSE", r"else")
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
    return parser.parse(lexer.lex(program), state=[0])
        
    

def createParser():
    ParseGen = ParserGenerator(
        ['GOGREEN','GOWHITE','SPARTYSAYS','SEMICOLON','NVAR','SVAR',"EQ", "GREATEREQ", "NOTEQ", "LESSEQ", "LESS", "GREATER" 
         'IDENTIFIER','NUMBER', 'STRING', 'PLUS', 'MINUS', 'MUL', 'DIV','ASSIGNMENT'
         ,'OPEN_PARENS', 'CLOSE_PARENS', "OR", "NOT", "AND", "IF", "ELSE" ],
        precedence=[('left',['PLUS', 'MINUS', 'NUMBER']),
                    ('left', ['MUL', 'DIV']),
                    ("left", ["LESSEQ", "GREATEREQ", "LESS", "GREATER","EQ", "NOTEQ"]),
                    ("left" , ["AND", "OR", "NOT"])]
    )
    
    @ParseGen.production('program : GOGREEN SEMICOLON statements GOWHITE SEMICOLON')
    def program(id, p: list[Token]):   
        return {
            "type": "program",
            "statements": p[2]
        }
        
    
    @ParseGen.production('statements : statements statement')
    def statements(id, p: list[Token]):
        return [*p[0], p[1]]

    
    @ParseGen.production('statements : statement')
    def single_statement(id, p: list[Token]):
        return [p[0]]
   
        
    @ParseGen.production('statement : SPARTYSAYS expression SEMICOLON')
    def statement_spartysays(id, p: list[Token]):
        id[0] += 1
        return {
            "id": id[0],
            "type": "statement",
            "statement_type": "spartysays",
            "expression": p[1]
        }
    
    @ParseGen.production('statement : NVAR IDENTIFIER ASSIGNMENT expression SEMICOLON')
    @ParseGen.production('statement : SVAR IDENTIFIER ASSIGNMENT expression SEMICOLON')
    def statement_delcaration(id, p: list[Token]):
        statementType = str(p[0].gettokentype()).lower()
        id[0] += 1
        return {
            "id": id[0],
            "type": "statement",
            "statement_type": statementType,
            "identifier": p[1].getstr(),
            "expression": p[3]
        }
   
    @ParseGen.production('statement : IDENTIFIER ASSIGNMENT expression SEMICOLON')
    def statement_assignment(id, p: list[Token]):
        id[0] += 1
        return {
            "id": id[0],
            "type": "statement",
            "statement_type": "assignment",
            "identifier": p[0].getstr(),
            "expression": p[2],
        }
        
    @ParseGen.production('expression : IDENTIFIER' )
    @ParseGen.production('expression : NUMBER' )
    @ParseGen.production('expression : STRING' )
    def expression_token(id, p: list[Token]):
        key = 'identifier' if (str(p[0].gettokentype()) == 'IDENTIFIER') else "value"
        value = p[0].getstr().replace('"', '') 
        if p[0].gettokentype() == 'NUMBER':
            value = float(value)
            if value % 1.0 == 0:
                value = int(value)
            
        id[0] += 1
        return {
                "id": id[0],
                "type": "expression",
                "expression_type": p[0].gettokentype().lower(),
                key: value
            }
        
    @ParseGen.production('boolexp')
    
    @ParseGen.production('expression : OPEN_PARENS expression CLOSE_PARENS')
    def paren_expression(id, p: list[Token]):
        id[0] += 1
        return {
            "id": id[0],
            "type": "expression",
            "expression_type": "parentheses",
            "expression": p[1]
        }
    
    @ParseGen.production('expression : expression PLUS expression')
    @ParseGen.production('expression : expression MINUS expression')
    @ParseGen.production('expression : expression DIV expression')
    @ParseGen.production('expression : expression MUL expression')
    def expression_arithmetic(id,p: list[Token]):
            id[0] += 1
            return {
                "id": id[0],
                "type": "expression",
                "expression_type": str(p[1].gettokentype()).lower(),
                "left": p[0],
                "right": p[2],
            }
            
    
    @ParseGen.error
    def error_handler(id, token: Token):
        raise ValueError({
            "type": "error",
            "tokentype": token.gettokentype(),
            "line": token.getsourcepos().lineno,
            "column": token.getsourcepos().colno,
            "id": id[0],
        }) from AssertionError
        
    
    return ParseGen.build()


class RunTimeState:
    def __init__(self) -> None:
        self.sso = []
        self.pc = 0
        self.scache = {}
        self.som = {}
        self.symtable = {}
        
def evaluate_expression(expression, rts: RunTimeState):
    if expression['expression_type'] == 'parentheses':
        return evaluate_expression(expression['expression'], rts)
    if expression['expression_type'] == "number":
        return expression['value']
    if expression['expression_type'] == 'string':
        return expression['value']
    if  expression['expression_type'] == 'identifier':
        return rts.symtable[expression['identifier']]['value']
    if (op := expression['expression_type']) == 'plus' or op == 'mul' or  op == 'minus' or op =='div':
        return eval_arithmetic_ops(expression['left'], expression['right'], op, rts)
    
    print('Expression evaluation error: unknown expression type')
    
def eval_arithmetic_ops(left, right, op, rts: RunTimeState):
    if op == 'plus':
        left = evaluate_expression(left, rts)  
        right = evaluate_expression(right, rts)
         
        if type(left) == type('') or type(right) == type(''):
            return str(left) + str(right)
        return left + right
         
    if op == 'minus':
        return evaluate_expression(left, rts) - evaluate_expression(right, rts)
    if op == 'mul':
        return evaluate_expression(left, rts) * evaluate_expression(right, rts)
    if op == 'div':
        return evaluate_expression(left, rts) / evaluate_expression(right, rts)
    

def interpret_spartytalk(program):
    ir = parse_spartytalk(program)
    rts = RunTimeState()
    
    count = 0
    
    for statement in ir['statements']:
        rts.sso.append(statement['id'])
        rts.som[statement['id']] = count
        rts.scache[statement['id']] = statement
        count += 1
        
    while True:
        statement = rts.scache[rts.sso[rts.pc]]
        
        if statement['statement_type'] == 'nvar' or statement['statement_type'] == 'svar' or statement['statement_type'] == 'assignment':
            rts.symtable[statement['identifier']] = {
                'value': evaluate_expression(statement['expression'], rts)
            }
            
        if statement['statement_type'] == 'spartysays':
            print(evaluate_expression(statement['expression'], rts))
            
        if rts.pc == len(rts.sso) - 1:
            break
        
        rts.pc = rts.som[rts.sso[rts.pc]] + 1
