from cCategoria import Categoria

class Produto:
    def __init__(self, nome=None, preco=0.0, categoria=Categoria(), id=None ):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

    def imprimir(self):
        pass


