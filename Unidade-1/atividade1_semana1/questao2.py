# Introdução a Python Com Aplicações de SO
# página 193 - Questões 1, 2 e 3.
# Questão 2

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcularPerimetro(self):
        return 2 * (self.largura + self.altura)

    def calcularArea(self):
        return self.largura * self.altura

# Código de teste
retangulo = Retangulo(5, 3)

perimetro = retangulo.calcularPerimetro()
print(f"Perímetro do retângulo: {perimetro}")

area = retangulo.calcularArea()
print(f"Área do retângulo: {area}")