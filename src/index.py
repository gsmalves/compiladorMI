# Autores: Gustavo dos Santos Menezes Alves e Hiago Rangel de Almeida
# Componente Curricular: MI - PROCESSADORES DE LINGUAGEM DE PROGRAMAÇÃO
# Concluido em: 15/03/2021
# Declaro que este código foi elaborado por nós de forma individual e não contém nenhum
# trecho de código de outro colega ou de outro autor, tais como provindos de livros e
# apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
# de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
# do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.




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
    