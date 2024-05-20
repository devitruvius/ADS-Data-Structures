# Introdução a Python Com Aplicações de SO
# página 193 - Questões 1, 2 e 3.
# Questão 1

class Ingresso:
  def __init__(self, nome_evento, valor_ingresso):
    self.nome_evento = nome_evento
    self.valor_ingresso = valor_ingresso

  def exibirValor(self):
    return self.valor_ingresso

  def __str__(self):
    return f"{self.nome_evento}: R$ {self.valor_ingresso:.2f}"

# Programa para teste
ingresso1 = Ingresso("Show do Velho", 50.00)
ingresso2 = Ingresso("Show do Ave Sangria", 80.00)

print(ingresso1.exibirValor())
print(ingresso2.exibirValor())

print(ingresso1)
print(ingresso2)