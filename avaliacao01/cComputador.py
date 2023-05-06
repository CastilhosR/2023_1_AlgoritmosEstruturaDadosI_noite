from abc import ABC, abstractmethod
class computador(ABC):
    def __init__(self, modelo = "", cor = "", preco = 0):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco

    def getInformacoes(self):
        texto  = f"\tModelo: {self.modelo}\n"
        texto += f"\tCor: {self.cor}\n"
        texto += f"\tPreço: {str(self.preco)}\n"
        return texto

    @abstractmethod
    def cadastrar(self):
        pass

class Desktop(computador):
    def __init__(self, modelo = "", cor = "", preco = 0, potenciaDaFonte = 0):
        super().__init__(modelo, cor, preco)
        self._potenciaDaFonte = 0
    def getInformacoes(self):
        texto  = "Desktop:\n"
        texto += super().getInformacoes()
        texto += f"\tPotencia da fonte: {self._potenciaDaFonte} w\n"
        return texto

    def cadastrar(self, modelo = "", cor = "", preco = 0, potenciaDaFonte = 0):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        self._potenciaDaFonte = potenciaDaFonte

class Notebook (computador):
    def __init__(self, modelo = "", cor = "", preco = 0, tempoDeBateria = 0):
        super().__init__(modelo, cor, preco)
        self.__tempoDeBateria = 0
    def getInformacoes(self):
        texto  = "Notebook:\n"
        texto += super().getInformacoes()
        texto += f"\tTempo de bateria: {str(self.__tempoDeBateria)} h\n"
        return texto

    def cadastrar(self, modelo = "", cor = "", preco = 0, tempoDeBateria = 0):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        self.__tempoDeBateria = tempoDeBateria
