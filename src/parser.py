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
        self.tipo = {'int', 'real', 'boolean'}

    def setnext_token(self):
        if self.iterator < len(self.tokens) - 1:
            self.iterator += 1
            self.token = self.tokens[self.iterator]
        else:
            self.token = EOF
    def error_print(self, tkesperado :str): #vamo ter que lançar bonitinho mas acho que por enquanto serve
        print(self.token,
            'ERRO SINTÁTICO ESPERAVA:',tkesperado)
   
    def getprevious_token(self):
        token = self.tokens[self.iterator - 1]
        return token

    # def program(self): #ANCHOR implementar program

    # def global_decl(self):#ANCHOR implementar globaldecl

    # def const_decl(self)#ANCHOR implementar declaração de constantes        


    # def body_procedure(self): # ANCHOR implementar bodyprocedure 
    #     #gramatica body 
    #     # <Body Procedure>  ::=  <Body Item Procedure><Body Procedure> 
    #     #<Body Item Procedure>  ::=  <Var Decl>
    #             #  | <While Procedure>
    #             #  | <If Procedure>
    #             #  | <Read>
    #             #  | <Print>
    #             #  | <Assign>         |
    #             # 
    # def fp_list_read(self):#Formal Parameter List Read ANCHOR implementar list read e colocar no read
    
    # def conditional_expresion(self):#ANCHOR implementar espressões condicionais 

    # def prefix_global_local(self):

        
    def read_print(self): 
        if self.tokens[self.iterator].lexema == 'read' or self.tokens[self.iterator] == 'print':
            print(self.tokens[self.iterator])
        self.iterator +=1
        if self.tokens[self.iterator].lexema == '(':
            print(self.tokens[self.iterator])
        else:
            self.error_print('(')    
        self.fp_list_read()
        self.iterator +=1
        if self.tokens[self.iterator].lexema == ')':
            print(self.tokens[self.iterator])
        else:
            self.error_print(')')                

                
    def eof(self):
        if self.iterator < len(self.tokens) - 1:
            return True
        else:
            return False

    def init_language(self):     
        self.var_decl()
        self.start()

    def boolean_literal(self):
        return self.tokens[self.iterator].lexema in {'true', 'false'}

    def number(self):       
        return self.tokens[self.iterator].lexema == 'NRO'
    
    def value(self):
        return self.tokens[self.iterator].cod_token == 'CAD'  or self.boolean_literal() or self.number()  
             
        
    def var_decl(self):
        if self.tokens[self.iterator].lexema == 'var':
            print(self.tokens[self.iterator])
            self.setnext_token()
        else:
            print(self.tokens[self.iterator].linha,
                  'ERRO SINTÁTICO ESPERAVA:',
                  'var')
            self.setnext_token()
            
        if self.tokens[self.iterator].lexema == '{':
            print(self.tokens[self.iterator])
            self.setnext_token()

        else:
            print(self.tokens[self.iterator].linha,
                  'ERRO SINTÁTICO ESPERAVA:', '{')
            self.setnext_token()


        while self.tokens[self.iterator].lexema in self.tipo:#ANCHOR falta implementar para pegar o identifier de string
            #ANCHOR printar o tipo 
            self.setnext_token()
            self.declara_var()



        if self.tokens[self.iterator].lexema == '}':
            print(self.tokens[self.iterator])
            self.setnext_token()
        else:
            print(self.tokens[self.iterator].linha,
                'ERRO SINTÁTICO ESPERAVA:', '}')
            self.setnext_token()
    
    def declara_var(self):
        if self.tokens[self.iterator].cod_token == 'IDE':
            print(self.tokens[self.iterator])
        else:
            print(self.tokens[self.iterator].linha,
                  'ERRO SINTÁTICO ESPERAVA:', 'IDE')
        self.setnext_token()

        if self.tokens[self.iterator].lexema == '=':
            print(self.tokens[self.iterator])
        else:
            print(self.tokens[self.iterator].linha,
                  'ERRO SINTÁTICO ESPERAVA:', '=')
        self.setnext_token()

        if self.value() : 
            print(self.tokens[self.iterator])
        else:
            print(self.tokens[self.iterator].linha,
                  'ERRO SINTÁTICO ESPERAVA:', 'Value')
        self.setnext_token()

        if self.tokens[self.iterator].lexema == ';':
            print(self.tokens[self.iterator])
        else:
            print(self.tokens[self.iterator].linha,
                  'ERRO SINTÁTICO ESPERAVA:', ';')
        self.setnext_token()

    
    def start(self):
        if self.tokens[self.iterator].lexema == 'start':
            print(self.tokens[self.iterator])
            self.setnext_token()
        else:
            print(self.tokens[self.iterator].linha,
                  'ERRO SINTÁTICO ESPERAVA:',
                  'start')
            self.setnext_token()

        if self.tokens[self.iterator].lexema == '{':
            print(self.tokens[self.iterator])
            self.setnext_token()
        else:
            print(self.tokens[self.iterator].linha,
                  'ERRO SINTÁTICO ESPERAVA:', '{')
            self.setnext_token()
        #self.program()

        if self.tokens[self.iterator].lexema == '}':
            print(self.tokens[self.iterator])
            self.setnext_token()
        else:
            print(self.tokens[self.iterator].linha,
                  'ERRO SINTÁTICO ESPERAVA:', '}')
            self.setnext_token()

    # def program(self):
    #     if self.tokens[self.iterator].lexema == 'Body':
    #         print(self.tokens[self.iterator])
    #         self.setnext_token()
    #     else:
    #         print(self.tokens[self.iterator].linha,
    #               'ERRO SINTÁTICO ESPERAVA:', 'Body')
    #         self.setnext_token()
    #     "self.start()"


if __name__ == '__main__':
    tokens =[
        Token(1,'PRE', 'var'),
        Token(1, 'DEL', '{'),
        Token(2, 'PRE', 'int'),
        Token(2, 'IDE', 'a'),
        Token(2, 'REL', '='),
        Token(2, 'NUM', '2'),
        Token(2, 'NUM', ';'),
        Token(3, 'DEl', '}'),
        Token(4, 'PRE', 'start'),
        Token(4, 'DEL', '{'),
        Token(5, 'IDE', 'Bodiii'),
        Token(6, 'DEL', '}')
        
    ]

   

    Parser(tokens).init_language()
