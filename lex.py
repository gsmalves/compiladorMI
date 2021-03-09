# -*- coding: UTF-8 -*-
import os
import re

class Lexico:
    def __init__(self, arquivo_fonte):
        self.__cabeca = 0
        self.__fita = []
        self.__nlinhas = 0
        self.__tabelaSimbolos = []
        self.__lexema = ''
        self.__finalLinha = '\n'
        self.__simbolos = ''' !#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHJKLMNOPQRSTUVXWYZ[\]^_`abcdefghijklmnopqrstuvxwyz{|}~'''
        
        if os.path.exists(arquivo_fonte):
            self.__arquivo_fonte = open(arquivo_fonte, 'r')
        else:
            print("Erro: Arquivo não existe.")
            exit()
    ##Verifica se o simbolo está no escopo definido
    def __identificaSimbolo(self):
    # Strings com os simbolos da tabela ASCII (32 a 126, exceto 34)
        if self.__caracter in self.__simbolos:
            return True
        return False
    ##Verifica se um lexema está contido no conjunto de palavras reservadas
 #   def __identificaPalavraReservada(self):
 #     self.__palavrasReservadas = ["var", "const", "typedef", "struct", "extends", "procedure","function", "start", "return", "if", "else", "then", "while", "read","print",
 #          "int",   "real",   "boolean",   "string",   "true",   "false","global", "local"]
 #       for i in self.__palavrasReservadas:           
 #           if str(self.__fita) in str(self.__palavrasReservadas[i]):
 #               return True
 #          return False       
  
    def __avancaCabeca(self):
        self.__cabeca += 1

    def __posicaoCabeca(self):
        return self.__cabeca

    def __atualiza_nLinhas(self):
        self.__nlinhas += 1

    def __getCaracter(self):
        if self.__cabeca < len(self.__fita):
            self.__letra = self.__fita[self.__cabeca]
            self.__avancaCabeca()
            if self.__letra != self.__finalLinha or not self.__letra.isspace():
                self.__lexema += self.__letra
            return self.__letra
        else:
            return '\n'

    def getTabelaSimbolos(self):
        for self.__linha in self.__arquivo_fonte:
            self.__fita = list(self.__linha)
            self.__q0()
            self.__atualiza_nLinhas()
            self.__cabeca = 0
        self.__arquivo_fonte.close()
        return self.__tabelaSimbolos

    def __q0(self):
        self.__caracter = self.__getCaracter()
        if self.__caracter.isdigit():
            self.__q04()
        elif  self.__caracter.islower():
            self.__q1()
        elif  self.__caracter == '/':
            self.__q11()
        elif self.__caracter == '*':
            self.__q06()    
        elif self.__caracter == '+':
            self.__q07()    
        elif self.__caracter == '-':
            self.__q09()    
        elif self.__finalLinha == self.__caracter:
            #print(self.__caracter)
            pass
        elif self.__caracter.isspace():
            self.__lexema = ''
            self.__q0()
        else:
            print("Erro léxico ({0}, {1}): Caracter {2} inesperado".format(self.__nlinhas, self.__cabeca,
                                                                           self.__caracter))

            exit()

    def __q1(self):
        
        self.__caracter = self.__getCaracter() 

        while self.__caracter.isdigit() or self.__caracter.islower() or self.__caracter == '_':
            self.__caracter = self.__getCaracter()
        if self.__finalLinha == self.__caracter:  # final da linha
            #if self.__identificaPalavraReservada():
            #    self.__tabelaSimbolos.append([self.__nlinhas, self.__cabeca, 'PRE -', self.__lexema])
            #    self.__lexema = '' 
            #else:   
            self.__tabelaSimbolos.append([self.__nlinhas, self.__cabeca, 'IDE -', self.__lexema])
            self.__lexema = ''
        elif self.__caracter.isspace():
            self.__lexema = self.__lexema[:len(self.__lexema) - 1]
            self.__tabelaSimbolos.append([self.__nlinhas, self.__cabeca, 'IDE -', self.__lexema])
            self.__lexema = ''
            self.__q0()
        else:
            print("Erro léxico ({0}, {1}): Caracter {2} inesperado".format(self.__nlinhas, self.__cabeca,
                                                                           self.__caracter))
            pass

   
    def __q04(self):## verifica se é numeral
        self.__caracter = self.__getCaracter()
        while self.__caracter.isdigit():
            self.__caracter = self.__getCaracter()
        if self.__finalLinha == self.__caracter:  # final da linha
            self.__tabelaSimbolos.append([self.__nlinhas, self.__cabeca, "NRO -", self.__lexema])
            self.__lexema = ''
        elif self.__caracter.isspace():
            self.__lexema = self.__lexema[:len(self.__lexema) - 1]
            self.__tabelaSimbolos.append([self.__nlinhas, self.__cabeca, "NRO -", self.__lexema])
            self.__lexema = ''
            self.__q0()
        elif self.__caracter == ".":
            self.__q05()  
        else:
            print("Erro léxico ({0}, {1}): Caracter {2} inesperado".format(self.__nlinhas, self.__cabeca,
                                                                        self.__caracter))   

    def __q05(self):## verifica se é numeral depois do ponto
        self.__caracter = self.__getCaracter()
        while self.__caracter.isdigit():

            self.__caracter = self.__getCaracter()
        
        if self.__finalLinha == self.__caracter:  # final da linha
            self.__tabelaSimbolos.append([self.__nlinhas, self.__cabeca, "NRO -", self.__lexema])
            self.__lexema = ''
        elif self.__caracter.isspace():
            self.__lexema = self.__lexema[:len(self.__lexema) - 1]
            self.__tabelaSimbolos.append([self.__nlinhas, self.__cabeca, "NRO -", self.__lexema])
            self.__lexema = ''
            self.__q0()
        else:
            print("Erro léxico ({0}, {1}): Caracter {2} inesperado".format(self.__nlinhas, self.__cabeca,
                                                                        self.__caracter))   #corrigir definição do erro
   
   
   ###identifica operadores aritmeticos
    def __q06(self):
        self.__caracter = self.__getCaracter()
        if self.__finalLinha == self.__caracter:  # final da linha
            #self.__tabelaSimbolos.append([self.__nlinhas, self.__cabeca, 'ART -', self.__lexema])
            self.__tabelaSimbolos.append("[{1}{2}{3}{4}]".format(self.__nlinhas, self.__cabeca, 'ART -', self.__lexema))
            self.__lexema = ''
        elif self.__caracter.isspace():
            self.__lexema = self.__lexema[:len(self.__lexema) - 1]
            self.__tabelaSimbolos.append([self.__nlinhas, self.__cabeca, 'ART -', self.__lexema])
            self.__lexema = ''
            self.__q0()
        else:
            #Corrigir a definição do erro || ou é erro lexico
            print("Erro léxico ({0}, {1}): Caracter {2} inesperado".format(self.__nlinhas, self.__cabeca,
                                                                 self.__caracter))
    
    def __q07(self):# Operador Aritmetico de Adição
        self.__caracter = self.__getCaracter()
        if self.__caracter == "+":
            self.__q08()
        elif self.__finalLinha == self.__caracter:  # final da linha
            #self.__tabelaSimbolos.append([self.__nlinhas, self.__cabeca, 'ART -', self.__lexema])
            self.__tabelaSimbolos.append("[{1}{2}{3}{4}]".format(self.__nlinhas, self.__cabeca, 'ART -', self.__lexema))
            self.__lexema = ''
        elif self.__caracter.isspace():
            self.__lexema = self.__lexema[:len(self.__lexema) - 1]
            self.__tabelaSimbolos.append([self.__nlinhas, self.__cabeca, 'ART -', self.__lexema])
            self.__lexema = ''
            self.__q0()
        else:
            #Corrigir a definição do erro || ou é erro lexico
            print("Erro léxico ({0}, {1}): Caracter {2} inesperado".format(self.__nlinhas, self.__cabeca,
                                                                 self.__caracter))
    
    def __q08(self):
        self.__caracter = self.__getCaracter()
        if self.__finalLinha == self.__caracter:  # final da linha
            self.__tabelaSimbolos.append([self.__nlinhas, self.__cabeca, 'ART -', self.__lexema])
            #self.__tabelaSimbolos.append("[{1}{2}{3}{4}]".format(self.__nlinhas, self.__cabeca, 'ART -', self.__lexema))
            self.__lexema = ''
        elif self.__caracter.isspace():
            self.__lexema = self.__lexema[:len(self.__lexema) - 1]
            self.__tabelaSimbolos.append([self.__nlinhas, self.__cabeca, 'ART -', self.__lexema])
            self.__lexema = ''
            self.__q0()
        else:
            #Corrigir a definição do erro || ou é erro lexico
            print("Erro léxico ({0}, {1}): Caracter {2} inesperado".format(self.__nlinhas, self.__cabeca,
                                                                 self.__caracter))
    def __q09(self):# Operador Aritmetico de Adição
        self.__caracter = self.__getCaracter()
        if self.__caracter == "-":
            self.__q08()
        elif self.__finalLinha == self.__caracter:  # final da linha
            #self.__tabelaSimbolos.append([self.__nlinhas, self.__cabeca, 'ART -', self.__lexema])
            self.__tabelaSimbolos.append("[{1}{2}{3}{4}]".format(self.__nlinhas, self.__cabeca, 'ART -', self.__lexema))
            self.__lexema = ''
        elif self.__caracter.isspace():
            self.__lexema = self.__lexema[:len(self.__lexema) - 1]
            self.__tabelaSimbolos.append([self.__nlinhas, self.__cabeca, 'ART -', self.__lexema])
            self.__lexema = ''
            self.__q0()
        else:
            #Corrigir a definição do erro || ou é erro lexico
            print("Erro léxico ({0}, {1}): Caracter {2} inesperado".format(self.__nlinhas, self.__cabeca,
                                                                 self.__caracter))
    
    def __q10(self):
        self.__caracter = self.__getCaracter()
        if self.__finalLinha == self.__caracter:  # final da linha
            self.__tabelaSimbolos.append([self.__nlinhas, self.__cabeca, 'ART -', self.__lexema])
            #self.__tabelaSimbolos.append("[{1}{2}{3}{4}]".format(self.__nlinhas, self.__cabeca, 'ART -', self.__lexema))
            self.__lexema = ''
        elif self.__caracter.isspace():
            self.__lexema = self.__lexema[:len(self.__lexema) - 1]
            self.__tabelaSimbolos.append([self.__nlinhas, self.__cabeca, 'ART -', self.__lexema])
            self.__lexema = ''
            self.__q0()
        else:
            #Corrigir a definição do erro || ou é erro lexico
            print("Erro léxico ({0}, {1}): Caracter {2} inesperado".format(self.__nlinhas, self.__cabeca,
                                                                 self.__caracter))
    
  


    def __q11(self):#Identifica se é o operador aritmetico "/" ou se é um indicador de comentario
        self.__caracter = self.__getCaracter()
        if self.__caracter == "/":
            self.__q12()
        elif self.__caracter == "*":
            self.__q14()  
        elif self.__finalLinha == self.__caracter:  # final da linha
            #self.__tabelaSimbolos.append([self.__nlinhas, self.__cabeca, 'ART -', self.__lexema])
            self.__tabelaSimbolos.append("[{1}{2}{3}{4}]".format(self.__nlinhas, self.__cabeca, 'ART -', self.__lexema))
            self.__lexema = ''
        elif self.__caracter.isspace():
            self.__lexema = self.__lexema[:len(self.__lexema) - 1]
            self.__tabelaSimbolos.append([self.__nlinhas, self.__cabeca, 'ART -', self.__lexema])
            self.__lexema = ''
            self.__q0()
        else:
            #Corrigir a definição do erro || ou é erro lexico
            print("Erro léxico ({0}, {1}): Caracter {2} inesperado".format(self.__nlinhas, self.__cabeca,
                                                                           self.__caracter))

   
    def __q12(self):#comentario de linha
       self.__lexema = ''
       self.__caracter = self.__finalLinha
       self.__q0
    
    

    def __q14(self):## verifica CoMF
        self.__caracter = self.__getCaracter()
        while  self.__caracter.isdigit() or self.__caracter.islower() or self.__caracter.isspace():
            self.__caracter = self.__getCaracter()
        if self.__caracter == "*":
            self.__q15()  
        
    
    def __q15(self):## verifica comentário
        self.__caracter = self.__getCaracter() 
        while  self.__caracter.isdigit() or self.__caracter.islower() or self.__caracter.isspace() or self.__caracter == "*" :
            self.__caracter = self.__getCaracter()
        if self.__caracter == "/":
            self.__q16()  
        
             
    def __q16(self):#comentario de bloco
        print("fechei bloco")
        self.__lexema = ''
        self.__caracter = self.__finalLinha
        self.__q0
        
        