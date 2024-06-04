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

    def desenfileirar(self):  # Define o método para desenfileirar um elemento da fila

        if self.__fila_vazia():  # Verifica se a fila está vazia
            print('A fila se encontra vazia')  # Se a fila estiver vazia, imprime uma mensagem informando isso
            return  # Retorna imediatamente se a fila estiver vazia, sem fazer mais nada
        
        temporaria = self.valores[self.inicio]  # Armazena temporariamente o valor a ser removido, que está na posição do início da fila
        self.inicio += 1  # Move o índice de início para a próxima posição na fila
        if self.inicio == self.tamanhoVetor:  # Verifica se o índice de início atingiu o final do vetor
            self.inicio = 0  # Se o índice de início estiver no final do vetor, reinicia-o para o início do vetor
            self.numero_de_elementos -= 1  # Decrementa o número de elementos na fila
        return temporaria  # Retorna o valor removido da fila
    
    def primeiroFila(self):  # Define o método para obter o primeiro elemento da fila

        if self.__fila_vazia():  # Verifica se a fila está vazia
            return -1  # Retorna -1 se a fila estiver vazia, indicando que não há nenhum elemento na fila
        
        return self.valores[self.inicio]  # Retorna o valor na posição do início da fila, que é o primeiro elemento da fila