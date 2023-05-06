from cCidade import Cidade

class Pessoa:
    def __init__(self, nome="Fulano", fone="xxx", city=Cidade(), id=None ):
        self.id = id
        self.nome = nome
        self.fone = fone
        self.city = city

    def imprimir(self):
        print("Nome: ", self.nome)
        print("Fone: ", self.fone)
        print("Cidade: ", self.city.nome, "/", self.city.uf)