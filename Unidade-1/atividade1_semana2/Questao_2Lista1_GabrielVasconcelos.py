# Instituição: Universidade Federal do Cariri
# Disciplina: Estrutura de Dados
# Período: 2º Semestre
# Aluno: Gabriel Vasconcelos Andrade da Silva

import numpy as np

class VetorOrdenado:

    def __init__(self, tamanhoVetor):
        self.tamanhoVetor = tamanhoVetor  # Define o tamanho do vetor
        self.ultima_posicao = -1  # Inicializa a última posição como -1, indicando que o vetor está vazio
        self.valores = np.empty(self.tamanhoVetor, dtype=int)  # Cria um array vazio de tamanho definido

    # Função Imprimir
    def imprimir(self):
        if self.ultima_posicao == -1:  # Verifica se o vetor está vazio
            print('Vetor está vazio')  # Imprime uma mensagem informando que o vetor está vazio
        else:
            for i in range(self.ultima_posicao + 1):  # Itera sobre o vetor até a última posição preenchida
                print(i, '-', self.valores[i])  # Imprime o índice e o valor do elemento naquela posição

    # Função Inserir
    def inserir(self, valor):
        if self.ultima_posicao == self.tamanhoVetor - 1:  # Verifica se o vetor está cheio
            print(
                'Tamanho do vetor foi atingido com capacidade máxima')  # Imprime uma mensagem informando que o vetor está cheio
            return

        posicao = 0  # Inicializa a posição onde o elemento será inserido
        for i in range(self.ultima_posicao + 1):  # Itera sobre o vetor até a última posição preenchida
            posicao = i  # Atualiza a posição onde o elemento será inserido
            if self.valores[i] > valor:  # Verifica se o valor na posição atual é maior que o valor a ser inserido
                break
            if i == self.ultima_posicao:  # Verifica se chegou ao final do vetor
                posicao = i + 1  # Atualiza a posição onde o elemento será inserido

        y = self.ultima_posicao  # Inicializa um índice auxiliar para realocar os elementos do vetor
        while y >= posicao:  # Enquanto houver elementos a serem deslocados
            self.valores[y + 1] = self.valores[y]  # Desloca o elemento para a próxima posição
            y -= 1  # Atualiza o índice auxiliar

        self.valores[posicao] = valor  # Insere o valor na posição correta
        self.ultima_posicao += 1  # Atualiza a última posição preenchida do vetor

    # Função Pesquisar
    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):  # Itera sobre o vetor até a última posição preenchida
            if self.valores[i] > valor:  # Verifica se o valor na posição atual é maior que o valor procurado
                return -1  # Retorna -1, indicando que o valor não foi encontrado
            if self.valores[i] == valor:  # Verifica se o valor na posição atual é igual ao valor procurado
                return i  # Retorna o índice onde o valor foi encontrado
            if i == self.ultima_posicao:  # Verifica se chegou ao final do vetor
                return -1  # Retorna -1, indicando que o valor não foi encontrado

    # Função Excluir
    def excluir(self, valor):
        posicao = self.pesquisar(valor)  # Pesquisa a posição do valor a ser excluído
        if posicao == -1:  # Verifica se o valor não foi encontrado
            return -1  # Retorna -1, indicando que o valor não foi encontrado
        else:
            for i in range(posicao,
                           self.ultima_posicao):  # Itera sobre o vetor a partir da posição onde o valor foi encontrado
                self.valores[i] = self.valores[i + 1]  # Move os elementos uma posição para trás
            self.ultima_posicao -= 1  # Atualiza a última posição preenchida do vetor
