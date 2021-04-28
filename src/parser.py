# -*- coding: UTF-8 -*-
"""
<<Program> ::= <Var Decl><Start> 
<Start> ::= 'start' '()' '{' <Body Procedure> '}'
"""
EOF = {'Token': 'EOF', 'Lexeme': '__eof__'}
from token_lex import Token

class Parser:
    def __init__(self, tokens: list):
        self.tokens = tokens
        self.iterator = 0
        self.token = {}

    def setnext_token(self):
        if self.iterator < len(self.tokens) - 1:
            self.iterator += 1
            self.token = self.tokens[self.iterator]
        else:
            self.token = EOF

    def getprevious_token(self):
        token = self.tokens[self.iterator - 1]
        return token

    def eof(self):
        if self.iterator < len(self.tokens) - 1:
            return True
        else:
            return False

    def init_language(self):
        
        self.var()
        self.start()
        
        
    def var(self):
        if self.tokens[self.iterator].lexema == 'var':
            print(self.tokens[self.iterator].linha,
                  self.tokens[self.iterator].cod_lexema,
                  self.tokens[self.iterator].lexema)
            self.setnext_token()
        else:
            print(self.tokens[self.iterator].linha,
                  'ERRO SINTÁTICO ESPERAVA:',
                  'var')
            self.setnext_token()
            
        if self.tokens[self.iterator].lexema == '{':
            print(self.tokens[self.iterator].linha,
                  self.tokens[self.iterator].cod_lexema,
                  self.tokens[self.iterator].lexema)
            self.setnext_token()
        else:
            print(self.tokens[self.iterator].linha,
                  'ERRO SINTÁTICO ESPERAVA:', '{')
            self.setnext_token()

        if self.tokens[self.iterator].lexema == 'int':
            print(self.tokens[self.iterator].linha,
                  self.tokens[self.iterator].cod_lexema,
                  self.tokens[self.iterator].lexema)
            self.setnext_token()
        else:
            print(self.tokens[self.iterator].linha,
                  'ERRO SINTÁTICO ESPERAVA:', 'int')
            self.setnext_token()

        if self.tokens[self.iterator].lexema == 'a':
            print(self.tokens[self.iterator].linha,
                  self.tokens[self.iterator].cod_lexema,
                  self.tokens[self.iterator].lexema)
            self.setnext_token()
        else:
            print(self.tokens[self.iterator].linha,
                  'ERRO SINTÁTICO ESPERAVA:', 'a')
            self.setnext_token()

        if self.tokens[self.iterator].lexema == '=':
            print(self.tokens[self.iterator].linha,
                  self.tokens[self.iterator].cod_lexema,
                  self.tokens[self.iterator].lexema)
            self.setnext_token()
        else:
            print(self.tokens[self.iterator].linha,
                  'ERRO SINTÁTICO ESPERAVA:', '=')
            self.setnext_token()

        if self.tokens[self.iterator].lexema == '2':
            print(self.tokens[self.iterator].linha,
                  self.tokens[self.iterator].cod_lexema,
                  self.tokens[self.iterator].lexema)
            self.setnext_token()
        else:
            print(self.tokens[self.iterator].linha,
                  'ERRO SINTÁTICO ESPERAVA:', '2')
            self.setnext_token()

        if self.tokens[self.iterator].lexema == ';':
            print(self.tokens[self.iterator].linha,
                  self.tokens[self.iterator].cod_lexema,
                  self.tokens[self.iterator].lexema)
            self.setnext_token()
        else:
            print(self.tokens[self.iterator].linha,
                  'ERRO SINTÁTICO ESPERAVA:', ';')
            self.setnext_token()

        if self.tokens[self.iterator].lexema == '}':
            print(self.tokens[self.iterator].linha,
                  self.tokens[self.iterator].cod_lexema,
                  self.tokens[self.iterator].lexema)
            self.setnext_token()
        else:
            print(self.tokens[self.iterator].linha,
                  'ERRO SINTÁTICO ESPERAVA:', '}')
            self.setnext_token()
    def start(self):
        if self.tokens[self.iterator].lexema == 'start':
            print(self.tokens[self.iterator].linha,
                  self.tokens[self.iterator].cod_lexema,
                  self.tokens[self.iterator].lexema)
            self.setnext_token()
        else:
            print(self.tokens[self.iterator].linha,
                  'ERRO SINTÁTICO ESPERAVA:',
                  'start')
            self.setnext_token()

        if self.tokens[self.iterator].lexema == '{':
            print(self.tokens[self.iterator].linha,
                  self.tokens[self.iterator].cod_lexema,
                  self.tokens[self.iterator].lexema)
            self.setnext_token()
        else:
            print(self.tokens[self.iterator].linha,
                  'ERRO SINTÁTICO ESPERAVA:', '{')
            self.setnext_token()
        self.program()

        if self.tokens[self.iterator].lexema == '}':
            print(self.tokens[self.iterator].linha,
                  self.tokens[self.iterator].cod_lexema,
                  self.tokens[self.iterator].lexema)
            self.setnext_token()
        else:
            print(self.tokens[self.iterator].linha,
                  'ERRO SINTÁTICO ESPERAVA:', '}')
            self.setnext_token()

    def program(self):
        if self.tokens[self.iterator].lexema == 'Body':
            print(self.tokens[self.iterator].linha,
                  self.tokens[self.iterator].cod_lexema,
                  self.tokens[self.iterator].lexema)
            self.setnext_token()
        else:
            print(self.tokens[self.iterator].linha,
                  'ERRO SINTÁTICO ESPERAVA:', 'Body')
            self.setnext_token()
        "self.start()"


if __name__ == '__main__':
    tokens =[
        Token(1,'PRE', 'var'),
        Token(1, 'DEL', '{'),
        Token(2, 'PRE', 'int'),
        Token(2, 'IDE', 'a'),
        Token(2, 'REL', '='),
        Token(2, 'NUM', '2'),
        Token(3, 'DEl', '}'),
        Token(4, 'PRE', 'start'),
        Token(4, 'DEL', '{'),
        Token(5, 'IDE', 'Body'),
        Token(6, 'DEL', '}')
        
    ]

   

    Parser(tokens).init_language()
