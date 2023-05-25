class no:
    def __init__(self, valor):
        self.dado = valor
        self.proximo = None

class lista_encadeada:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def add_nodo(self, valor):
        nodo = no(valor)
        if self.inicio is None or valor < self.inicio.dado:
            nodo.proximo = self.inicio
            self.inicio = nodo
        else:
            aux = self.inicio
            while aux.proximo and valor > aux.proximo.dado:
                aux = aux.proximo
            nodo.proximo = aux.proximo
            aux.proximo = nodo
        self.tamanho += 1


    def imprimir(self):
        if self.inicio is None:
            print("Lista Vazia !!!")
        else:
            aux = self.inicio
            while aux:
                print(aux.dado, end="\t")
                aux = aux.proximo

    def del_nodo_inicio(self):
        if self.inicio is None:
            print("Lista Vazia !!!")
        else:
            self.inicio = self.inicio.proximo
            self.tamanho -= 1

    def del_nodo_fim(self):
        if self.inicio is None:
            print("Lista Vazia !!!")
        else:
            ant = self.inicio
            aux = self.inicio.proximo
            while aux.proximo:
                ant = aux
                aux = aux.proximo
            ant.proximo = None
            self.tamanho -= 1


    def del_nodo_meio(self, valor):
        if self.inicio is None:
            print("Lista Vazia !!!")
        else:
            ant = None
            aux = self.inicio
            while aux:
                if aux.dado == valor:
                    if ant is None:
                        self.inicio = aux.proximo
                    else:
                        ant.proximo = aux.proximo
                    self.tamanho -= 1
                    return
                ant = aux
                aux = aux.proximo
            print("Nodo não encontrado na lista !!!")


