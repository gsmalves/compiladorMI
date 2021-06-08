

class Simbolo:
    def __init__(self, simbolo, tipo, valor, categoria: int):#ANCHOR adicionar parametro para fuinções
        self.simbolo =simbolo
        self.tipo = tipo
        self.valor = valor
        self.cat = {
            '1': "function",
            '2': "var",
            '3': "procedure",
            '4': "struct",
            '5': "const"
        }   
        self.categoria = self.cat[str(categoria)]

     
    def __str__(self):
        return str("{} {} {} {} ".format(self.simbolo, self.tipo, self.valor, self.categoria))

if __name__ == '__main__':
    meme = Simbolo("meme", "int", None,1)
    print(meme)  