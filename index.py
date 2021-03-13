# -*- coding: UTF-8 -*-
import os.path

from lex import Lexico

for i in range(10):
  if os.path.isfile('entrada{}.txt'.format(i)):
    automato = Lexico(arquivo_fonte="entrada{}.txt".format(i))
    tabelasimbolos = automato.getTabelaSimbolos()
    saida = open("saida{}.txt".format(i),'w' )
    for simbolo in tabelasimbolos:
        saida.write(simbolo+"\n")
    