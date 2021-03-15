# -*- coding: UTF-8 -*-
import os.path
import os
from os import listdir
from os import walk
import re


from lex import Lexico
var = []
for (dirpath, dirnames, filenames) in walk(r"../input"):
  var +=filenames
if not os.path.exists(r"../output"):
  os.mkdir(r"../output")

for arquivo in var:
  if (re.match(r'(entrada)([0-9])+(\.txt$)' ,str(arquivo))):
    automato = Lexico(arquivo_fonte=arquivo)
    tabelasimbolos = automato.get_tabela_simbolos()
    num_arquivo = re.findall(r'\d+\.txt$', arquivo)
    saida = open("../output/saida"+num_arquivo[0],'w' )
    for simbolo in tabelasimbolos:
      saida.write(simbolo+"\n")
    