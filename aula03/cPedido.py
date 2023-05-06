from cProduto import Produto
from cPessoa  import Pessoa

class Pedido:
    def __init__(self, cliente=Pessoa(), endereco="Rua Lá", id=None):
        self.id = id
        self.cliente = cliente
        self.endereco = endereco
        self.produtos = []
        self.total = 0.0

    def imprimir(self):
        pass

    def calcTotal(self):
        self.total = 0.0
        if len(self.produtos) > 0:
            for x in self.produtos:
                self.total += x.preco

    def addProduto(self, produto=Produto() ):
        self.produtos.append(produto)
        self.total += produto.preco # * produto.quant

    def getTotal(self):
        return self.total

    def mostraPedido(self):
        print("Dados do Pedido:")
        print("Cliente:", self.cliente.nome)
        print("Endereço de entrega: ", self.endereco)
        print("Cidade:", self.cliente.city.nome+" - "+self.cliente.city.uf)
        print("Fone:", self.cliente.fone)

    def mostraProdutos(self):
        print("Produtos:")
        if len ( self.produtos ) == 0:
            print("----------------------------------------")
            print("Pedido Vazio !")
        else:
            for x in self.produtos:
                print("----------------------------------------")
                print("Produto: ", x.nome)
                print("Preço: ", x.preco)
                print("Categoria: ", x.categoria.nome, "\n")

