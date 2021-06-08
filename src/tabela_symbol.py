# -*- coding: UTF-8 -*-

from token_lex import Token
from simbolo import Simbolo

class TabelaSymbolos:
    def __init__(self, token: Token, tipo: String):
        self.__token = token
        self.__tipo = tipo
        self.tabela = []    
    def insert(self, token: Token):

    def add_symbol(self, simbolo, tipo):
        '''
        Coloca um novo símbolo na tabela de símbolo
        '''
        if not self.simbolo_no_escopo(simbolo): #se o símbolo nãp existe no escopo
            self.tabela.append(Simbolo(simbolo, tipo))   #adiciona o novo símbolo
            #print(self.tabela)
        else:
            sys.exit("Indentificador '" + simbolo + "' já no escopo!")  #se já existir o símbolo no escopo

    def simbolo_no_escopo(self, simbolo_atual: Simbolo):
        for i in self.tabela:
            if self.tabela[i].simbolo == simbolo:
                return True

    def busca_simbolo(self, simbolo):


