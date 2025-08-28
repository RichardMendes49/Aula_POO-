'''Exercício 4  Classe Aluno
1. Crie uma classe chamada Aluno com:
○ Atributos: nome, notas (lista de floats).
○ Métodos:
■ adicionar_nota(valor) → adiciona uma nota à lista.
■ media() → retorna a média das notas.
■ situacao() → retorna &quot;Aprovado&quot; se média ≥ 7, senão
&quot;Reprovado&quot;.

2. Crie um objeto aluno com nome &quot;Maria&quot;.
○ Adicione as notas: 8.0, 6.5, 7.5.
○ Mostre a média e a situação final.'''

class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []  

    def adicionar_nota(self, valor):
        self.notas.append(valor)

    def media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)

    def situacao(self):
        if self.media() >= 7:
            return "Aprovado"
        else:
            return "Reprovado"


aluno1 = Aluno("anonimo")

aluno1.adicionar_nota(8.0)
aluno1.adicionar_nota(6.5)
aluno1.adicionar_nota(7.5)

print("Média:", aluno1.media())
print("Situação:", aluno1.situacao())
 