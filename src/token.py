# -*- coding: UTF-8 -*-
class Token:

  def __init__(self, linha, cod_lexema, lexema):
    self.linha = linha
    self.cod_lexema = cod_lexema
    self.lexema = lexema
  
  def __str__(self):
    if self.line <= 9:
      return "0{self.linha} {self.cod_lexema} {self.lexema}"
    else:
      return "{self.linha} {self.cod_lexema} {self.lexema}"  
    
