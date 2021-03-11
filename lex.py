# -*- coding: UTF-8 -*-
import os
import re

class Lexico:
    def __init__(self, arquivo_fonte):
        self.__cabeca = 0
        self.__fita = []
        self.__array = []
        self.__nlinhas = 0
        self.__tabelaSimbolos = []
        self.__lexema = ''
        self.__finalLinha = '\n'
        self.__simbolos = ['!','#','$','%','&','(',')','*','+',',','-','.','/','0','1','2','3','4','5','6','7','8','9',':',';','<','=','>','?','@','A','B','C','D','E','F','G','H','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','W','Y','Z','[',']','^','_','`','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','w','y','z','{','|','}','~']
        
        
        if os.path.exists(arquivo_fonte):
            self.__arquivo_fonte = open(arquivo_fonte, 'r')
           
        else:
            print("Erro: Arquivo não existe.")
            exit()
    ##Verifica se o simbolo está no escopo definido
    #Gustavo
    def __veriSimbol(self):
        if (ord(self.__caracter) >= 32 and ord(self.__caracter) <= 126) and ord(self.__caracter) != 34 :
            return True
        return False
  
  
    def __identificaSimbolo(self):
    # Strings com os simbolos da tabela ASCII (32 a 126)
        
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
            return self.__finalLinha

    def getTabelaSimbolos(self):
        for self.__linha in self.__arquivo_fonte:
            self.__fita = list(self.__linha)
            #print (self.__fita)
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
        elif self.__caracter == '"':
            self.__q30()    
        elif self.__finalLinha == self.__caracter:
            #print(self.__caracter)
            pass
        elif self.__caracter.isspace():
            self.__lexema = ''
            self.__q0()
        elif self.__caracter == "&":
            self.__q21()
        elif self.__caracter == "|":
            self.__q19()
        elif self.__caracter == "!":
            self.__q18()
        elif self.__caracter == "=":
            self.__q23()
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

   #operadores logicos 
    
    
    #Operador Lógico "e" // verifica se não existe um erro lexico
    #caso não exista o erro lança pra o estado q22 que adiciona o lexena de && 
    def __q21(self):
        self.__caracter = self.__getCaracter()
        if(self.__caracter == "&"):
           self.__q22()
        else:
        #Corrigir a definição do erro || ou é erro lexico
            print("Erro léxico ({0}, {1}): Caracter {2} inesperado".format(self.__nlinhas, self.__cabeca,
                                                                        self.__caracter))


    def __q22(self):#Lança o lexema de operador logico "e"
        self.__tabelaSimbolos.append([self.__nlinhas, self.__cabeca, 'LOG -', self.__lexema])
        #self.__tabelaSimbolos.append("[{1}{2}{3}{4}]".format(self.__nlinhas, self.__cabeca, 'ART -', self.__lexema))
        self.__lexema = ''
        self.__q0()


    #Operador Lógico "ou" // verifica se não existe um erro lexico
    #caso não exista o erro lança pra o estado q20 que adiciona o lexena de || 
    def __q19(self):
        self.__caracter = self.__getCaracter()
        if(self.__caracter == "|"):
           self.__q20()     
        else:
        #Corrigir a definição do erro || ou é erro lexico
            print("Erro léxico ({0}, {1}): Caracter {2} inesperado".format(self.__nlinhas, self.__cabeca,
                                                                        self.__caracter))


    def __q20(self):#Lança o lexema de operador logico "ou"
        self.__tabelaSimbolos.append([self.__nlinhas, self.__cabeca, 'LOG -', self.__lexema])
        #self.__tabelaSimbolos.append("[{1}{2}{3}{4}]".format(self.__nlinhas, self.__cabeca, 'ART -', self.__lexema))
        self.__lexema = ''
        self.__q0()

    #Operadores Relacionais

    #Operador Relacionais "diferente de" // verifica se não existe um erro lexico
    #caso não exista o erro lança pra o estado q25 que adiciona o lexena de || 
    def __q18(self):
        self.__caracter = self.__getCaracter()
        if(self.__caracter == "="):
           self.__q25()
        else:
        #Corrigir a definição do erro || ou é erro lexico
            print("Erro léxico ({0}, {1}): Caracter {2} inesperado".format(self.__nlinhas, self.__cabeca,
                                                                        self.__caracter))


    def __q25(self):#Lança o lexema de operador relacional diferente de "!="
        self.__tabelaSimbolos.append([self.__nlinhas, self.__cabeca, 'LOG -', self.__lexema])
        #self.__tabelaSimbolos.append("[{1}{2}{3}{4}]".format(self.__nlinhas, self.__cabeca, 'ART -', self.__lexema))
        self.__lexema = ''
        self.__q0()

    #Operador Relacionais "atribuição" 
    def __q23(self):
        self.__caracter = self.__getCaracter()
        if self.__caracter == "=":
            self.__q24()
        elif self.__finalLinha == self.__caracter:  # final da linha
            #self.__tabelaSimbolos.append([self.__nlinhas, self.__cabeca, 'ART -', self.__lexema])
            self.__tabelaSimbolos.append("[{1}{2}{3}{4}]".format(self.__nlinhas, self.__cabeca, 'REL -', self.__lexema))
            self.__lexema = ''
        elif self.__caracter.isspace():
            self.__lexema = self.__lexema[:len(self.__lexema) - 1]
            self.__tabelaSimbolos.append([self.__nlinhas, self.__cabeca, 'REL -', self.__lexema])
            self.__lexema = ''
            self.__q0()


    def __q24(self):
        self.__tabelaSimbolos.append([self.__nlinhas, self.__cabeca, 'REL -', self.__lexema])
        #self.__tabelaSimbolos.append("[{1}{2}{3}{4}]".format(self.__nlinhas, self.__cabeca, 'ART -', self.__lexema))
        self.__lexema = ''
        self.__q0()





    def __q12(self):#comentario de linha
       self.__lexema = ''
       self.__caracter = self.__finalLinha
       self.__q0()
    
    

    def __q14(self):## verifica Comentario bloco
        self.__caracter = self.__getCaracter()
        # botar mais caracteres aqui pra o while, só não pode o "*"
        while  self.__caracter != "*":
            self.__caracter = self.__getCaracter()
                
        if self.__caracter == "*":
            self.__q15()  
        
    
    def __q15(self):## verifica comentário bloco
        self.__caracter = self.__getCaracter() 
        # botar mais caracteres aqui pra o while, só não pode o "/"
        if self.__caracter != "/":
            self.__q14()
            
        else:
            self.__q16()  
        
             
    def __q16(self):#comentario de bloco
        print("fechei bloco")
        self.__tabelaSimbolos.append([self.__nlinhas, self.__cabeca, 'Coments', self.__lexema])
        self.__lexema = ''
        self.__caracter = self.__finalLinha
        self.__q0
        
    def __q30(self):# cadeia de caracter    
        self.__caracter = self.__getCaracter()
        
        if self.__caracter == '"' :
            self.__q34()
        
        elif (re.match('[\x20-\x21]|[\x23-\x7e]',self.__caracter)):
            self.__q32()
        else:
            print("erro aqui")
            pass
    def __q32(self):
        
        self.__caracter = self.__getCaracter() 

        while (re.match('[\x20-\x21]|[\x23-\x7e]',self.__caracter)):
            self.__caracter = self.__getCaracter()
        if self.__caracter == '"':
            self.__q34()
        else:
            print("Erro léxico ({0}, {1}): Caracter {2} inesperado".format(self.__nlinhas, self.__cabeca,
                                                                           self.__caracter))
            pass

    def __q34(self):

        self.__tabelaSimbolos.append([self.__nlinhas, self.__cabeca, 'CAD', self.__lexema])
       