from cCidade import Cidade
from cPessoa import Pessoa
from cCategoria import Categoria
from cProduto import Produto
from cPedido import Pedido

c1 = Cidade("Porto Alegre", "RS")
p1 = Pessoa("Rodrigo", "+55 51 99259.3360", c1)

print("\nA cidade de ", p1.nome, " é: ", p1.city.nome, "/", p1.city.uf, "\n")

p1.imprimir()

print("\n-----------------------\n")

cat1 = Categoria("Bebidas")
cat2 = Categoria("Alimento")

prod1 = Produto("Coca Cola", 12.0, cat1)
prod2 = Produto("Feijao", 8.0, cat2 )
prod3 = Produto("Pepsi", 5.0, cat1)

ped1 = Pedido(cliente=p1, endereco="Rua tal")

ped1.addProduto(prod1)
ped1.addProduto(prod2)
ped1.addProduto((prod3))

ped1.mostraPedido()

ped1.mostraProdutos()

print("Total do pedido: ", ped1.total)

print("Total do pedido metodo 2: ", ped1.getTotal())