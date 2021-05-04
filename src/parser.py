# -*- coding: UTF-8 -*-
#ANCHOR Gustavo man eu sei que esse codigo tá uma bagunça, eu pegeui e comecei a implementar a gramatica, dai fiz assim, fui vendo o que cada função precisava e fui fazendo recursão pra começar sempre do mais simples. tô remando aqui, mas vou deixa a ultima versão do git baixada, caso queira voltar atrás

"""
<<Program> ::= <Var Decl><Start> 
<Start> ::= 'start' '()' '{' <Body Procedure> '}'
"""
EOF = {'Token': 'EOF', 'Lexeme': '__eof__'}
from token_lex import Token

class Parser:
    def __init__(self, tokens: list):
        self.tokens = tokens
        self.tabelasimbolos = []
        self.iterator = 0
        self.token = self.tokens[0]
        self.tipo = {'int', 'real', 'boolean'}
    
    def setnext_token(self):
        '''
        Avança para o proximo token
        '''
        if self.iterator < len(self.tokens) - 1:
            self.iterator += 1
            self.token = self.tokens[self.iterator]
        else:
            self.token = EOF

    
    def add_error(self, tkesperado :str): #vamo ter que lançar bonitinho mas acho que por enquanto serve
        '''
        Adiciona um novo erro e sua descrição a tabela de simbolos
        '''
        self.tabelasimbolos.append("{} ERRO SINTÁTICO ESPERAVA:{}".format(self.token.linha, tkesperado))
        self.setnext_token()

    def add_token(self):
        '''
        Anexa um novo token a tabela de simbolos
        '''
        self.tabelasimbolos.append(self.token)
        self.setnext_token()

    def getprevious_token(self):#ANCHOR verificar se é util
        '''
        Verifica o token anterior
        '''    
        token = self.tokens[self.iterator - 1]
        return token


    #def global_decl(self):#ANCHOR implementar globaldecl

      

    #def expression_value_logic(self):#ANCHOR implementar função condicional expressãoi de valor logico 

   
    def program(self):#Program na linguagem     
        self.const_decl()
        self.var_decl()
        self.start()
        return self.tabelasimbolos

                
    def eof(self):#ANCHOR ver se ainda é util
        if self.iterator < len(self.tokens) - 1:
            return True
        else:
            return False


    def boolean_literal(self):
        return self.token.lexema in {'true', 'false'}

    def number(self):       
        return self.token.cod_token == 'NRO'
    
    def value(self):
        return self.token.cod_token == 'CAD'  or self.boolean_literal() or self.number()  
             
    def const_decl(self):
        if self.token.lexema == 'const':
            self.add_token()
            if self.token.lexema == '{':
                self.add_token()
                self.const_list()
                if self.token.lexema == '}':
                    self.add_token()
                else:
                    self.add_error('}')
            else:
                self.add_error('{')
        else:
            self.add_error('const')

    def const_list(self):
        if self.token.lexema in self.tipo:
            self.add_token()
            self.const()
            self.const_list()
        
    def const(self):
        if self.token.cod_token == 'IDE':
            self.add_token()
            self.aux()
            if self.token.lexema == '=':
                self.add_token()
                if self.value():
                    self.add_token()
                    if self.token.lexema == ';' or self.token.lexema == ',' :#ANCHOR FIQUEI NA DUVIDA SE CHAMO OU N ADDTOKEN
                        self.delimiter_const()
                    else:
                        add_error(';')    
                else:
                    self.add_error('value')    
            else:
                self.add_error('=')
        else:
            self.add_error('IDE')

    def delimiter_const(self):
        if self.token.lexema == ',':
            self.add_token()
            self.const()
        elif self.token.lexema == ';':
            self.add_token()
        else: 
            self.add_error('DEL')#ANCHOR rever      


    def var_decl(self):
        if self.token.lexema == 'var':
            self.add_token()
            if self.token.lexema == '{':
                self.add_token()
                self.variable_list()
                if self.token.lexema == '}':
                    self.add_token()
                else:
                    self.add_error('}')
            else:
                self.add_error('{')
        else:
            self.add_error('var')
            
            

    def variable_list(self):
        if self.token.lexema in self.tipo:
            self.add_token()
            self.variable()
            self.variable_list()
        
 
 
    def variable(self):
        if self.token.cod_token == 'IDE':
            self.add_token()
            self.aux()
        else:
            self.add_error('IDE')

    def aux(self): #ANCHOR função incompleta para teste <Aux> ::= '=' <Value> <Delimiter Var> | <Delimiter Var>|  <Vector><Assignment_vector><Delimiter Var>  | <Matrix><Assignment_matrix><Delimiter Var>                                             
        if self.token.lexema == '=':
            self.add_token()
            if self.token.lexema == ';':
                self.delimiter_var()
            elif self.value():
                self.add_token()
                if self.token.lexema == ';':#ANCHOR rever
                    self.add_token()
                else:
                    add_error(';')    
            else:
                self.add_error('value')    
        else:
            self.add_error('=')


    def delimiter_var(self):
        if self.token.lexema == ',':
            self.add_token()
            self.variable()
        elif self.token.lexema == ';':
            self.add_token()
        else: 
            self.add_error('DEL')#ANCHOR rever      


    
    def start(self):#ANCHOR verificar se vai pegar a partir do start ou n
        if self.token.lexema == 'start':
            self.add_token()
        else:
            self.add_error('start')

        if self.tokens[self.iterator].lexema == '{':
            self.add_token()
        else:
            print(self.tokens[self.iterator].linha,
                  'ERRO SINTÁTICO ESPERAVA:', '{')
            self.setnext_token()
        
        #self.program()#ANCHOR ver se vai chamar o program, daqui ou não ver na gramatica

        if self.token.lexema == '}':
            self.add_token()
        else:
            self.add_error('}')

    def expression_value(self):   
        if self.token.lexema == '-':
            self.add_token()
            self.expression_value()
        elif self.number() or self.boolean_literal()  or self.token.cod_token == 'STR'  :
            self.add_token()
        elif self.token.lexema == '(':
            self.add_token()
            self.exp()
            if self.token == ')':
                self.add_token()
            else: 
                self.add_error(')')
        elif self.token.cod_token == 'IDE':
            self.add_token()
            if self.token == '(':
                self.function_call()

    def term(self):
        self.expression_value()
        self.mult_exp()


    def mult_exp(self):
        if self.token.lexema == '*':
            self.term()
        elif self.token.lexema == '/':
            self.term()    

 
    def exp(self): #ANCHOR implementar função exp
        pass
        #<Exp> ::= <PrefixGlobalLocal> <Term> <Add Exp> | <Term> <Add Exp>


    #def formal_parameter_list(self):#ANCHOR implementar depende da funçao exp
    
    def function_call(self):
        '''
        Recebe passagem quando um identificador é proceguido de um (
        Funcionamento: aciona o formal parameter list e verifica o fechamento de parenteses
        '''
        self.formal_parameter_list()
        if self.token == ')':
            print(self.token)
        else:
            self.add_error(')')    
       # def conditional_expresion(self):#ANCHOR implementar espressões condicionais 

    # def logical(self):#ANCHOR  implementar função logical 

    # def condicional_operator(self):#ANCHOR  implementa  função condicional operator


    def prefix_global_local(self):#ANCHOR rever 
        if self.token.lexema == 'global' or self.token.lexema == 'local':
            self.add_token()
            if self.token.lexema == '.':
                self.add_token()
                if self.token.cod_token == 'IDE':
                    self.add_token()
                else:
                    self.add_error('IDE')#ANCHOR verificar o que era esperado
            else:
                self.add_error('.')

    
    def exp(self):
        self.prefix_global_local()

            







    #     #ANCHOR acho que precisa fazer uma regex pra pegar 'global' e 'local' ai depois cê olha pra mim  GUSTAVO
    def read_print(self): 
        if self.tokens[self.iterator].lexema == 'read' or self.tokens[self.iterator] == 'print':
            self.add_token()
        if self.tokens[self.iterator].lexema == '(':
            self.add_token()
        else:
            self.add_error('(')    
        self.fp_list_read()
        if self.tokens[self.iterator].lexema == ')':
            self.add_token()
        else:
            self.add_error(')')                

    
    #def body_procedure(self): # ANCHOR implementar bodyprocedure 
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

    Parser(tokens).program()
