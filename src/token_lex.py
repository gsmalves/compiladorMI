class Token:
  def __init__(self, linha,  cod_lexema, lexema):
    self.linha = linha
    self.lexema = lexema
    self.cod_lexema = cod_lexema
    
  def __str__(self):
       return "{} {} {}".format(self.linha, self.cod_lexema, self.lexema)

if __name__ == '__main__':
  meme = Token(1, "meme", "CAD")
  print(meme)  