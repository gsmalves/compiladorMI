# -*- coding: UTF-8 -*-

class Parser:
  def __init__(self, list_token):
    self.list_token = list_token  
    self.__iterator = 0
    self.__token = {}
    
  def __proximo_token(self):
    if self.__iterator < self.list_token.len() -1:
      self.__iterator +=1
      self.__token = self.list_token[self.__iterator]
    else:
      self.__token = NULL  
  def __anterior_token(self):




  def sintatic_analizer(self):
    self.__cabeca = 0
    self.

if __name__ == '__main__':
    tokens = [{'Linha': 1, 'Cod_Lexema': 'PRE', 'Lexema': 'procedure'},
              {'Linha': 1, 'Cod_Lexema': 'PRE', 'Lexema': 'start'},
              {'Linha': 1, 'Cod_Lexema': 'DEL', 'Lexema': '{'},
              {'Linha': 2, 'Cod_Lexema': 'IDE', 'Lexema': 'Statement'},
              {'Linha': 3, 'Cod_Lexema': 'DEL', 'Lexema': '}'}]

    Parser(Cod_Lexemas).init_language()
