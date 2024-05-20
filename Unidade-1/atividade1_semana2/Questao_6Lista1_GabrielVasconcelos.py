# Instituição: Universidade Federal do Cariri
# Disciplina: Estrutura de Dados
# Período: 2º Semestre
# Aluno: Gabriel Vasconcelos Andrade da Silva

class Pilha:
    def __init__(self):
        self.items = []

    def vazia(self):
        return self.items == []

    def empilhar(self, item):
        self.items.append(item)

    def desempilhar(self):
        return self.items.pop()

    def topo(self):
        return self.items[-1]

    def tamanho(self):
        return len(self.items)

def ordenar_pilha(pilha):
    pilha_aux = Pilha()

    while not pilha.vazia():
        temp = pilha.desempilhar()
        while not pilha_aux.vazia() and pilha_aux.topo() > temp:
            pilha.empilhar(pilha_aux.desempilhar())
        pilha_aux.empilhar(temp)

    # Copiando os elementos de volta para a pilha original
    while not pilha_aux.vazia():
        pilha.empilhar(pilha_aux.desempilhar())

# Caso de uso
pilha = Pilha()
pilha.empilhar(5)
pilha.empilhar(3)
pilha.empilhar(8)
pilha.empilhar(1)
pilha.empilhar(2)

print("Pilha antes de ordenar:", pilha.items)

ordenar_pilha(pilha)

print("Pilha depois de ordenar:", pilha.items)