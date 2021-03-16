# -*- coding: UTF-8 -*-
# Autores: Gustavo dos Santos Menezes Alves e Hiago Rangel de Almeida
# Componente Curricular: MI - PROCESSADORES DE LINGUAGEM DE PROGRAMAÇÃO
# Concluido em: 15/03/2021
# Declaro que este código foi elaborado por nós de forma individual e não contém nenhum
# trecho de código de outro colega ou de outro autor, tais como provindos de livros e
# apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
# de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
# do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
import os
import re

class Lexico:
  def __init__(self, arquivo_fonte):
    '''
    Inicializa o analisador lexico e define o arquivo fonte, que recebe o conteúdo do arquivo analisado
    '''
    self.__cabeca = 0
    self.__incidencia_de_erro = 0
    self.__fita = []
    self.__caracter = ''  
    self.__comentario_aberto = False
    self.__n_linhas = 0
    self.__linha_comentario = 0
    self.__tabela_simbolos = []
    self.__lexema = ''
    self.__cod_lexema = ''
    self.nome_arquivo = arquivo_fonte
    self.__arquivo_fonte = self.__abre_arquivo(arquivo_fonte)
    self.__palavrasReservadas = {"var", "const", "typedef", "struct", "extends", "procedure" ,"function", "start", "return", "if", "else", "then", "while", "read","print",
        "int",  "real",   "boolean",   "string",   "true",   "false", "global", "local"}

  def __abre_arquivo(self, arquivo_fonte):
    '''
    Abre o arquivo e retorna o seu conteudo separado por linhas
    '''
    if os.path.exists("../input/"+arquivo_fonte):
      with open("../input/"+arquivo_fonte, 'r') as file:  
        return file.readlines()
    
  def __adiciona_token(self):
    '''
    Adiciona um token a tabela de simbolos
    '''
    self.__tabela_simbolos.append(str("{} {} {}").format(self.__n_linhas+1, self.__cod_lexema, self.__lexema))
    self.__lexema = ''

    

  def __avanca_caracter(self):
    '''
    Avança para o proximo caracter da linha, em caso de fim de linha recebe o caracter de quebra de linha
    '''
    if self.__cabeca < len(self.__fita):
      self.__letra = self.__fita[self.__cabeca]
      self.__cabeca += 1
      self.__caracter = str(self.__letra)
    else:
      self.__caracter = "\n"

  def get_tabela_simbolos(self):
    '''
    Gera a tabela de simbolos com a lista de todos os tokens
    '''
    for self.__linha in self.__arquivo_fonte:
        self.__fita = list(self.__linha)
        #print (self.__fita)
        self.__avanca_caracter()
        self.__q0()
        self.__n_linhas += 1
        self.__cabeca = 0
    if self.__comentario_aberto == True:
      self.__n_linhas = self.__linha_comentario
      self.__cod_lexema = "CoMF"
      self.__incidencia_de_erro +=1
      self.__adiciona_token()    
    print("Arquivo analisado: {}".format(self.nome_arquivo))
    if self.__incidencia_de_erro != 0:
      print("O Arquivo Analisado contem {} erros\n".format(self.__incidencia_de_erro))
      self.__tabela_simbolos.append(str("\n\n\nO arquivo analisado contem {} erros\n\n\n".format(self.__incidencia_de_erro)))
    else:
      print("O arquivo Analisado não contem erros\n")  

    return self.__tabela_simbolos
  
  def __q0(self):
    '''
    Distribui os caracteres para os estados responsaveis pelo processamento dos mesmos
    '''
    if self.__comentario_aberto == True:
      self.__q14()
    elif (re.match (r"([A-Za-z])", str(self.__caracter))):
        self.__q01() 
    elif(re.match(r"([0-9])" ,str(self.__caracter))):
      self.__q04()
    elif(re.match(r"[;]|[,]|[.]|[(]|[)]|[{]|[}]|[[]|[]]",str(self.__caracter))):
      self.__q3()  
    elif self.__caracter == '+':
      self.__q07()
    elif self.__caracter == '*':
      self.__q06()
    elif self.__caracter == '-':
      self.__q09()  
    elif self.__caracter == '/':
      self.__q11()
    elif self.__caracter == '|':
      self.__q19()  
    elif self.__caracter == '&':
      self.__q21() 
    elif self.__caracter == '"':
      self.__q32()     
    elif self.__caracter == '=' or self.__caracter == '<' or self.__caracter == '>' or self.__caracter == '!':
      self.__q23()
    elif self.__caracter == '' or self.__caracter == "\t"  or self.__caracter == ' ' or self.__caracter == '\r':
      self.__avanca_caracter() 
      self.__q0() 
    elif self.__caracter != '\n':
        self.__lexema += self.__caracter
        self.__avanca_caracter()
        self.__q40()


        
  
  def __q01(self):
    '''
    Recebe uma letra , gera os identificadores e verifica se os mesmos são palavras reservadas
    '''
    self.__lexema += self.__caracter
    self.__avanca_caracter()
    while  (re.match(r"[A-Za-z]|[0-9]|[_]", str(self.__caracter))):
      self.__lexema += self.__caracter
      self.__avanca_caracter()
    if self.__lexema in self.__palavrasReservadas:
      self.__cod_lexema = "PRE"
      self.__adiciona_token()
    else:
      self.__cod_lexema = "IDE"
      self.__adiciona_token()  
    
    self.__q0()

  def __q3(self):
    '''
    Recebe e define os delimitadores
    '''
    self.__lexema += self.__caracter    
    self.__avanca_caracter()
    self.__cod_lexema = "DEL"
    self.__adiciona_token()
    self.__q0()

  def __q04(self):
    '''
    Recebe os numerais inteiros, e distribui caso seja um numero decimal
    '''
    self.__lexema += self.__caracter
    self.__avanca_caracter()
    while (re.match(r"([0-9])" ,self.__caracter)):
      self.__lexema += self.__caracter
      self.__avanca_caracter()
    if self.__caracter == '.':
      self.__q05()
    else:
      self.__cod_lexema = "NRO"  
      self.__adiciona_token()
      self.__q0()


  def __q05(self):
    '''
    Verifica os numeros reais
    '''
    self.__lexema +=self.__caracter
    self.__avanca_caracter()
    if self.__caracter.isdigit():
      while re.match(r"([0-9])" ,str(self.__caracter)):
        self.__lexema += self.__caracter
        self.__avanca_caracter()
      self.__cod_lexema = "NRO"
    else: 
      
      while  self.__caracter.isspace()!=True and self.__caracter != '\t' and self.__caracter != '\n':
        self.__lexema += self.__caracter
        self.__avanca_caracter()
      self.__cod_lexema = "NMF"
      self.__incidencia_de_erro +=1
    self.__adiciona_token() 
    self.__q0()

  def __q06(self):
    '''
    Recebe e define o operador aritmético de multiplicação
    definido por *
    '''
    self.__lexema += self.__caracter
    self.__cod_lexema = "ART"
    self.__adiciona_token()
    self.__avanca_caracter()
    self.__q0()

  def __q07(self):
    '''
    Recebe e define o operador aritmético de adição.\n
    definido por +\n
    E distibui em caso de operador de incremento
    ''' 
    self.__lexema += self.__caracter
    self.__avanca_caracter()
    self.__cod_lexema = "ART"
    if self.__caracter == "+":
      self.__q08()
    else:
      self.__adiciona_token()
      self.__q0()

  def __q08(self): 
    '''
    Recebe e define o operador aritmético de incremento e decremento
    '''
    self.__lexema += self.__caracter
    self.__avanca_caracter()
    self.__adiciona_token()
    self.__q0()
  
  def __q09(self):
    '''
    Recebe e define o operador aritmético de Subtração.\n
    definido por +\n
    E distibui em caso de operador de decremento
    ''' 
    self.__lexema += self.__caracter
    self.__avanca_caracter()
    self.__cod_lexema = "ART"
    if self.__caracter == "-":
      self.__q08()
    else:
      self.__adiciona_token()
      self.__q0()

  def __q11(self):
    '''
    Recebe e define o perado aritmético de divisão. Ou verifica se o mesmo forma um comentario de bloco ou linha\n
    Caso isso aconteça distribui para a geração de comentario
    
    '''
    self.__lexema += self.__caracter
    self.__avanca_caracter()
    if self.__caracter == '/':
      self.__lexema == ' '
    elif self.__caracter == "*":
      self.__lexema += self.__caracter
      self.__avanca_caracter()
      self.__linha_comentario = self.__n_linhas   
      self.__q14()  
    else:
      self.__cod_lexema = "ART"
      self.__adiciona_token()
      self.__q0()

  def __q12(self):
    '''
    Recebe e define um comentário de linha identificado por //\n
    Ignora toda a linha
    '''
    self.__lexema = ''

  def __q14(self):
    '''
    Recebe e verifica a construção  do comentário de bloco e caso seja bem formado e executa seu fechamento
    '''
    ## verifica Comentario bloco 
    while  self.__caracter != "*":
      if self.__caracter == '\n':
        self.__comentario_aberto = True
        break          
      else: 
        self.__lexema += self.__caracter  
        self.__avanca_caracter()    
    if self.__caracter == "*":
        self.__avanca_caracter()
        if self.__caracter == '/':
          self.__lexema = ''
          self.__comentario_aberto = False
          self.__avanca_caracter()  
          self.__q0()
        else:
          self.__q14()        

  
  def __q19(self):
    '''
    Recebe e identifica a contrução do operado lógico de "ou" definido por ||\n
    Caso seja bem formado indexa o mesmo, 
    caso não seja lança o erro de operador mal formado
    '''
    self.__lexema += self.__caracter
    self.__avanca_caracter()
    if(self.__caracter == "|"):
      self.__lexema += self.__caracter
      self.__avanca_caracter()
      self.__cod_lexema = "LOG"
    else:
      self.__cod_lexema = "OpMF"
      self.__incidencia_de_erro +=1
    self.__adiciona_token()
    self.__q0()
   
  def __q21(self):
    '''
    Recebe e identifica a contrução do operado lógico de "e" definido por &&\n
    Caso seja bem formado indexa o mesmo, 
    caso não seja lança o erro de operador mal formado
    '''
    self.__lexema += self.__caracter
    self.__avanca_caracter()
    if(self.__caracter == '&'):
      self.__lexema += self.__caracter
      self.__avanca_caracter()
      self.__cod_lexema = "LOG"
    else:
      self.__cod_lexema = "OpMF"
      self.__incidencia_de_erro +=1
    self.__adiciona_token()
    self.__q0()   
    
  def __q23(self): 
    '''
    Recebe e define todos os operadores relacionais\n
    E operador mal formado no caso de  "!" que não seja seguido por "="
    '''
    self.__lexema += self.__caracter   
    if self.__caracter == '!':
      self.__avanca_caracter()
      if self.__caracter == '=':
        self.__cod_lexema = "REl"
        self.__lexema += self.__caracter
        self.__avanca_caracter()
      else:
        self.__cod_lexema = "LOG"
      self.__adiciona_token()
      self.__q0()
  
    else:  
      self.__avanca_caracter()
      self.__cod_lexema = "REL"
      if self.__caracter == "=":
        self.__lexema += self.__caracter
        self.__avanca_caracter()
      self.__adiciona_token()
      self.__q0()


  def __q32(self):
    '''
    Recebe e estabelece um cadeia de caracteres\n
    Em cado de cadeia mal formada distribui a definição do erro
    '''
    sib_invalido = False
    self.__lexema += self.__caracter
    self.__avanca_caracter()
    while self.__caracter != '\n' and self.__caracter != '\"':
      if ord(self.__caracter)<32 or ord(self.__caracter)>126:
        sib_invalido = True 
      elif self.__caracter == '\\':
        self.__lexema += self.__caracter
        self.__avanca_caracter()
        if self.__caracter == '"' : #após \
          self.__lexema += '"'
          self.__avanca_caracter()
      self.__lexema += self.__caracter  
      self.__avanca_caracter()  
    if self.__caracter == '"' : 
      self.__lexema += self.__caracter
      if sib_invalido == False:
        self.__cod_lexema = "CAD"
      else:
        self.__cod_lexema = "CMF"
        self.__incidencia_de_erro +=1
      self.__adiciona_token()
      self.__avanca_caracter()
    else:
      if re.match('["]' ,self.__lexema):
        self.__cod_lexema = "CMF"
        self.__incidencia_de_erro +=1
        self.__adiciona_token()
      else:
        self.__lexema = ''
    self.__q0()  

  def __q31(self):
    '''
    Identifica uma " dentro de uma cadeia de carácter , que não é um delimitador de cadeia de carácter.
    '''  
    self.__lexema += self.__caracter
    self.__avanca_caracter()
    if self.__caracter == '"' : #após \
      self.__lexema += '"'
      self.__avanca_caracter()
    else:
      self.__lexema += self.__caracter()
    self.__q32()
  
  def __q40(self):
    '''
    Recebe um simbolo inválido e lança seu erro a tabela de símbolos
    '''
    self.__incidencia_de_erro +=1
    self.__cod_lexema = "SIB"
    self.__adiciona_token()
    self.__q0()

