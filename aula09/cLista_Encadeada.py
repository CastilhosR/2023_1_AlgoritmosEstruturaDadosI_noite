class no:

    def __init__(self, valor):
        self.dado = valor
        self.proximo = None

class lista_encadeada:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def add_nodo_inicio(self, valor):
        nodo = no(valor)
        if self.inicio == None:
            self.inicio = nodo
        else:
            nodo.proximo = self.inicio
            self.inicio = nodo
        self.tamanho += 1

    def add_nodo_fim(self, valor):
        nodo = no(valor)
        if self.inicio == None:
            self.inicio = nodo
        else:
            aux = self.inicio
            while aux.proximo:
                aux = aux.proximo
            aux.proximo = nodo
        self.tamanho += 1

    def imprimir(self):
        if self.inicio == None:
            print("Lista Vazia !!!")
        else:
            aux = self.inicio
            while aux:
                print(aux.dado, end="\t")
                aux = aux.proximo

    def del_nodo_inicio(self):
        if self.inicio == None:
            print("Lista Vazia !!!")
        else:
            self.inicio = self.inicio.proximo
            self.tamanho -= 1

    def del_nodo_fim(self):
        if self.inicio == None:
            print("Lista Vazia !!!")
        else:
            ant = self.inicio
            aux = self.inicio.proximo
            while aux.proximo:
                ant = aux
                aux = aux.proximo
            ant.proximo = None
            self.tamanho -= 1