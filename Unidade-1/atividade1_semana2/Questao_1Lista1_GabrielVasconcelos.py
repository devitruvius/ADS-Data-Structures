# Instituição: Universidade Federal do Cariri
# Disciplina: Estrutura de Dados
# Período: 2º Semestre
# Aluno: Gabriel Vasconcelos Andrade da Silva

import numpy as np

class VetorNaoOrdenado:
    # Método construtor da classe VetorNaoOrdenado
    def __init__(self, tamanhoVetor):
        # Inicializa a propriedade tamanhoVetor com o valor passado ao criar o objeto
        self.tamanhoVetor = tamanhoVetor
        # Inicializa a última posição com -1, indicando que o vetor está vazio
        self.ultima_posicao = -1
        # Cria um array numpy de tamanho tamanhoVetor, com valores inteiros não inicializados

        self.valores = np.empty(self.tamanhoVetor, dtype=int)
        # A função np.empty aloca espaço na memória para o array, mas não inicializa os valores

    # Função Imprimir
    def imprimir(self):
        # Define um método chamado 'imprimir' na classe que recebe a instância atual 'self'

        if self.ultima_posicao == -1:
            # Verifica se 'ultima_posicao' é -1, o que indica que o vetor está vazio

            print("Vetor está vazio")
            # Se o vetor estiver vazio, imprime a mensagem "Vetor está vazio"

        else:
            # Se o vetor não estiver vazio, executa o bloco abaixo

            for i in range(self.ultima_posicao + 1):
                # Percorre um intervalo de 0 até 'ultima_posicao' inclusivo

                print(i, "-", self.valores[i])
                # Para cada índice 'i', imprime o índice seguido do valor correspondente no vetor

    # Função Inserir Elementos
    def inserir(self, valor):
        # Verifica se a última posição no vetor está no limite máximo.
        if self.ultima_posicao == self.tamanhoVetor - 1:
            # Se a última posição está no limite máximo, imprime uma mensagem informando que o tamanho máximo do vetor foi atingido.
            print("Tamanho máximo do vetor foi atingido")
        else:
            # Caso contrário, incrementa a posição atual e insere o valor na próxima posição disponível no vetor.
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor

# Função Pesquisar
    def pesquisar(self, valor):
        # Inicia a busca pelo valor fornecido dentro da lista/array da instância da classe.

        for i in range(self.ultima_posicao + 1):
            # Itera sobre cada índice da lista/array até a última posição preenchida (ultima_posicao).

            if valor == self.valores[i]:
                # Compara o valor procurado (valor) com o elemento na posição atual (self.valores[i]).

                return i
                # Se encontrar uma correspondência, retorna o índice da posição onde o valor foi encontrado.

        return -1
        # Se percorrer toda a lista/array e não encontrar o valor, retorna -1 indicando que o valor não foi encontrado.

# Função Excluir

    def excluir(self, valor):
        # Encontra a posição do valor a ser excluído
        posicao = self.pesquisar(valor)
        # Se o valor não foi encontrado, retorna -1
        if posicao == -1:
            return -1
        else:
            # Move os valores à direita do valor a ser excluído uma posição para a esquerda
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            # Atualiza a última posição válida na lista
            self.ultima_posicao -= 1

vetor = VetorNaoOrdenado(7)