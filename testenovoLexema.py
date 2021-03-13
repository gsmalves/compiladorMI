# -*- coding: UTF-8 -*-
import os
import re

class Lexico:
  def __init__(self, arquivo_fonte):
      self.__cabeca = 0
      self.__fita = []
      self.__caracter = ''
      self.__nlinhas = 0
      self.__tabela_simbolos = []
      self.__lexema = ''
      self.__cod_lexema = ''
      self.arquivo_lido = self.__abre_arquivo(arquivo_fonte)

  def __abre_arquivo(self, arquivo_fonte)-> list:
    if os.path.exists(arquivo_fonte):
        with open(arquivo_fonte, 'r') as file:  
          return file.readlines()
    
  def __adiciona_token(self):
    self.__tabela_simbolos.append([self.__nlinhas, self.__cabeca,self.__cod_lexema, self.__lexema])
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
      return self.__tabela_simbolos
  
  def __q0(self):
    if(re.match(r"([0-9])" ,str(self.__caracter))):
      self.__q04()
    elif self.__caracter == '+':
      self.__q07()
    elif self.__caracter == '*':
      self.__q06()
    elif self.__caracter == " " or self.__caracter == "\t":
      self.__avanca_caracter() 
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
      while self.__caracter.isdigit():
        self.__lexema += self.__caracter
        self.__avanca_caracter()
    else: 
      while  self.__caracter != " " and self.__caracter != "\t" and self.__caracter != "\n":
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
    if self.__caracter == "+":
      self.__cod_lexema = "ART"
      self.__q08()
    else:
      self.__adiciona_token()
      self.__q0()

  def __q08(self): #Operador de incremento
    self.__lexema += self.__caracter
    self.__avanca_caracter()
    self.__adiciona_token()
    self.__q0()
  

if __name__ == "__main__":
    lex = Lexico("entrada2.txt") 
    __tabela_simbolos = lex.get_tabela_simbolos()    
    for simbolo  in __tabela_simbolos:
      print(simbolo)