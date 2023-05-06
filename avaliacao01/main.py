from cComputador import Desktop, Notebook

d1 = Desktop()
n1 = Notebook()
print(d1.getInformacoes())
print(n1.getInformacoes())

print("-"*50)

d1.cadastrar(modelo="dell", cor="verde", preco=100, potenciaDaFonte=250)
n1.cadastrar(modelo="acer", cor='azul', preco=200, tempoDeBateria=8)

print(d1.getInformacoes())
print(n1.getInformacoes())

