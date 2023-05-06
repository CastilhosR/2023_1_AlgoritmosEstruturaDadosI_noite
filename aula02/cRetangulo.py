
class AreaRetangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcularArea(self):
        return self.largura * self.altura

    def imprimir(self):
        print("Largura: ", self.largura)
        print("Altura:", self.altura)
        print("Área: ", self.calcularArea())

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass

