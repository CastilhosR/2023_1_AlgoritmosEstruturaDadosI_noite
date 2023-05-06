from abc import ABC, abstractmethod
class Veiculo(ABC):
    def __init__(self, fabricante = None, modelo = None, ano = None):
        self.fabricante = fabricante
        self.modelo = modelo
        self.ano = ano

    def imprimir(self):
        print("Fabricante: ", self.fabricante)
        print("Modelo: ", self.modelo)
        print("Ano: ", self.ano)

    @abstractmethod
    def imprimirEspecifico(self):
        pass

class Carro(Veiculo):
    def __init__(self, fabricante = None, modelo = None, ano = None, qtdPortas = None):
        super().__init__(fabricante, modelo, ano)
        self.qtdPortas = qtdPortas

    def imprimirEspecifico(self):
        super().imprimir()
        print("Qtd. Portas: ", self.qtdPortas)

class Moto(Veiculo):
    def __init__(self, fabricante = None, modelo = None, ano = None, cilindradas = None):
        super().__init__(fabricante, modelo, ano)
        self.cilindradas = cilindradas

    def imprimirEspecifico(self):
        super().imprimir()
        print("Cilindradas: ", self.cilindradas)

