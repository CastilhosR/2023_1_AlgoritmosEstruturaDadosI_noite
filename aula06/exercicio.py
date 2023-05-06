from cAluno import AlunoEnsinoMedio, AlunoGraduacao

aem1 = AlunoEnsinoMedio("Adaltinho", "123456", 7)
aem2 = AlunoEnsinoMedio("Adaltao", 123456, 9)

ag1 = AlunoGraduacao("Rodriguinho", "987654", 6)
ag2 = AlunoGraduacao("Rodrigao", 987654, 3)

aem1.imprimir()
aem2.imprimir()
print("--------------")
ag1.imprimir()
ag2.imprimir()
