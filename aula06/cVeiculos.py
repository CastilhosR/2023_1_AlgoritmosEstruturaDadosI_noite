class veiculo():
    def __init__(self, marca = None, qtdRodas = None, modelo = None, velocidade = 0):
        self.marca = marca
        self.qtdRodas = qtdRodas
        self.modelo = modelo
        self.velocidade = velocidade

    def imprimirinfo(self):
        print("Marca: ", self.marca)
        print("Rodas: ", self.qtdRodas)
        print("Modelo: ", self.modelo)
        print("Velocidade atual: ", self.velocidade)

    def acelerar(self, valor = 0):
        self.velocidade += valor

    def frear(self, valor = 0):
        self.velocidade -= valor if self.velocidade > 0 else 0


class bicicleta(veiculo):
    def __init__(self, marca = None, modelo = None, numMarchas = 1, bagageiro = False,  qtdRodas = 2, velocidade = 30):
        super().__init__(marca=marca, qtdRodas=qtdRodas, modelo=modelo, velocidade=velocidade)
        self.numMarchas = numMarchas
        self.bagageiro = bagageiro
    def imprimirinfo(self):
        super().imprimirinfo()
        print("Marchas: ", self.numMarchas)
        print("Bagageiro: ", "Sim" if self.bagageiro else "Não" )
        print("\n--------------------------------------------------\n")

class automotor(veiculo):
    def __init__(self, potenciaDoMotor = 0.0, marca = None, qtdRodas = 0, modelo = None, velocidade = 0):
        super().__init__(marca=marca, qtdRodas=qtdRodas, modelo=modelo, velocidade=velocidade)
        self.potenciaDoMotor = potenciaDoMotor

    def imprimirinfo(self):
        super().imprimirinfo()
        print("Potencia motor: ", self.potenciaDoMotor)


class carro(automotor):
    def __init__(self, marca = None, modelo = None, qtdPortas = 2, qtdRodas = 4, velocidade = 180):
        super().__init__(marca=marca, qtdRodas=qtdRodas, modelo=modelo, velocidade=velocidade)
        self.qtdPortas = qtdPortas

    def imprimirinfo(self):
        super().imprimirinfo()
        print("Portas: ", self.qtdPortas)
        print("\n--------------------------------------------------\n")

class moto(automotor):
    def __init__(self, marca = None, modelo = None, qtdRodas = 2, partidaEletrica = False, velocidade = 180 ):
        super().__init__(marca = marca, qtdRodas = qtdRodas, modelo = modelo, velocidade = velocidade)
        self.partidaEletrica = partidaEletrica

    def imprimirinfo(self):
        super().imprimirinfo()
        print("Partida Eletrica: ", "Sim" if self.partidaEletrica else "Não")
        print("\n--------------------------------------------------\n")

