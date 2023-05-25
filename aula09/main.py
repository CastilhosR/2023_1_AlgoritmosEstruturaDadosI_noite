# from cLista_Encadeada import lista_encadeada
# from teste import lista_encadeada
from teste2 import lista_dupla_encadeada
import random

valores = [48,46,23,50,47,29,35,32,41]

lista = lista_dupla_encadeada()

lista.imprimir()

# for x in range(1, 10, 1):
#     y = random.randint(20,50)
#     lista.add_nodo_inicio(y)
#     # lista.add_nodo_fim(y+100)
#     print(y, end="\t")

for x in valores:
    lista.add_nodo(x)
    print(x, end="\t")

print()

lista.imprimir()
print()
lista.del_nodo_fim()

print()

lista.imprimir()

lista.del_nodo_inicio()
print()

lista.imprimir()

lista.del_nodo_meio(41)

print()

lista.imprimir()
