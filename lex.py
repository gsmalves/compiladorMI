# -*- coding: UTF-8 -*-
import os
import re

class Lexico:
  def __init__(self, arquivo_fonte):
    '''
    Inicializa o analisador lexico e define o arquivo fonte, que recebe o conteudo do arquivo analisado
    '''
    self.__cabeca = 0
    self.__fita = []
    self.__caracter = ''  
    self.__comentario_aberto = False
    self.__nlinhas = 0
    self.__linha_comentario = 0
    self.__tabela_simbolos = []
    self.__lexema = ''
    self.__cod_lexema = ''
    self.__arquivo_fonte = self.__abre_arquivo(arquivo_fonte)
    self.__palavrasReservadas = ["var", "const", "typedef", "struct", "extends", "procedure" ,"function", "start", "return", "if", "else", "then", "while", "read","print",
        "int",  "real",   "boolean",   "string",   "true",   "false", "global", "local"]

  def __abre_arquivo(self, arquivo_fonte):
    '''
    Abre o arquivo e retorna o seu conteudo separado por linhas
    '''
    if os.path.exists(arquivo_fonte):
        with open(arquivo_fonte, 'r') as file:  
          return file.readlines()
    
  def __adiciona_token(self):
    '''
    Adiciona um token a tabela de simbolos
    '''
    self.__tabela_simbolos.append([self.__nlinhas+1, self.__cabeca,self.__cod_lexema, self.__lexema])
    self.__lexema = ''

  def __avanca_caracter(self):
    '''
    Avança para o proximo caracter da linha, em caso de fim de linha recebe o caracter de quebra de linha
    '''
    if self.__cabeca < len(self.__fita):
      self.__letra = self.__fita[self.__cabeca]
      self.__cabeca += 1
      self.__caracter = str(self.__letra)
    else:
      self.__caracter = "\n"

  def get_tabela_simbolos(self):
    '''
    Gera a tabela de simbolos com a lista de todos os tokens
    '''
    for self.__linha in self.__arquivo_fonte:
        self.__fita = list(self.__linha)
        #print (self.__fita)
        self.__avanca_caracter()
        self.__q0()
        self.__nlinhas += 1
        self.__cabeca = 0
    if self.__comentario_aberto == True:
      self.__nlinhas = self.__linha_comentario
      self.__cod_lexema = "CoMF"
      self.__adiciona_token()    
    return self.__tabela_simbolos
  
  def __q0(self):
    '''
    Distribui os caracteres para os estados responsaveis pelo processamento dos mesmos
    '''
    if self.__comentario_aberto == True:
      self.__q14()
    elif (re.match (r"([A-Za-z])", str(self.__caracter))):
        self.__q01() 
    elif(re.match(r"([0-9])" ,str(self.__caracter))):
      self.__q04()
    elif(re.match(r"[;]|[,]|[.]|[(]|[)]|[{]|[}]|[[]|[]]",str(self.__caracter))):
      self.__q3()  
    elif self.__caracter == '+':
      self.__q07()
    elif self.__caracter == '*':
      self.__q06()
    elif self.__caracter == '-':
      self.__q09()  
    elif self.__caracter == '/"':
      self.__q11()
    elif self.__caracter == '|':
      self.__q19()  
    elif self.__caracter == '&':
      self.__q21() 
    elif self.__caracter == '"':
      self.__q32()     
    elif self.__caracter == '=' or self.__caracter == '<' or self.__caracter == '>' or self.__caracter == '!':
      self.__q23()
    elif self.__caracter == '' or self.__caracter == "\t"  or self.__caracter == ' ':
      self.__avanca_caracter() 
      self.__q0() 
    elif self.__caracter != '\n':
        self.__lexema += self.__caracter
        self.__avanca_caracter()
        self.__q40()

  def __q40(self):
    '''
    Recebe um simbolo invalido e lança seu erro a tabela de simbolos
    '''
    self.__cod_lexema = "SIB"
    self.__adiciona_token()
    self.__q0()

        
  
  def __q01(self):
    '''
    Recebe uma letra minuscula, gera os identificadores e verifica se os mesmos são palavras reservadas
    '''
    self.__lexema += self.__caracter
    self.__avanca_caracter()
    while  (re.match(r"[A-Za-z]|[0-9]|[_]", str(self.__caracter))):
      self.__lexema += self.__caracter
      self.__avanca_caracter()
    if self.__lexema in self.__palavrasReservadas:
      self.__cod_lexema = "PRE"
      self.__adiciona_token()
    else:
      self.__cod_lexema = "IDE"
      self.__adiciona_token()  
    
    self.__q0()

  def __q3(self):
    '''
    Recebe e define os delimitadores
    '''
    self.__lexema += self.__caracter    
    self.__avanca_caracter()
    self.__cod_lexema = "DEL"
    self.__adiciona_token()
    self.__q0()

  def __q04(self):
    '''
    Recebe e delimita os numerais inteiros, e distribui caso seja um numero decimal
    '''
    self.__lexema += self.__caracter
    self.__avanca_caracter()
    while (re.match(r"([0-9])" ,self.__caracter)):
      self.__lexema += self.__caracter
      self.__avanca_caracter()
    if self.__caracter == '.':
      self.__q05()
    else:
      self.__cod_lexema = "NRO"  
      self.__adiciona_token()
      self.__q0()


  def __q05(self):
    '''
    Verifica os numeros reais
    '''
    self.__lexema +=self.__caracter
    self.__avanca_caracter()
    if self.__caracter.isdigit():
      while re.match(r"([0-9])" ,str(self.__caracter)):
        self.__lexema += self.__caracter
        self.__avanca_caracter()
      self.__cod_lexema = "NRO"
    else: 
      while  self.__caracter.isspace()!=True and self.__caracter != '\t' and self.__caracter != '\n':
        self.__lexema += self.__caracter
        self.__avanca_caracter()
      self.__cod_lexema = "NMF"
    self.__adiciona_token() 
    self.__q0()

  def __q06(self):
    '''
    Recebe e define o operador aritimetico de multiplicação
    definido por *
    '''
    self.__lexema += self.__caracter
    self.__cod_lexema = "ART"
    self.__adiciona_token()
    self.__avanca_caracter()
    self.__q0()

  def __q07(self):
    '''
    Recebe e define o operador aritimetico de adição.\n
    definido por +\n
    E distibui em caso de operador de incremento
    ''' 
    self.__lexema += self.__caracter
    self.__avanca_caracter()
    self.__cod_lexema = "ART"
    if self.__caracter == "+":
      self.__q08()
    else:
      self.__adiciona_token()
      self.__q0()

  def __q08(self): 
    '''
    Recebe e define o operador aritimetico de incremento e decremento
    '''
    self.__lexema += self.__caracter
    self.__avanca_caracter()
    self.__adiciona_token()
    self.__q0()
  
  def __q09(self):
    '''
    Recebe e define o operador aritimetico de Subtração.\n
    definido por +\n
    E distibui em caso de operador de decremento
    ''' 
    self.__lexema += self.__caracter
    self.__avanca_caracter()
    self.__cod_lexema = "ART"
    if self.__caracter == "-":
      self.__q08()
    else:
      self.__adiciona_token()
      self.__q0()

  def __q11(self):#Identifica se é o operador aritmetico "/" ou se é um indicador de comentario
    '''
    Recebe e define o perado aritimetico de divisão. Ou verifica se o mesmo forma um comentario de bloco ou linha\n
    Caso isso aconteça distribui para a geração de comentario
    
    '''
    self.__lexema += self.__caracter
    self.__avanca_caracter()
    if self.__caracter == '/':
      self.__q12()
    elif self.__caracter == "*":
      self.__lexema += self.__caracter
      self.__avanca_caracter()
      self.__linha_comentario = self.__nlinhas   
      self.__q14()  
    else:
      self.__cod_lexema = "ART"
      self.__adiciona_token()
      self.__q0()

  def __q12(self):
    '''
    Recebe e define um comentario de linha identificado por //\n
    Ignora toda a linha
    '''
    self.__lexema = ''
    self.__caracter = '\n'
    self.__q0()

  def __q14(self):
    '''
    Recebe e verifica a construção  do comentario de bloco e caso seja bem formado e executa seu fechamento
    '''
    ## verifica Comentario bloco 
    while  self.__caracter != "*":
      if self.__caracter == '\n':
        self.__comentario_aberto = True
        break              
    if self.__caracter == "*":
        self.__avanca_caracter()
        self.__avanca_caracter()
        if self.__caracter == '/':
          self.__lexema = ''
          self.__comentario_aberto = False
          self.__avanca_caracter()  
          self.__q0()
        
 #operadores logicos 
  #Operador Lógico "e" // verifica se não existe um erro lexico
  #caso não exista o erro lança pra o estado q22 que adiciona o lexena de && 
  def __q21(self):
    '''
    Recebe e identifica a contrução do operado logico de "e" definido por &&\n
    Caso seja bem formado indexa o mesmo, 
    caso não seja lança o erro de operador mal formado
    '''
    self.__lexema += self.__caracter
    self.__avanca_caracter()
    if(self.__caracter == '&'):
      self.__lexema += self.__caracter
      self.__cod_lexema = "LOG"
    else:
      self.__cod_lexema = "OpMF"
    self.__adiciona_token()
    self.__q0()
      

  def __q19(self):
    '''
    Recebe e identifica a contrução do operado logico de "ou" definido por ||\n
    Caso seja bem formado indexa o mesmo, 
    caso não seja lança o erro de operador mal formado
    '''
    self.__lexema += self.__caracter
    self.__avanca_caracter()
    if(self.__caracter == "|"):
      self.__lexema += self.__caracter
      self.__cod_lexema = "LOG"
    else:
      self.__cod_lexema = "OpMF"
    self.__adiciona_token()
    self.__q0()
      
    
  def __q23(self): 
    '''
    Recebe e define todos os operadores Relacionais\n
    E operador mal formado no caso de  "!" que não seja seguido por "="
    '''
    self.__lexema += self.__caracter   
    if self.__caracter == '!':
      self.__avanca_caracter()
      if self.__caracter == '=':
        self.__cod_lexema = "REl"
        self.__lexema += self.__caracter
        self.__avanca_caracter()
      else:
        self.__cod_lexema = "LOG"
      self.__adiciona_token()
      self.__q0()
  
    else:  
      self.__avanca_caracter()
      self.__cod_lexema = "REL"
      if self.__caracter == "=":
        self.__lexema += self.__caracter
        self.__avanca_caracter()
      self.__adiciona_token()
      self.__q0()


  def __q32(self):
    '''
    Recebe e estabelece um cadeia de caracteres\n
    Em cado de cadeia mal formada distribui a definição do erro
    '''
    sib_invalido = False
    self.__lexema += self.__caracter
    self.__avanca_caracter()
    while self.__caracter != '\n' and self.__caracter != '\"':
      if (re.match('[\x20-\x21]|[\x23-\x7e]',self.__caracter)!= True):
        sib_invalido = True
      if self.__caracter == '\\':
        self.__q31()
      self.__lexema += self.__caracter  
      self.__avanca_caracter()  
    if sib_invalido == False:     
      if self.__caracter == '"' : 
        self.__lexema += self.__caracter
        self.__cod_lexema = "CAD"
        self.__adiciona_token()
        self.__avanca_caracter()
        self.__q0()
    else:
      self.__lexema += self.__caracter    
    self.__q33()

  '''
  Identifica uma " dentro de uma cadeia de caractere quando não delimitando - a
  '''  
  def __q31(self):
    self.__lexema += self.__caracter
    self.__avanca_caracter()
    if self.__caracter == '"' : #após \
      self.__lexema += '"'
      self.__avanca_caracter()
    else:
      self.__lexema += self.__caracter()
    self.__q32()
        
  
  def __q33(self):
    '''
    Define uma cadeia de caracteres mal formada
    '''
    if re.match('["]' ,self.__lexema):
      self.__cod_lexema = "CMF"
      self.__adiciona_token()
      self.__q0()
    else:
      self.__lexema = ''
      self.__q0()  
