# -*- coding: UTF-8 -*-
import os.path
import os
from os import listdir

from lex import Lexico

if not os.path.exists(r"../output"):
  os.mkdir(r"../output")
diretorio = listdir(r"../input")
for arquivo in diretorio:
  print(os.path.abspath(arquivo))
  # #automato = Lexico(arquivo_fonte=os.path.abspath(arquivo))
  # tabelasimbolos = automato.get_tabela_simbolos()
  # saida = open("../output/saida{}.txt".format(i),'w' )
  # for simbolo in tabelasimbolos:
  #   # print(type(simbolo))
  #   # #print('Resultado ---> ', ''.join(str(simbolo))).replace("'", "")
  #   saida.write(simbolo+"\n")
    