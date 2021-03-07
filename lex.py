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
        if os.path.exists(arquivo_fonte):
            self.__arquivo_fonte = open(arquivo_fonte, 'r')
        else:
            print("Erro: Arquivo não existe.")
            exit()
    def __identificaSimbolo(self):
    # Strings com os simbolos da tabela ASCII (32 a 126)
        simbolos = ''' !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHJKLMNOPQRSTUVXWYZ[\]^_`abcdefghijklmnopqrstuvxwyz{|}~'''
        if self.__caracter in simbolos:
            return True
        return False

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
            self.__q03()
        elif  self.__caracter.islower():
            self.__q1()
        elif  self.__caracter == '/':
            self.__q05()
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

   
    def __q03(self):## verifica se é numeral
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
            self.__q04()  
        else:
            print("Erro léxico ({0}, {1}): Caracter {2} inesperado".format(self.__nlinhas, self.__cabeca,
                                                                        self.__caracter))   

    def __q04(self):## verifica se é numeral depois do ponto
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
    def __q05(self):
        self.__caracter = self.__getCaracter()
        if self.__caracter == "/":
            self.__q06()


#depois mudar a numeração quando fazer dos outros operadores pra ficar organizado            
    def __q06(self):#comentario de linha
       self.__caracter = self.__finalLinha
       self.__q0
            
def main():
    __arquivo = "fonte.txt"
    __automato = Lexico(arquivo_fonte=__arquivo)
    __tabelasimbolos = __automato.getTabelaSimbolos()
    for i in range(len(__tabelasimbolos)):
        print(__tabelasimbolos[i])

if __name__ == '__main__':
    main()
