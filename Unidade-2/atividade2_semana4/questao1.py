# Universidade Federal do Cariri
# Estrutura de Dados
# 2º semestre
# Gabriel Vasconcelos Andrade da Silva

import numpy as np  # Importa a biblioteca NumPy para manipulação de arrays multidimensionais

class FilaCircular:

    def __init__(self, tamanhoVetor):  # Define o método de inicialização da classe com um parâmetro tamanhoVetor
        self.tamanhoVetor = tamanhoVetor  # Inicializa o atributo tamanhoVetor com o valor passado
        self.tamanhoVetor = 0  # Inicializa o tamanho do vetor como 0
        self.final = -1  # Inicializa o atributo final como -1
        self.numero_de_elementos = 0  # Inicializa o atributo numero_de_elementos como 0
        self.valores = np.empty(self.tamanhoVetor, dtype=int)  # Inicializa o vetor de valores com um vetor vazio de tamanho especificado e tipo inteiro

    def __fila_vazia(self):  # Define um método privado para verificar se a fila está vazia
        return self.numero_de_elementos == 0  # Retorna True se o número de elementos for igual a 0, indicando que a fila está vazia
    
    def __fila_cheia(self):  # Define um método privado para verificar se a fila está cheia
        return self.numero_de_elementos == self.tamanhoVetor  # Retorna True se o número de elementos for igual ao tamanho máximo da fila, indicando que a fila está cheia
    
    def enfileirar(self, valor):  # Define o método para enfileirar um valor na fila, com um parâmetro valor
        if self.__fila_cheia():  # Verifica se a fila está cheia
            print('A fila está cheia')  # Se a fila estiver cheia, imprime uma mensagem informando isso

        if self.final == self.tamanhoVetor -1:  # Verifica se o final da fila está no final do vetor
            self.final = -1  # Se estiver no final do vetor, reinicia o índice para -1 (para que o próximo valor seja adicionado no início do vetor)
        self.final += 1  # Incrementa o índice do final para indicar a próxima posição disponível
        self.valores[self.final] = valor  # Adiciona o valor na posição do final da fila
        self.numero_de_elementos += 1  # Incrementa o número de elementos na fila