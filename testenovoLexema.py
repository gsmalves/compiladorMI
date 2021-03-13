# -*- coding: UTF-8 -*-
import os
import re

class Lexico:
  def __init__(self, arquivo_fonte):
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
    if os.path.exists(arquivo_fonte):
        with open(arquivo_fonte, 'r') as file:  
          return file.readlines()
    
  def __adiciona_token(self):
    self.__tabela_simbolos.append([self.__nlinhas+1, self.__cabeca,self.__cod_lexema, self.__lexema])
    self.__lexema = ''

  def __avanca_cabeca(self):
      self.__cabeca += 1

  def __atualiza_n_linhas(self):
      self.__nlinhas += 1

  def __avanca_caracter(self):
      if self.__cabeca < len(self.__fita):
        self.__letra = self.__fita[self.__cabeca]
        self.__avanca_cabeca()
        self.__caracter = str(self.__letra)
      else:
        self.__caracter = "\n"

  def get_tabela_simbolos(self):
      for self.__linha in self.__arquivo_fonte:
          self.__fita = list(self.__linha)
          #print (self.__fita)
          self.__avanca_caracter()
          self.__q0()
          self.__atualiza_n_linhas()
          self.__cabeca = 0
      if self.__comentario_aberto == True:
        self.__nlinhas = self.__linha_comentario
        self.__cod_lexema = "CoMF"
        self.__adiciona_token()    
      return self.__tabela_simbolos
  
  def __q0(self):
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
    elif self.__caracter == '/':
      self.__q11()
    elif self.__caracter == '|':
      self.__q19()  
    elif self.__caracter == '&':
      self.__q21() 
    elif self.__caracter == '"':
      self.__q30()     
    elif self.__caracter == '' or self.__caracter == "\t" :
      self.__avanca_caracter() 
      self.__q0() 
    else: # default
      if self.__caracter != '\n':
        self.__lexema += self.__caracter
        self.__cod_lexema = "SIB"
        self.__adiciona_token()
        self.__avanca_caracter()
        self.__q0()

        
  
  def __q01(self):
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
    self.__lexema += self.__caracter    
    self.__avanca_caracter()
    self.__cod_lexema = "DEL"
    self.__adiciona_token()
    self.__q0()

  def __q04(self):## verifica se é numeral // q04
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


  def __q05(self):## verifica se é numeral depois do ponto
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

  def __q06(self):# multiplicação
    self.__lexema += self.__caracter
    self.__cod_lexema = "ART"
    self.__adiciona_token()
    self.__caracter = self.__avanca_caracter
    self.__q0()

  def __q07(self):# Operador Aritmetico de Adição 
    self.__lexema += self.__caracter
    self.__avanca_caracter()
    self.__cod_lexema = "ART"
    if self.__caracter == "+":
      self.__q08()
    else:
      self.__adiciona_token()
      self.__q0()

  def __q08(self): #Operador de incremento
    self.__lexema += self.__caracter
    self.__avanca_caracter()
    self.__adiciona_token()
    self.__q0()
  
  def __q09(self):# Operador Aritmetico de Subtração 
    self.__lexema += self.__caracter
    self.__avanca_caracter()
    self.__cod_lexema = "ART"
    if self.__caracter == "-":
      self.__q08()
    else:
      self.__adiciona_token()
      self.__q0()

  def __q10(self): #Operador de decremento
    self.__lexema += self.__caracter
    self.__avanca_caracter()
    self.__adiciona_token()
    self.__q0()


  def __q11(self):#Identifica se é o operador aritmetico "/" ou se é um indicador de comentario
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

  def __q12(self):#comentario de linha
    self.__lexema = ''
    self.__caracter = '\n'
    self.__q0()

  def __q14(self):## verifica Comentario bloco 
    while  self.__caracter != "*":
      self.__avanca_caracter()
      if self.__caracter == '\n':
        self.__comentario_aberto = True
        break              
    if self.__caracter == "*":
        self.__q15()  
        
  
  def __q15(self):## verifica comentário bloco
    self.__avanca_caracter()
    if self.__caracter != "/":
        self.__q14()     
    else:
        self.__q16()  
        
    
  def __q16(self):#comentario de bloco
    self.__lexema = ''
    self.__comentario_aberto = False
    print("fechei")
    self.__avanca_caracter()  
    self.__q0()
 #operadores logicos 
  #Operador Lógico "e" // verifica se não existe um erro lexico
  #caso não exista o erro lança pra o estado q22 que adiciona o lexena de && 
  def __q21(self):
    self.__lexema += self.__caracter
    self.__avanca_caracter()
    if(self.__caracter == "&"):
      self.__q22()
    else:
      self.__cod_lexema = "OpMF"
      self.__adiciona_token()
      self.__avanca_caracter()
      self.__q0()
      
  def __q22(self):#Lança o lexema de operador logico "e"
    self.__lexema += self.__caracter
    self.__cod_lexema = "LOG"
    self.__adiciona_token()
    self.__q0()

  def __q19(self):
    self.__lexema += self.__caracter
    self.__avanca_caracter()
    if(self.__caracter == "|"):
      self.__q20()
    else:
      self.__cod_lexema = "OpMF"
      self.__adiciona_token()
      self.__avanca_caracter()
      self.__q0()
      
  def __q20(self):#Lança o lexema de operador logico "e"
    self.__lexema += self.__caracter
    self.__cod_lexema = "LOG"
    self.__adiciona_token()
    self.__q0()
    
  def __q30(self):# cadeia de caracter    
    self.__lexema += self.__caracter
    self.__avanca_caracter()
    if self.__caracter == '"' :
      self.__q34()
    elif self.__caracter == '\\':
      self.__q32()
    elif (re.match('[\x20-\x21]|[\x23-\x7e]',self.__caracter)) :
      self.__q32()
    else:
      print("erro")

  def __q31(self):
    self.__lexema += self.__caracter
    self.__avanca_caracter()
    if self.__caracter == '"' : #após \
      self.__q33()
    elif (re.match('[\x20-\x21]|[\x23-\x7e]',self.__caracter)) :
      self.__q32()
        
  def __q32(self):
    self.__lexema += self.__caracter
    self.__avanca_caracter()
    while  (re.match('[\x20-\x21]|[\x23-\x7e]',self.__caracter)):
      self.__lexema += self.__caracter
      self.__avanca_caracter()
    if self.__caracter == '\\':
      self.__q31()
    elif self.__caracter == '"' : 
      self.__q34()
    else:
      print("erro") # fazer estado de erro para tratar todos possíveis
  
  def __q33(self):
    self.__lexema += self.__caracter
    self.__avanca_caracter()
    if (re.match('[\x20-\x21]|[\x23-\x7e]',self.__caracter)):
      self.__q32()
    elif self.__caracter == '"' : 
      self.__q34()
    else:
      print("erro") 
  
  def __q34(self):
    self.__lexema += self.__caracter
    self.__cod_lexema = "CAD"
    self.__adiciona_token()
    self.__lexema = ''
    self.__caracter = self.__avanca_caracter
    self.__q0()

  

if __name__ == "__main__":
    lex = Lexico("entrada2.txt") 
    __tabela_simbolos = lex.get_tabela_simbolos()    
    for simbolo  in __tabela_simbolos:
      print (simbolo)