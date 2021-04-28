"""
<<Program> ::= <Var Decl><Start> 
<Start> ::= 'start' '()' '{' <Body Procedure> '}'
"""
EOF = {'Token': 'EOF', 'Lexeme': '__eof__'}


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
        if self.tokens[self.iterator]['Lexeme'] == 'var':
            print(self.tokens[self.iterator]['Line'],
                  self.tokens[self.iterator]['Token'],
                  self.tokens[self.iterator]['Lexeme'])
            self.setnext_token()
        else:
            print(self.tokens[self.iterator]['Line'],
                  'ERRO SINTÁTICO ESPERAVA:',
                  'var')
            self.setnext_token()
            
        if self.tokens[self.iterator]['Lexeme'] == '{':
            print(self.tokens[self.iterator]['Line'],
                  self.tokens[self.iterator]['Token'],
                  self.tokens[self.iterator]['Lexeme'])
            self.setnext_token()
        else:
            print(self.tokens[self.iterator]['Line'],
                  'ERRO SINTÁTICO ESPERAVA:', '{')
            self.setnext_token()

        if self.tokens[self.iterator]['Lexeme'] == 'int':
            print(self.tokens[self.iterator]['Line'],
                  self.tokens[self.iterator]['Token'],
                  self.tokens[self.iterator]['Lexeme'])
            self.setnext_token()
        else:
            print(self.tokens[self.iterator]['Line'],
                  'ERRO SINTÁTICO ESPERAVA:', 'int')
            self.setnext_token()

        if self.tokens[self.iterator]['Lexeme'] == 'a':
            print(self.tokens[self.iterator]['Line'],
                  self.tokens[self.iterator]['Token'],
                  self.tokens[self.iterator]['Lexeme'])
            self.setnext_token()
        else:
            print(self.tokens[self.iterator]['Line'],
                  'ERRO SINTÁTICO ESPERAVA:', 'a')
            self.setnext_token()

        if self.tokens[self.iterator]['Lexeme'] == '=':
            print(self.tokens[self.iterator]['Line'],
                  self.tokens[self.iterator]['Token'],
                  self.tokens[self.iterator]['Lexeme'])
            self.setnext_token()
        else:
            print(self.tokens[self.iterator]['Line'],
                  'ERRO SINTÁTICO ESPERAVA:', '=')
            self.setnext_token()

        if self.tokens[self.iterator]['Lexeme'] == '2':
            print(self.tokens[self.iterator]['Line'],
                  self.tokens[self.iterator]['Token'],
                  self.tokens[self.iterator]['Lexeme'])
            self.setnext_token()
        else:
            print(self.tokens[self.iterator]['Line'],
                  'ERRO SINTÁTICO ESPERAVA:', '2')
            self.setnext_token()

        if self.tokens[self.iterator]['Lexeme'] == ';':
            print(self.tokens[self.iterator]['Line'],
                  self.tokens[self.iterator]['Token'],
                  self.tokens[self.iterator]['Lexeme'])
            self.setnext_token()
        else:
            print(self.tokens[self.iterator]['Line'],
                  'ERRO SINTÁTICO ESPERAVA:', ';')
            self.setnext_token()

        if self.tokens[self.iterator]['Lexeme'] == '}':
            print(self.tokens[self.iterator]['Line'],
                  self.tokens[self.iterator]['Token'],
                  self.tokens[self.iterator]['Lexeme'])
            self.setnext_token()
        else:
            print(self.tokens[self.iterator]['Line'],
                  'ERRO SINTÁTICO ESPERAVA:', '}')
            self.setnext_token()
    def start(self):
        if self.tokens[self.iterator]['Lexeme'] == 'start':
            print(self.tokens[self.iterator]['Line'],
                  self.tokens[self.iterator]['Token'],
                  self.tokens[self.iterator]['Lexeme'])
            self.setnext_token()
        else:
            print(self.tokens[self.iterator]['Line'],
                  'ERRO SINTÁTICO ESPERAVA:',
                  'start')
            self.setnext_token()

        if self.tokens[self.iterator]['Lexeme'] == '{':
            print(self.tokens[self.iterator]['Line'],
                  self.tokens[self.iterator]['Token'],
                  self.tokens[self.iterator]['Lexeme'])
            self.setnext_token()
        else:
            print(self.tokens[self.iterator]['Line'],
                  'ERRO SINTÁTICO ESPERAVA:', '{')
            self.setnext_token()
        self.program()

        if self.tokens[self.iterator]['Lexeme'] == '}':
            print(self.tokens[self.iterator]['Line'],
                  self.tokens[self.iterator]['Token'],
                  self.tokens[self.iterator]['Lexeme'])
            self.setnext_token()
        else:
            print(self.tokens[self.iterator]['Line'],
                  'ERRO SINTÁTICO ESPERAVA:', '}')
            self.setnext_token()

    def program(self):
        if self.tokens[self.iterator]['Lexeme'] == 'Body':
            print(self.tokens[self.iterator]['Line'],
                  self.tokens[self.iterator]['Token'],
                  self.tokens[self.iterator]['Lexeme'])
            self.setnext_token()
        else:
            print(self.tokens[self.iterator]['Line'],
                  'ERRO SINTÁTICO ESPERAVA:', 'Body')
            self.setnext_token()
        "self.start()"


if __name__ == '__main__':
    tokens = [{'Line': 1, 'Token': 'PRE', 'Lexeme': 'var'},
              {'Line': 1, 'Token': 'DEL', 'Lexeme': '{'},
              {'Line': 2, 'Token': 'PRE', 'Lexeme': 'int'},
              {'Line': 2, 'Token': 'IDE', 'Lexeme': 'a'},
              {'Line': 2, 'Token': 'REL', 'Lexeme': '='},
              {'Line': 2, 'Token': 'NUM', 'Lexeme': '2'},
              {'Line': 2, 'Token': 'DEL', 'Lexeme': '.'},
              {'Line': 3, 'Token': 'DEL', 'Lexeme': '}'},
              {'Line': 4, 'Token': 'PRE', 'Lexeme': 'start'},
              {'Line': 4, 'Token': 'DEL', 'Lexeme': '{'},
              {'Line': 5, 'Token': 'IDE', 'Lexeme': 'Body'},
              {'Line': 6, 'Token': 'DEL', 'Lexeme': '}'}]

    Parser(tokens).init_language()
