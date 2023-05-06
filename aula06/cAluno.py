class Aluno:
    def __init__(self, nome = None, matricula = None, codigo = None):
        self.codigo = codigo
        self.nome = nome
        self.matricula = matricula

    def imprimir(self):
        print("Nome: ", self.nome)
        print("Matricula: ", self.matricula)

class AlunoEnsinoMedio(Aluno):
    def __init__(self, nome = None, matricula = None, ano = None):
        super().__init__(nome, matricula)
        self.ano = ano

    def imprimir(self):
        super().imprimir()
        print("Ano: ", self.ano)

class AlunoGraduacao(Aluno):
    def __init__(self, nome = None, matricula = None, semestre = None):
        super().__init__(nome, matricula)
        self.semestre = semestre

    def imprimir(self):
        super().imprimir()
        print("Semestre: ", self.semestre)
