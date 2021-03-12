# -*- coding: UTF-8 -*-
import os
import re

class Lexico:
  def __init__(self, arquivo_fonte):
      self.__cabeca = 0
      self.__fita = []
      
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
          #if self.__letra != self.__finalLinha or not self.__letra.isspace():
              #self.__lexema += self.__letra
          return self.__letra
      else:
          return self.__finalLinha

  def getTabelaSimbolos(self):
      for self.__linha in self.__arquivo_fonte:
          self.__fita = list(self.__linha)
          #print (self.__fita)
          self.__caracter = self.__getCaracter()
          self.__distribuicao()
          self.__atualiza_nLinhas()
          self.__cabeca = 0
      self.__arquivo_fonte.close() 
      return self.__tabelaSimbolos
  
  def __distribuicao(self):#q00
    if(re.match(r"([0-9])" ,self.__caracter)):
      self.__numeralInteiro()
    elif self.__caracter == '+':
      self.__operadorAdicao()
    elif self.__caracter == " " or self.__caracter == "\t":
      self.__caracter = self.__getCaracter() 
      self.__distribuicao() 
  

  def __numeralInteiro(self):## verifica se é numeral // q04
    self.__lexema += self.__caracter
    self.__caracter = self.__getCaracter()
    while (re.match(r"([0-9])" ,self.__caracter)):
      self.__lexema += self.__caracter
      self.__caracter = self.__getCaracter()
    self.__codLexema = "NRO"  
    self.__adicionaToken()
    self.__distribuicao()

  def __operadorAdicao(self):# Operador Aritmetico de Adição // q07
    self.__lexema += self.__caracter
    self.__caracter = self.__getCaracter()
    #if self.__caracter == "+":
      #self.__q08()
    #else:
    self.__adicionaToken()
    self.__distribuicao()

if __name__ == "__main__":
    lex = Lexico("entrada2.txt") 
    __tabelasimbolos = lex.getTabelaSimbolos()    
    for j in range(len(__tabelasimbolos)):
      print(str(__tabelasimbolos[j])+"\n")