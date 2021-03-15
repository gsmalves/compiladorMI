# -*- coding: UTF-8 -*-
import os.path
import os
from os import listdir
from os import walk
import re


from lex import Lexico
var = []
#var+=walk(r"../input")[3]
for (dirpath, dirnames, filenames) in walk(r"../input"):
  var +=filenames
if not os.path.exists(r"../output"):
  os.mkdir(r"../output")
diretorio = listdir(r"../input")
for arquivo in var:
  print(arquivo)
  regex = '(entrada)\d+\.tx$'
  if (re.match(regex ,arquivo)):
    print("o arquivo é "+ arquivo)
    automato = Lexico(arquivo_fonte=arquivo)
    tabelasimbolos = automato.get_tabela_simbolos()
    saida = open("../output/"+arquivo,'w' )
    for simbolo in tabelasimbolos:
      # print(type(simbolo))
      # #print('Resultado ---> ', ''.join(str(simbolo))).replace("'", "")
      saida.write(simbolo+"\n")
    