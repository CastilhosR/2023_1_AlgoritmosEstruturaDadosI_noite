from cPessoa import Fisica, Juridica
from cCidade import Cidade

c1 = Cidade("Porto Alegre", "RS")
c2 = Cidade("Curitiba", "PR")

pf1 = Fisica("João", "223314", c1, "12345678901")

pf2 = Fisica("Maria", "342789", c1, "10987654321")

pj1 = Juridica("Mercado do Zé", "987654", c2, "00123456000123" )

pj1.imprimir()

pj1.addFuncionario(pf1)
pj1.addFuncionario(pf2)

pj1.imprimir()

pf1.imprimir()
pf2.imprimir()

print("\n----------------x\n")
pj1.imprimir(tudo = False)

print("\n----------------xx\n")
pf2.imprimir()