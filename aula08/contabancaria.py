from abc import ABC, abstractmethod

class contabancaria(ABC):
    def __init__(self, numero, id_pessoa, saldoTotal = 0):
        self.numero = numero
        self.id_pessoa = id_pessoa
        self.saldoTotal = saldoTotal
        pass

    @abstractmethod
    def cadastrar(self):
        pass

    @abstractmethod
    def depositar(self):
        pass

class contacorrente(contabancaria):
    def __init__(self, numero, id_pessoa):
        super().__init__(numero, id_pessoa)
        self.saldoCC = 0.0

    def depositar(self, valor = 0):
        self.saldoCC += valor

    def cadastrar(self):
        self.saldoTotal += self.saldoCC

class contapoupanca(contabancaria):
    def __init__(self, numero, id_pessoa):
        super().__init__(numero, id_pessoa)
        self.saldoCP = 0.0

    def depositar(self, valor = 0):
        self.saldoCP += valor

    def cadastrar(self):
        self.saldoTotal += self.saldoCP
