class Token:
  def __init__(self, linha, lexema,cod_token):
    self.linha = linha
    self.lexema = lexema
    self.cod_token = cod_token
    
  def __str__(self):
       return "{} {} {}".format(self.linha, self.lexema, self.cod_token)

if __name__ == '__main__':
  meme = Token(1, "meme", "CAD")
  print(meme)  