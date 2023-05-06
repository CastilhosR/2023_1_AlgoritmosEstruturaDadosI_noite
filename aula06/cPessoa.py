from cCidade import Cidade

class Pessoa:
    def __init__(self, nome="Fulano", fone="xxx", city=Cidade(), id=None ):
        self.id = id
        self.nome = nome
        self.fone = fone
        self.city = city

    def imprimir(self, label="Nome: "):
        print(label, self.nome)
        print("Fone: ", self.fone)
        print("Cidade: ", self.city.nome, "/", self.city.uf)

class Juridica(Pessoa):
    def __init__(self, nome, fone, cidade, cnpj = None):
        super().__init__(nome, fone, cidade)
        self.cnpj = cnpj
        self.funcionarios = []

    def addFuncionario(self, funcionario = None ):
        self.funcionarios.append(funcionario)
        funcionario.empresa = (self)

    def imprimir(self, tudo = True):
        super().imprimir(label="Empresa: ")
        if tudo:
            print("CNPJ: ", self.cnpj)
            print("---------------")
            if len(self.funcionarios) == 0:
                print("Não possui funcionários")
            else:
                for f in self.funcionarios:
                    print("Funcionário: ", f.nome, f.cpf, f.city.nome, "/", f.city.uf)
            print("---------------\n")

class Fisica(Pessoa):
    def __init__(self, nome, fone, cidade, cpf = None, empresa = None ):
        super().__init__(nome, fone, cidade)
        self.cpf = cpf
        self.empresa = empresa

    def imprimir(self):
        print("Pessoa: ", self.nome, self.fone, self.city.nome, "/", self.city.uf, ' - ', self.empresa.nome)

