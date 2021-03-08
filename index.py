# -*- coding: UTF-8 -*-
import os.path

from lex import Lexico

for i in range(10):
  if os.path.isfile('entrada{}.txt'.format(i)):
    __automato = Lexico(arquivo_fonte="entrada{}.txt".format(i))
    __tabelasimbolos = __automato.getTabelaSimbolos()
    __saida = open("saida{}.txt".format(i),'w' )
    for j in range(len(__tabelasimbolos)):
        __saida.write(str(__tabelasimbolos[j])+"\n")
    