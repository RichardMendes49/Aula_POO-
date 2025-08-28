'''Exercício 3  Classe Retangulo
1. Crie uma classe chamada Retangulo com:
○ Atributos: largura, altura.
○ Métodos:
■ area() → retorna a área.

■ perimetro() → retorna o perímetro.

2. Crie um objeto representando um retângulo de largura 5 e altura 3.
○ Calcule e mostre a área.
○ Calcule e mostre o perímetro.'''

class Retangulo :

    def __init__ (self,largura,altura):
        self.largura = largura 
        self.altura = altura

    def area (self):
        return self.largura * self.altura

    def perimetro (self):
        return(self.largura + self.altura)*2
    

meu_retangulo = Retangulo(5, 3)
print("Área:", meu_retangulo.area())
print("Perímetro:", meu_retangulo.perimetro())
