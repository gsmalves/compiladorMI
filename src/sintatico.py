# -*- coding: UTF-8 -*-


EOF = {'Token': 'EOF', 'Lexeme': '__eof__'}
from typing import Iterator
from token_lex import Token
from follows import Follows
from firsts import Firsts

symbol = []
symbolFunction = []
isGlobal = False
isUsed = False

isUsed = False
Scope = 'Global'
TypeFunc = ''
TypeVar = ''
TypeConst = ''
Param = ''

def set_TypeConst(value):
    global TypeConst
    TypeConst = value


def get_TypeConst():
    return TypeConst


def set_TypeVar(value):
    global TypeVar
    TypeVar = value


def get_TypeVar():
    return TypeVar


def set_TypeFunc(value):
    global TypeFunc
    TypeFunc = value


def get_TypeFunc():
    return TypeFunc


def get_param():
    return Param

def set_param(value):
    global Param
    Param = value

def set_Scope(value):
    global Scope
    Scope = value


def get_Scope():
    return Scope


def set_isUsed(value):
    global isUsed
    isUsed = value


def get_isUsed():
    return isUsed



def set_isGlobal(value):
    global isGlobal
    isGlobal = value

def get_isGlobal():
    return isGlobal

# def add_symbol_function(line,token ,lexeme,type,param1,scope,used ):
#     status = 'OK'
#     if exists_symbol(lexeme, scope):
#         status = 'ERROR'

#     symbol.append({'Line': line,
#                    'Token': token,
#                    'Lexeme': lexeme,
#                    'Type': type,
#                    'Param1': param1,
                  
#                    'Scope': scope,
#                    'Status': status,
#                    })



def add_symbol(line, token, lexeme, type, category, scope, used):
    status = 'OK'
    if exists_symbol(lexeme, scope):
        status = 'ERROR'

    symbol.append({'Line': line,
                   'Token': token,
                   'Lexeme': lexeme,
                   'Type': type,
                   'Category': category,
                   'Scope': scope,
                   'Used': used,
                   'Status': status,
                   })


def escopo(line, lexeme, type, category):
    for element in symbol:
        if element['Lexeme'] == lexeme:
            print('ERRO', line, lexeme, type, category)


def exists_symbol(lexeme, scope):
    for element in symbol:
        if element['Lexeme'] == lexeme and element['Scope'] == scope:
            "print(line, 'ERRO SEMÂNTICO:', lexeme)"
            return True
    return False






class Parser:
    def __init__(self, listatokens: list):
        self.listatokens = listatokens
        self.tabelasimbolos = []
        self.iterator = 0
        self.error = 0
        self.token = self.listatokens[0]
        self.tipo = {'int', 'real', 'boolean'}
    def verify_first(self, production :str):
        '''
        Verifica se o token atual é o esperado conforme a sua produção
        Recebe a Produção
        '''
        if self.eof() :
            return Firsts().get_first(production, self.token.lexema) or Firsts().get_first(production, self.token.cod_token)
        
    def setprev_token(self):
        self.iterator -=1
        self.token = self.listatokens[self.iterator]   

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
        self.error +=1
        while self.eof() != True:
            if Follows().get_follows(production, self.token.lexema) or Follows().get_follows(production, self.token.cod_token):
                break
            else:
                self.setnext_token()
                if self.eof() != True:
                    self.tabelasimbolos.append("ERRO SINTATICO NAO ESPERAVA FIM DE ARQUIVO")    
                    break

                

    def add_token(self):
        '''
        Anexa um novo token a tabela de simbolos
        '''
        self.tabelasimbolos.append(self.token)
        self.setnext_token()



   
    def program(self):    
        self.global_decl()
        self.decls()
        self.start()
        if self.error != 0:
            print('Analise sintatica concluida com falhas')
            print('O Arquivo possui {} erros'.format(self.error))
        else:
            print('Arquivo analisado com sucesso')
            
        print(
            "________________________________________________________________________________________________________________")
        print('{:^15}'.format('Linha'), '{:^15}'.format('Token'), '{:^15}'.format('Lexema'), '{:^15}'.format('Tipo'),
              '{:^15}'.format('Categoria'), '{:^15}'.format('Escopo'), '{:^15}'.format('Usado'), '{:^15}'.format('Status'),)
        print(
            "________________________________________________________________________________________________________________")
        for element in symbol:
            print('{:^15}'.format(element['Line']), '{:^15}'.format(element['Token']),
                  '{:^15}'.format(element['Lexeme']),
                  '{:^15}'.format(element['Type']), '{:^15}'.format(element['Category']),
                  '{:^15}'.format(element['Scope']),
                  '{:^15}'.format(str(element['Used'])), '{:^15}'.format(str(element['Status'])),)


            #print(
            #     "________________________________________________________________________________________________________________")
            # print('{:^15}'.format('Line'), '{:^15}'.format('Tokeni'), '{:^15}'.format('Lexemai'), '{:^15}'.format('Retorno'),
            #       '{:^15}'.format('Parametro1'), '{:^15}'.format('Escopo'), '{:^15}'.format('Status'),)
            # print(
            #     "________________________________________________________________________________________________________________")
            # for element in symbolFunction:
            #     print('{:^15}'.format(element['Line']), '{:^15}'.format(element['Token']),
            #           '{:^15}'.format(element['Lexeme']),'{:^15}'.format(element['Type']),
            #           '{:^15}'.format(element['Param1']),
            #           '{:^15}'.format(str(element['Scope'])), '{:^15}'.format(str(element['Status'])),)
        return self.tabelasimbolos

    def global_decl(self):
        '''
        Verifica a existencia de bloco de const e var
        '''
        if self.token.lexema == 'const':
            self.const_decl()
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
            self.assign()
            self.return_statement()
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
            set_TypeConst(self.token.lexema)
            self.type()
            add_symbol(line=self.token.linha, token=self.token.cod_token, lexeme=self.token.lexema, type=get_TypeConst(),
                                category='const', scope=get_Scope(), used=False)

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
            

    def delimiter_const(self):
        '''
        Verifica pelo delimitador da constante
        '''    
        if self.token.lexema == ',':
            self.add_token()
            self.const()
        elif self.token.lexema == ';':
            self.add_token()    
        else: 
            self.treatment_error('DEL', 'delimiterConst')   


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
            set_TypeVar(self.token.lexema)
            self.type()
            add_symbol(line=self.token.linha, token=self.token.cod_token, lexeme=self.token.lexema, type=get_TypeVar(),
                       category='var', scope=get_Scope(), used=False)
            self.variable()
            self.variable_list()
        
 
 
    def variable(self):
        if self.token.cod_token == 'IDE':
            self.add_token()
            self.aux()
        else:
            self.treatment_error('IDE', 'variable')
   
    def aux(self): 
        if self.token.lexema == '=':
            self.add_token()
            if self.verify_first('value'):
                self.add_token()
                if self.token.lexema == ';' or ',':
                    self.delimiter_var() 
            else:
                self.treatment_error('Valor', 'aux')  
        elif self.verify_first('delimiter'):
            self.delimiter_var()
        elif self.verify_first('vector'):
            self.vector()
            self.assignment_vector()
            self.delimiter_var()
        else:
            self.treatment_error('=', 'aux')

    def delimiter_var(self):
        if self.token.lexema == ',':
            self.add_token()
            self.variable()
        elif self.token.lexema == ';':
            self.add_token()
        else: 
            self.treatment_error('DEL', 'aux')


    def start(self):
        '''
        Verifica o inicio do programa recebendo o bloco de start
        '''
        if self.token.lexema == 'start':
            self.add_token()
            if self.token.lexema == "(":         
                self.add_token()
                if self.token.lexema == ")":
                    self.add_token()
                    if self.token.lexema == '{':
                        self.add_token()
                        self.body()
                        if self.token.lexema == '}':
                            self.add_token()
                        else:
                            self.treatment_error('}', 'varDecl') 
                    else:
                        self.treatment_error('{', 'varDecl')
                else:
                    self.treatment_error(")", "varDecl")         
            else:
                self.treatment_error("(", "varDecl")       
        else:
            self.treatment_error('start', 'varDecl') 

    def decls(self):
        '''
        Gerencia a chamada das declarações
        
        '''
        if self.verify_first('decls'):
            self.struct_decl()
            self.function_declaration()
            self.proc_decl()
            self.typedef()
            if self.verify_first('decls'):
                self.decls()



    def formal_parament_list(self):

        if self.verify_first('formalParameterList'):
            self.exp()
            if self.token.lexema == ',':
                self.add_token()
                self.formal_parament_list()   
            


    def formal_parament_list_read(self):
        
        if self.verify_first('formalParameterListRead'):
            self.add_token()
            if self.token.lexema == ',':
                self.add_token()
                self.formal_parament_list()
                            
    def body_proc(self):
        if self.verify_first('bodyProcedure'):
            self.var_decl()
            self.if_proc()       
            self.while_proc()
            self.assign()
            self.my_print()
            self.read()
            if self.verify_first('bodyProcedure'):
                self.body_proc()


    def proc_decl(self):
        if self.token.lexema == 'procedure':
            self.add_token() 
            if self.token.cod_token == 'IDE':
                set_Scope(self.token.lexema)           
                self.add_token() 
                if self.token.lexema == '(':
                    self.add_token()
                    self.params()
                    if self.token.lexema == ')':
                        self.add_token()
                        if self.token.lexema == '{':
                            self.add_token()
                            self.body_proc()
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
        if  self.token.cod_token == 'IDE':
            self.add_token()       
            if self.token.lexema == '(':
                self.add_token()
                self.formal_parament_list()
                if self.token.lexema == ')':
                    self.add_token()
                    if self.token.lexema == '{':
                        self.add_token()
                        self.body_proc()
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


    def function_call(self):
        if  self.token.cod_token == 'IDE':
            self.add_token()       
            if self.token.lexema == '(':
                self.add_token()
                self.formal_parament_list()
                if self.token.lexema == ')':
                    self.add_token()
                    if self.token.lexema == ';':
                        self.add_token()
                    else:
                        self.treatment_error(';', 'functionCall')    
                else:
                    
                    self.treatment_error(')', 'functionCall')    
            else:
                self.treatment_error('(', 'functionCall')    
    
    def function_aux(self):    
         if  self.token.cod_token == 'IDE':
            self.add_token()       
            if self.token.lexema == '(':
                self.add_token()
                self.formal_parament_list()
                if self.token.lexema == ')':
                    self.add_token()
                else:
                    self.treatment_error(')', 'functionCall')    

                         
    def function_declaration(self):
        '''
        Identifica a declaração de uma função
        '''
        if self.token.lexema == 'function':
            self.add_token()
            if self.verify_first('type'):
                set_TypeFunc(self.token.lexema)
                self.type()
                if self.token.cod_token == 'IDE':
                    set_Scope(self.token.lexema)           
                    self.add_token()
                    if self.token.lexema == '(':
                        self.add_token()
                        set_param(self.token.lexema)
                        self.params()
                        # add_symbol_function(line=self.token.linha, token=self.token.cod_token, lexeme=self.token.lexema, type=get_TypeFunc(),
                        #             param1=get_param(), scope=get_Scope(), used=False)
                        if self.token.lexema == ')':
                            self.add_token()
                            if self.token.lexema == '{':
                                self.add_token()
                                self.body()
                                if self.token.lexema == '}':
                                    self.add_token()
                                else:
                                    self.treatment_error('}', 'functionDeclaration')
                            else:
                                self.treatment_error('{', 'functionDeclaration') 
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
        
    def type(self):
        if self.token.lexema == 'struct':
            self.add_token()
            if self.token.cod_token == 'IDE':
                set_TypeVar(self.token.lexema)
                self.add_token()
            else:
                self.treatment_error('IDE','type')  
        else:
            self.add_token()        



    def base(self):
        if self.verify_first('type'):
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
                set_Scope(self.token.lexema)
                self.add_token()
                self.extends()
                if self.token.lexema == '{':
                    self.add_token()
                    self.variable_list()
                    if self.token.lexema == '}':
                        self.add_token()
                    else:
                        self.treatment_error('}', 'structDecl') 
                else:
                    self.treatment_error('{', 'structDecl') 
            else:
                self.treatment_error('Identificador', 'structDecl') 
         





    def extends(self):
        if self.token.lexema == 'extends':
            self.add_token()
            if self.token.cod_token == 'IDE':
                self.add_token()
            else:
                self.treatment_error('Identificador', 'extends') 


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
                  if self.token.lexema == ',':
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
                            self.treatment_error('}', 'while') 
                    else:
                        self.treatment_error('{', 'while') 
                else:
                    self.treatment_error(')', 'while')    
            else:
                self.treatment_error('(', 'while')    
    
    def while_proc(self): 
        if self.token.lexema == 'while':
            self.add_token()
            if self.token.lexema == '(':
                self.add_token()
                self.conditional_expression()
                if self.token.lexema == ')':
                    self.add_token()
                    if self.token.lexema == '{':
                        self.add_token()
                        self.body_proc()
                        if self.token.lexema == '}':
                            self.add_token()
                        else:
                            self.treatment_error('}', 'while') 
                    else:
                        self.treatment_error('{', 'while') 
                else:
                    self.treatment_error(')', 'while')    
            else:
                self.treatment_error('(', 'while')    

    def expression_value_logical(self):
        if self.verify_first('expressionValueLogical'):
            self.add_token()
        elif self.token.lexema == 'IDE':
            self.setnext_token()
            if self.token.lexema == '(':
                self.setprev_token()    
                self.function_call()
            else:
                self.add_token()
            self.relational_expression()

    def conditional_expression(self):

        if self.verify_first('conditionalExpression'):
            if self.verify_first('prefixGlobalLocal'):
                self.prefix_global_local()
            else:
                self.setnext_token()
                if self.token.lexema == {'+', '-', '/', '*'}:
                    self.setprev_token()
                    self.add_token()
                    self.exp()
                    self.relational_expression()
                elif self.verify_first('relational'): 
                    self.setprev_token()
                    self.add_token()
                    self.relational_expression()
                else:
                    self.setprev_token()
                    self.add_token()
                    self.logical_expression()


    def logical_expression(self):
        if self.verify_first('logical'):
            self.add_token()
            self.expression_value_logical()

       
    def logical(self):
        if self.verify_first('conditionalOperator'):
            self.add_token()
            if self.verify_first('expressionValueLogical') or self.token.lexema == '!':
                self.expression_value_logical()
                self.logical_denied()
                if self.verify_first('relational'):
                    self.relational_expression()
                    if self.token.lexema != ')':
                        pass
            else:  
                self.treatment_error('Expressão de valor ', 'logical')
        else: 
            self.treatment_error('Operador Condicional', 'logical')                  

    def logical_denied(self):
        if self.token.lexema == '!':
            self.add_token()
            if self.boolean_literal or self.identifier():
                self.add_token()
            elif self.verify_first('exp') or self.verify_first('relational'):
                self.relational_expression() 
        
    def relational_expression(self):
        if self.verify_first('relational'):
            self.add_token()
            self.exp()
            if self.verify_first('logical'):
                self.logical()
 



        
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
   
    def if_proc(self):
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
                        self.body_proc()
                        if self.token.lexema == '}':
                            self.add_token()
                            self.else_proc()
                        else:
                            self.treatment_error('}', 'if') 
                    else:
                        self.treatment_error('{', 'if')  
                else:
                    self.treatment_error(')', 'if')    
            else:
                self.treatment_error('(', 'if')    
    

    
    def then(self):
        if self.token.lexema == 'then':
            self.add_token()
            self.conditional_expression()
   

    def else_proc(self):
        if self.token.lexema == 'else':
            self.add_token()
            if self.token.lexema == '{':
                self.add_token()
                self.body_proc()
                if self.token.lexema == '}':
                    self.add_token()
                    self.else_proc()
                else:
                    self.treatment_error('}', 'else') 
            else:
                self.treatment_error('{', 'else') 

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
                if self.verify_first('vector'):
                    self.matrix()
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
            else:
                self.treatment_error(']','vector')
        
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
        else:
            self.treatment_error('Valor','valueAssignedVector')
    
    def assignment_matrix(self):
        
        self.assignment_vector()
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
        else:
            self.treatment_error('Valor','valueAssignedMatrix')
           

    def assign(self):
        if self.verify_first('prefixGlobalLocal'):
            self.prefix_global_local()
            if self.token.lexema == '=':
                self.add_token()
                self.exp()
                if self.token.lexema == ';':
                    self.add_token()
                    self.assign()
                else:
                    self.treatment_error(';', 'assign')
            else:
                self.treatment_error('=','assign')
        if self.token.cod_token == 'IDE':
            self.setnext_token() 
            if self.token.lexema == '(':
                self.setprev_token()
                self.function_call()
            else:
                self.setprev_token()    
                self.add_token()
                if self.token.lexema == '.':
                    self.add_token()
                    if self.token.cod_token == 'IDE':
                        self.add_token()
                    else:
                        self.treatment_error('IDE', 'assign')    
                if self.token.lexema == '=':
                    self.add_token()    
                    self.exp()
                    if self.token.lexema == ';':
                        self.add_token()     
                    elif self.verify_first('vector'):
                        self.vector()
                        self.assignment_vector()
                        if self.token.lexema == ';':
                            self.add_token()
                        else:
                            self.treatment_error(';', 'assign')
                    elif self.verify_first('matrix'):
                        self.matrix()
                        self.assignment_matrix()        
                        if self.token.lexema == ';':
                            self.add_token()
                        else:
                            self.treatment_error(';', 'assign')
                    else:
                        self.treatment_error('= ou [','assign')
        elif self.verify_first('exp') or self.verify_first('expressionValue') or self.token.cod_token == 'IDE':
            self.exp()
            if self.token.lexema == ';':
                self.add_token()
            else:
                self.treatment_error(';', 'assign')
  
    def expression_value(self):   
        if self.token.lexema == '-':
            self.add_token()
            self.expression_value()
        elif self.number() or self.boolean_literal()  or self.token.cod_token == 'CAD'  :
            self.add_token()
        elif self.token.cod_token == 'IDE':
            self.function_aux()
        elif self.token.lexema == '(':
            self.add_token()
            self.exp()
            if self.token == ')':
                self.add_token()
            else:
                self.treatment_error(')', 'expressionValue')    
     

    

    def term(self):
        if self.verify_first('expressionValue'):
            self.expression_value()
            self.mult_exp()
        else:
            self.treatment_error('Expressão de Valor', 'term')    


    def mult_exp(self):
        if self.token.lexema == '*':
            self.term()
        elif self.token.lexema == '/':
            self.term()    
    
    def exp(self):
        if self.verify_first('prefixGlobalLocal'):
            self.prefix_global_local()
        self.term()
        if self.token.lexema == '+' or self.token.lexema == '-':
            self.add_token()
            self.exp()

    


    def prefix_global_local(self): 
        if self.token.lexema == 'global' or self.token.lexema == 'local':
            self.add_token()
            if self.token.lexema == '.':
                self.add_token()
                if self.token.cod_token == 'IDE':
                    self.add_token()
                else:
                    self.treatment_error('IDE', 'body')
                    self.treatment_error('.', 'prefixGlobalLocal')