from cVeiculos import bicicleta, carro, moto

bici1 = bicicleta(bagageiro = True, marca="Caloi", modelo="Cross")


moto1 = moto(marca="Honda", modelo="Titan")

carro1 = carro(marca="Ford", modelo="Cobalt")

bici1.imprimirinfo()
bici1.acelerar(10)
bici1.imprimirinfo()
bici1.acelerar(10)
bici1.imprimirinfo()
bici1.acelerar(10)
bici1.imprimirinfo()
bici1.frear(30)
bici1.imprimirinfo()
bici1.frear(30)
bici1.imprimirinfo()
bici1.frear(10)
bici1.imprimirinfo()

# moto1.imprimirinfo()

# carro1.imprimirinfo()