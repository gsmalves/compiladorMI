# -*- coding: UTF-8 -*-
import os
import re

class Lexico:
  def __init__(self, arquivo_fonte):
      self.__cabeca = 0
      self.__fita = []
      self.__caracter = ''
      self.__nlinhas = 0
      self.__tabelaSimbolos = []
      self.__lexema = ''
      self.__finalLinha = '\n'
      self.__codLexema = ''
      if os.path.exists(arquivo_fonte):
          self.__arquivo_fonte = open(arquivo_fonte, 'r')
      else:
          print("Erro: Arquivo não existe.")
          exit()

  def __adicionaToken(self):
    self.__tabelaSimbolos.append([self.__nlinhas, self.__cabeca,self.__codLexema, self.__lexema])
    self.__lexema = ''

  def __avancaCabeca(self):
      self.__cabeca += 1

  def __posicaoCabeca(self):
      return self.__cabeca

  def __atualiza_nLinhas(self):
      self.__nlinhas += 1

  def __getCaracter(self):
      if self.__cabeca < len(self.__fita):
        self.__letra = self.__fita[self.__cabeca]
        self.__avancaCabeca()
        self.__caracter = str(self.__letra)
      else:
        self.__caracter = str(self.__finalLinha)

  def getTabelaSimbolos(self):
      for self.__linha in self.__arquivo_fonte:
          self.__fita = list(self.__linha)
          #print (self.__fita)
          self.__getCaracter()
          self.__q0()
          self.__atualiza_nLinhas()
          self.__cabeca = 0
      self.__arquivo_fonte.close() 
      return self.__tabelaSimbolos
  
  def __q0(self):
    if(re.match(r"([0-9])" ,str(self.__caracter))):
      self.__q04()
    elif self.__caracter == '+':
      self.__q07()
    elif self.__caracter == '*':
      self.__q06()
    elif self.__caracter == " " or self.__caracter == "\t":
      self.__getCaracter() 
      self.__q0() 
  

  def __q04(self):## verifica se é numeral // q04
    self.__lexema += self.__caracter
    self.__getCaracter()
    while (re.match(r"([0-9])" ,self.__caracter)):
      self.__lexema += self.__caracter
      self.__getCaracter()
    if self.__caracter == '.':
      self.__q05()
    else:
      self.__codLexema = "NRO"  
      self.__adicionaToken()
      self.__q0()


  def __q05(self):## verifica se é numeral depois do ponto
    self.__lexema +=self.__caracter
    self.__getCaracter()
    if self.__caracter.isdigit():
      while self.__caracter.isdigit():
        self.__lexema += self.__caracter
        self.__getCaracter()
    else: 
      while  self.__caracter != " " and self.__caracter != "\t" and self.__caracter != "\n":
        self.__lexema += self.__caracter
        self.__getCaracter()
      self.__codLexema = "NMF"
      self.__adicionaToken() 
    self.__q0()

  def __q06(self):# multiplicação
    self.__lexema += self.__caracter
    self.__codLexema = "ART"
    self.__adicionaToken()
    self.__caracter = self.__getCaracter
    self.__q0()


  def __q07(self):# Operador Aritmetico de Adição 
    self.__lexema += self.__caracter
    self.__getCaracter()
    if self.__caracter == "+":
      self.__codLexema = "ART"
      self.__q08()
    else:
      self.__adicionaToken()
      self.__q0()

  def __q08(self): #Operador de incremento
    self.__lexema += self.__caracter
    self.__getCaracter()
    self.__adicionaToken()
    self.__q0()
  
  


if __name__ == "__main__":
    lex = Lexico("entrada2.txt") 
    __tabelasimbolos = lex.getTabelaSimbolos()    
    for j in range(len(__tabelasimbolos)):
      print(str(__tabelasimbolos[j])+"\n")