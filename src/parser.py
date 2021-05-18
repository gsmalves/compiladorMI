# -*- coding: UTF-8 -*-


EOF = {'Token': 'EOF', 'Lexeme': '__eof__'}
from token_lex import Token
from follows import Follows
from firsts import Firsts

class Parser:
    def __init__(self, listatokens: list):
        self.listatokens = listatokens
        self.tabelasimbolos = []
        self.iterator = 0
        self.token = self.listatokens[0]
        self.tipo = {'int', 'real', 'boolean'}
    def verify_first(self, production :str):
        '''
        Verifica se o token atual é o esperado conforme a sua produção
        Recebe a Produção
        '''
        if self.eof() :
            return Firsts().get_first(production, self.token.lexema) or Firsts().get_first(production, self.token.cod_token)
        
        
    def setnext_token(self):
        '''
        Avança para o proximo token
        '''
        if self.iterator < len(self.listatokens) - 1:
            self.iterator += 1
            self.token = self.listatokens[self.iterator]
        else:
            self.token = EOF

    def eof(self):
        if self.iterator < len(self.listatokens) - 1:
            return True
        else:
            return False


    def treatment_error(self, tkesperado :str, production :str):
        '''
        Adiciona o erro e o que era esperado e procura o proximo ponto seguro para retornar a analise
        '''
        self.tabelasimbolos.append("{} ERRO SINTÁTICO ESPERAVA:{}".format(self.token.linha, tkesperado))
        while self.eof() != True:
            if Follows().get_follows(production, self.token.lexema) or Follows().get_follows(production, self.token.cod_token):
                break
            else:
                self.setnext_token()
                if self.eof() != True:
                    self.tabelasimbolos.append("ERRO SINTATICO NAO ESPERAVA FIM DE ARQUIVO")    

                

    def add_token(self):
        '''
        Anexa um novo token a tabela de simbolos
        '''
        self.tabelasimbolos.append(self.token)
        self.setnext_token()



   
    def program(self):#Program na linguagem     
        self.global_decl()
        self.start()
        return self.tabelasimbolos

    def global_decl(self):
        '''
        Verifica a existencia de bloco de const e var
        '''
        if self.token.lexema == 'const':
            self.const_decl
            self.var_decl()        
        elif self.token.lexema == 'var':    
            self.var_decl()
            self.const_decl()

    def body(self):
        '''
        Formula a estrutura de recepção de comandos da analise sintatica do corpo do código
        '''
        if self.verify_first('body'):
            self.var_decl()
            self.my_while()
            self.my_if()
            self.read()
            self.my_print()
            #Implemente assign
            #return statement
            if self.verify_first('body'):
                self.body()

    def boolean_literal(self):
        return self.token.lexema in {'true', 'false'}

    def number(self):       
        return self.token.cod_token == 'NRO'
    
    def value(self):
        return self.token.cod_token == 'CAD'  or self.boolean_literal() or self.number()  
             
    def const_decl(self):
        if self.verify_first('constDecl'):
            self.add_token()
            if self.token.lexema == '{':
                self.add_token()
                self.const_list()
                if self.token.lexema == '}':
                    self.add_token()
                else:
                    self.treatment_error('}', 'constDecl') 
            else:
                self.treatment_error('{', 'constDecl')         

    def const_list(self):
        '''
        Verifica a declaração de novas constantes
        '''
        if self.verify_first('type'):
            self.add_token()
            self.const()
            self.const_list()
        
    def const(self):
        if self.token.cod_token == 'IDE':
            self.add_token()
            if self.token.lexema == '=':
                self.add_token()
                if self.verify_first('value'):
                    self.add_token()
                    if self.verify_first('delimiter') :
                        self.delimiter_const()
                    else:
                        self.treatment_error(';', 'const')    
                else:
                    self.treatment_error('VALOR', 'const')    
            else:
                self.treatment_error('=', 'const' )
        else:
            self.treatment_error('IDE')
            

    def delimiter_const(self):#ANCHOR verificar se é util para delimitervar
        '''
        Verifica pelo delimitador da constante
        '''    
        if self.token.lexema == ',':
            self.add_token()
            self.const_list()
        else: 
            self.add_error('DEL', 'delimiterConst')   


    def var_decl(self):
        if self.verify_first('var'):
            self.add_token()
            if self.token.lexema == '{':
                self.add_token()
                self.variable_list()
                if self.token.lexema == '}':
                    self.add_token()
                else:
                    self.treatment_error('}', 'varDecl')
            else:
                self.treatment_error('{', 'varDecl')

            
            

    def variable_list(self):
        if self.verify_first('type'):
            self.add_token()
            self.variable()
            self.variable_list()
        
 
 
    def variable(self):
        if self.token.cod_token == 'IDE':
            self.add_token()
            self.aux()
        else:
            self.treatment_error('IDE', 'variable')
   
    def aux(self): #ANCHOR função incompleta para teste <Aux> ::= '=' <Value> <Delimiter Var> | <Delimiter Var>|  <Vector><Assignment_vector><Delimiter Var>  | <Matrix><Assignment_matrix><Delimiter Var>                                             
        if self.token.lexema == '=':
            self.add_token()
            if self.token.lexema == ';':
                self.delimiter_var()
            elif self.verify_first('value'):
                self.add_token()
                if self.token.lexema == ';':#ANCHOR rever
                    self.add_token()
                else:
                    self.treatment_error(';', 'aux')    
            else:
                self.treatment_error('value', 'aux')    
        else:
            self.treatment_error('=', 'aux')


    def delimiter_var(self):
        if self.token.lexema == ',':
            self.add_token()
            self.variable()
        elif self.token.lexema == ';':
            self.add_token()
        else: 
            self.treatment_error('DEL', 'aux')#ANCHOR o erro busca os tokens do first de aux pq o de delimitador ficaria limitado

    
    def start(self):
        '''
        Verifica o inicio do programa recebendo o bloco de start
        '''
        if self.token.lexema == 'start':
            self.add_token()
            if self.token.lexema == '{':
                self.add_token()
                self.body()
                if self.token.lexema == '}':
                    self.add_token()
                else:
                    self.treatment_error('}', 'varDecl') #ANCHOR rever follow que vai usar
            else:
                self.treatment_error('{', 'varDecl') #ANCHOR rever follow que vai usar
        else:
            self.treatment_error('start', 'varDecl') #ANCHOR rever follow que vai usar

    def decls(self):
        '''
        Gerencia a chamada das declarações
        
        '''
        if self.verify_first('decls'):
            #chamar as funções
            if self.verify_first('decls'):
                self.decls()
    #ANCHOR n tem que fazer tratamento de erro não?


    def formal_parament_list(self):

        if self.verify_first('formalParameterList'):
            self.exp()
            if self.token.lexema == ',':#rever condição de erro
                self.add_token()
                self.formal_parament_list()   
            


    def formal_parament_list_read(self):
        
        if self.verify_first('formalParameterListRead'):
            self.add_token()
            if self.token.lexema == ',':
                self.add_token()
                self.formal_parament_list()
                            
             


    def proc_decl(self):
        if self.token.lexema == 'procedure':
            self.add_token() 
            if self.token.cod_token == 'IDE':
                self.add_token()            
                if self.token.lexema == '(':
                    self.add_token()
                    self.params()
                    if self.token.lexema == ')':
                        self.add_token()
                        if self.token.lexema == '{':
                            self.add_token()
                             #chamar o "bodyProcedure"
                            if self.token.lexema == '}':
                                self.add_token()
                            else:
                                self.treatment_error('}', 'procDecl')
                        else:
                            self.treatment_error('{', 'procDecl') #
                    else:
                        self.treatment_error(')', 'procDecl')    
                else:
                    self.treatment_error('(', 'procDecl')    
            else:
                self.treatment_error('Identificador', 'procDecl')    
        else:
            self.treatment_error('procedure', 'procDecl')
        if  self.token.cod_token == 'IDE':
            self.add_token()       
            if self.token.lexema == '(':
                self.add_token()
                self.formal_parament_list()
                if self.token.lexema == ')':
                    self.add_token()
                    if self.token.lexema == '{':
                        self.add_token()
                            #chamar o "bodyProcedure"
                        if self.token.lexema == '}':
                            self.add_token()
                        else:
                            self.treatment_error('}', 'procDecl')
                    else:
                        self.treatment_error('{', 'procDecl') 
                else:
                    self.treatment_error(')', 'procDecl')    
            else:
                self.treatment_error('(', 'procDecl')    
        else:
            self.treatment_error('Identificador', 'procDecl') 

    def function_call(self):
        if  self.token.cod_token == 'IDE':
            self.add_token()       
            if self.token.lexema == '(':
                self.add_token()
                self.formal_parament_list()
                if self.token.lexema == ')':
                    self.add_token()
                else:
                    self.treatment_error(')', 'functionCall')    
            else:
                self.treatment_error('(', 'functionCall')    
        else:
            self.treatment_error('Identificador', 'functionCall')         
                         
    def function_declaration(self):
        '''
        Identifica a declaração de uma função
        '''
        if self.token.lexema == 'function':
            self.add_token()
            if self.verify_first('type'):
                self.add_token()
                if self.token.cod_token == 'IDE':
                    self.add_token()
                    if self.token.lexema == '(':
                        self.add_token()
                        self.params()
                        if self.token.lexema == ')':
                            self.add_token()
                            if self.token.lexema == '{':
                                self.add_token()
                                #chamar o "bodi"
                                if self.token.lexema == '}':
                                    self.add_token()
                                else:
                                    self.treatment_error('}', 'functionDeclaration') #ANCHOR rever follow que vai usar
                            else:
                                self.treatment_error('{', 'functionDeclaration') #ANCHOR rever follow que vai usar
                        else:
                            self.treatment_error(')', 'functionDeclaration')    
                    else:
                        self.treatment_error('(', 'functionDeclaration')    
                else:
                    self.treatment_error('Identificador', 'functionDeclaration')    
            else:
                self.treatment_error('Tipo', 'functionDeclaration')

    def typedef(self):
        if self.token.lexema == 'typedef':
            self.add_token()
            self.base()
            if self.token.cod_token == 'IDE':
                self.add_token()
                if self.token.lexema == ';':
                    self.add_token()
                else:
                    self.treatment_error(';', 'typedef')
            else:
                self.treatment_error('Identificador', 'typedef')
        else:
            self.treatment_error('typedef', 'typedef')




    def base(self):
        if self.verify_first('type'):#ANCHOR ver se aqui coloca erro ou não
            self.add_token()
        else:
            self.treatment_error('Tipo', 'base') 
        if self.token.lexema == 'struct':
            self.add_token()
            self.extends()
            if self.token.lexema == '{':
                self.add_token()
                self.variable_list
                if self.token.lexema == '}':
                    self.add_token()
                else:
                    self.treatment_error('}', 'base') 
            else:
                self.treatment_error('{', 'base') 
        else:
            self.treatment_error('struct', 'base') 


    def struct_decl(self):
        if self.token.lexema == 'struct':
            self.add_token()
            if self.token.cod_token == 'IDE':
                self.add_token()
                self.extends()
                if self.token.lexema == '{':
                    self.add_token()
                    self.variable_list
                    if self.token.lexema == '}':
                        self.add_token()
                    else:
                        self.treatment_error('}', 'structDecl') 
                else:
                    self.treatment_error('{', 'structDecl') 
            else:
                self.treatment_error('Identificador', 'structDecl') 
        else:
            self.treatment_error('struct', 'structDecl') 





    def extends(self):
        if self.token.lexema == 'extends':
            self.add_token()
            if self.token.cod_token == 'IDE':
                self.add_token()
            else:
                self.treatment_error('Identificador', 'extends') 
        else:
            self.treatment_error('extends', 'extends') 

    def params(self):
        '''
        Identifica os parametros da função
        '''
        if self.token.lexema == 'const':
            self.add_token()
        if self.verify_first('type'):
            self.add_token()
            if self.token.cod_token == 'IDE':
                  self.add_token()
                  if self.token.lexema == ',':#rever condição de erro
                      self.add_token()
                      self.params()   
            else:
                self.treatment_error('Identificador', 'param')
        else:
            self.treatment_error('Tipo', 'param')        
    

    def my_while(self): 
        if self.token.lexema == 'while':
            self.add_token()
            if self.token.lexema == '(':
                self.add_token()
                self.conditional_expression()
                if self.token.lexema == ')':
                    self.add_token()
                    if self.token.lexema == '{':
                        self.add_token()
                        self.body()
                        if self.token.lexema == '}':
                            self.add_token()
                        else:
                            self.treatment_error('}', 'while') #ANCHOR verificar se condição de body seria o ideal
                    else:
                        self.treatment_error('{', 'while') 
                else:
                    self.treatment_error(')', 'while')    
            else:
                self.treatment_error('(', 'while')    

    def expression_value_logical(self):
        if self.verify_first('expressionValueLogical'):
            self.add_token()
        else:
            self.function_call()
            self.relational_expression()

    def conditional_expression(self):
        if self.verify_first('conditionalExpression'):
            if self.boolean_literal():
                self.add_token()
            self.relational_expression()
            self.logical_expression()
                        #ANCHOR terminar função

    def logical_expression(self):
        if self.verify_first('expressionValueLogical'):#ANCHOR ajustar first para identificar value logical
            self.expression_value_logical()
            if self.verify_first('logical'):
                self.logical()
        elif self:#ANCHOR implementar logical e logical deined        
            self.logical_deined()
        else:
            self.treatment_error('Expressão logica', 'logicalExpression')#ANCHOR Rever o follow
        #<Logical Expression> ::= <Expression Value Logical> <Logical> | 
        # <Logical Denied>   

    def logical(self):
        if self.verify_first('conditionalOperator'):
            self.add_token()
            if self.verify_first('expressionValueLogical') or self.verify_first('logicalDeined'): #ANCHOR condição de receber expression value logical ou logical deined
                self.expression_value_logical()
                self.logical_deined()
            else:  
                self.treatment_error('Expressão de valor', 'logical')
        else: 
            self.treatment_error('Operador Condicional', 'logical')                  

    def relational_expression(self):
        self.exp()
        if self.verify_first('relational'):
            self.add_token()
            self.exp()
        
    def my_if(self):
        if self.token.lexema == 'if':
            self.add_token()
            if self.token.lexema == '(':
                self.add_token()
                self.conditional_expression()
                if self.token.lexema == ')':
                    self.add_token()
                    self.then()
                if self.token.lexema == '{':
                    self.add_token()
                    self.body()
                    if self.token.lexema == '}':
                        self.add_token()
                        self.my_else()
                    else:
                        self.treatment_error('}', 'if') 
                else:
                    self.treatment_error('{', 'if')  
            else:
                self.treatment_error('(', 'if')    
     

    def then(self):
        if self.token.lexema == 'then':
            self.add_token()
            self.conditional_expression()
   

    
    def my_else(self):
        if self.token.lexema == 'else':
            self.add_token()
            if self.token.lexema == '{':
                self.add_token()
                self.body()
                if self.token.lexema == '}':
                    self.add_token()
                    self.my_else()
                else:
                    self.treatment_error('}', 'else') 
            else:
                self.treatment_error('{', 'else') 




    

    def read(self):
        '''
        Identifica a validade sintatica da estrutura de read
        '''
        if self.token.lexema == 'read':
            self.add_token()
            if self.token.lexema == '(':
                self.add_token()
                self.formal_parament_list_read()          
                if self.token.lexema == ')':
                    self.add_token()
                    if self.token.lexema == ';':
                        self.add_token()
                    else:
                        self.treatment_error(';', 'read')
                else:                   
                     self.treatment_error(')', 'read')
            else:                   
                self.treatment_error('(', 'read')
        


    def my_print(self):
        '''
        Recebe e verifica a integridade sintatica da função print
        '''
        if self.token.lexema == 'print':
            self.add_token()
            if self.token.lexema == '(':
                self.add_token()
                self.formal_parament_list_read()          
                if self.token.lexema == ')':
                    self.add_token()
                    if self.token.lexema == ';':
                        self.add_token()
                    else:
                        self.treatment_error(';', 'print')
                else:                   
                     self.treatment_error(')', 'print')
            else:                   
                self.treatment_error('(', 'print')
       
    def return_statement(self):
        if self.token.lexema == 'return':
            self.add_token()

            if self.token.lexema == ';':
                self.add_token()
            else:
                self.assign()  


    def index (self):
        if self.verify_first('index'):
            self.add_token()
        else:
            self.treatment_error('Número ou identificador', 'index') 
    
    def vector(self):
        if self.token.lexema == '[':
            self.add_token()
            self.index()
            if self.token.lexema == ']':
                self.add_token()
            else:
                self.treatment_error(']','vector')
        else:
            self.treatment_error('[','vector')

    def matrix(self):
        if self.token.lexema == '[':
            self.add_token()
            self.index()
            if self.token.lexema == ']':
                self.add_token()
                self.vector()
            else:
                self.treatment_error(']','vector')
        else:
            self.treatment_error('[','vector')

    def assignment_vector(self):
        if self.token.lexema == '=':
            self.add_token()
            if self.verify_first('value'):
                self.add_token()
            elif self.token.lexema == '{':
                self.add_token()
                self.value_assigned_vector()
                if self.token.lexema == '}':
                    self.add_token()
                else:
                    self.treatment_error('}','assignmentVector')
            else:
                self.treatment_error('Valor ou {','assignmentVector')     




    def value_assigned_vector(self):
        if self.verify_first('value'):
            self.add_token()
            if self.toke.lexema == ',':
                self.add_token()
                self.value_assigned_vector()
            else:
                pass

    
    def assignment_matrix(self):
        
        self.assignment_vector()#ANCHOR VERIFICAR SE PRECISA DE OUTRO IGUAL AQUI
        if self.token.lexema == '{':
            self.add_token()
            if self.token.lexema == '{':
                self.add_token()
                self.value_assigned_matrix()
                if self.token.lexema == '}':
                    self.add_token()
                    self.dimensao_matrix()
                else:
                    self.treatment_error('}','assignmentMatrix')
            else:
                self.treatment_error('Valor ou {','assignmentMatrix')     
        else:
            self.treatment_error('Valor ou {','assignmentMatrix')  

    def dimensao_matrix(self):
        if self.token.lexema == ',':
            self.add_token()
            if self.token.lexema == '{':
                self.add_token()
                self.value_assigned_matrix()
                if self.token.lexema == '}':
                    self.add_token()
                    if self.token.lexema == '}':
                      self.add_token()
                    else:
                        self.treatment_error('}','dimensionMatrix')
                else:
                    self.treatment_error('}','dimensionMatrix')
            else:
                self.treatment_error('{','dimensionMatrix')
        else:
            self.treatment_error(',','dimensionMatrix')
    
    
    def value_assigned_matrix(self):
        if self.verify_first('value'):
            self.add_token()
            if self.toke.lexema == ',':
                self.add_token()
                self.value_assigned_matrix()
            else:
                pass

    # <Assign> ::= <PrefixGlobalLocal> Identifier '=' <Exp> ';' 
#            | Identifier '=' <Exp> ';'
#            | Identifier <Vector><Assignment_vector> ';' | Identifier <Matrix><Assignment_matrix> ';' | <Exp> ';' 

    def assing(self):
        if self.verify_first('prefixGlobalLocal'):#precisa do erro desse?
            self.prefix_global_local()
            if self.token.cod_token == 'IDE':
                self.add_token()
                if self.token.lexema == '=':
                    self.add_token()
                    self.exp()
                    if self.token.lexema == ';':
                        self.add_token()
                    else:
                        self.treatment_error(';', 'assign')
                else:
                    self.treatment_error('=','assign')
            else:
                self.treatment_error('Identificador','assign')
        if self.token.cod_token == 'IDE':
            self.add_token()
            if self.token.lexema == '=':
                self.add_token()
                self.exp()
                if self.token.lexema == ';':
                    self.add_token()
                else:
                    self.treatment_error(';', 'assign')
            else:
                self.treatment_error('=','assign')
       

    ##falta ainda a parte do vetor

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

 
    def exp(self):
        if self.token.lexema == 'global' or self.token.lexema == 'local':
            self.prefix_global_local()
        self.term()
        if self.token.lexema == '+' or self.token.lexema == '-':
            self.add_token()
            self.exp()
        



    def prefix_global_local(self):#ANCHOR rever 
        if self.token.lexema == 'global' or self.token.lexema == 'local':
            self.add_token()
            if self.token.lexema == '.':
                self.add_token()
                if self.token.cod_token == 'IDE':
                    self.add_token()
                else:
                    self.treatment_error('IDE', 'body')#ANCHOR verificar o que era esperado
            else:
                self.add_error('.', 'prefixGlobalLocal')

    


            


   #ANCHOR acho que precisa fazer uma regex pra pegar 'global' e 'local' ai depois cê olha pra mim  GUSTAVO
    def read_print(self): 
        if self.listatokens[self.iterator].lexema == 'read' or self.listatokens[self.iterator] == 'print':
            self.add_token()
        if self.listatokens[self.iterator].lexema == '(':
            self.add_token()
        else:
            self.add_error('(')    
        self.fp_list_read()
        if self.listatokens[self.iterator].lexema == ')':
            self.add_token()
        else:
            self.add_error(')')                

  

if __name__ == '__main__':
    listatokens =[
        Token(1,'PRE', 'const'),
        Token(1, 'DEL', '{'),
        Token(2, 'PRE', 'int'),
        Token(2, 'IDE', 'a'),
        Token(2, 'REL', '='),
        Token(2, 'NUM', '2'),
        Token(2, 'NUM', ';'),
        Token(2, 'PRE', 'int'),
        Token(2, 'IDE', 'b'),
        Token(2, 'REL', '='),
        Token(2, 'NUM', '2'),
        Token(2, 'NUM', ';'),
        Token(3, 'DEl', '}'),
        Token(4, 'PRE', 'start'),
        Token(4, 'DEL', '{'),
        Token(5, 'IDE', 'Bodiii'),
        Token(6, 'DEL', '}')
        
    ]

    Parser(listatokens).program()
