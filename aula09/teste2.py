class no:
    def __init__(self, valor):
        self.dado = valor
        self.anterior = None
        self.proximo = None

class lista_dupla_encadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def add_nodo(self, valor):

        nodo = no(valor)

        if self.inicio is None:
            self.inicio = nodo
            self.fim = nodo

        elif valor < self.inicio.dado:
            nodo.proximo = self.inicio
            self.inicio.anterior = nodo
            self.inicio = nodo

        else:
            aux = self.inicio

            while aux.proximo and valor > aux.proximo.dado:
                aux = aux.proximo

            nodo.proximo = aux.proximo

            if aux.proximo:
                aux.proximo.anterior = nodo
            else:
                self.fim = nodo

            aux.proximo = nodo
            nodo.anterior = aux

        self.tamanho += 1

    def imprimir_do_inicio(self):
        if self.inicio is None:
            print("Lista Vazia !!!")
        else:
            aux = self.inicio
            while aux:
                print(aux.dado, end="\t")
                aux = aux.proximo
            print()

    def imprimir_do_fim(self):
        if self.fim is None:
            print("Lista Vazia !!!")
        else:
            aux = self.fim
            while aux:
                print(aux.dado, end="\t")
                aux = aux.anterior
            print()


valores = [48,46,23,50,47,29,35,90,41,1]

lista = lista_dupla_encadeada()




for x in valores:
    lista.add_nodo(x)
    print(x, end="\t")

print()
print("Inicio da  Lista -> ", lista.inicio.dado)
print("Fim da  Lista -> ", lista.fim.dado)

print("do inicio")

lista.imprimir_do_inicio()

print("\ndo fim")

lista.imprimir_do_fim()

