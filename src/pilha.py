     # -*- coding: utf-8 -*- 

import sys

class EstPilha:
    
    def __init__(self):
        self.pilha = [] #pilha de tipos 
    
    def push(self, tipo):
        '''
        Colocar um novo tipo na pilha
        '''
        self.pilha.append(tipo)
    
    def pop(self):
        '''
        Remover o tipo no topo da pilha
        '''
        self.pilha.pop(-1)
    
    def topo(self):
        '''
        Retorna o topo da pilha
        '''
        return self.pilha[-1]
