# Instituição: Universidade Federal do Cariri
# Disciplina: Estrutura de Dados
# Período: 2º Semestre
# Aluno: Gabriel Vasconcelos Andrade da Silva

import numpy as np

class Pilha:
    # Construtor
    def __init__(self, tamanhoPilha):
        self.__tamanhoPilha = tamanhoPilha  # Define o tamanho máximo da pilha
        self.__topo = -1  # Inicializa o topo da pilha como -1, indicando que está vazia
        self.__valores = np.empty(self.__tamanhoPilha, dtype=int)  # Inicializa um array vazio com o tamanho especificado

    # Função que verifica se a pilha está cheia
    def __pilha_cheia(self):
        if self.__topo == self.__tamanhoPilha -1:  # Verifica se o topo está na última posição do array
            return True  # Retorna True se a pilha estiver cheia
        else:
            return False  # Retorna False se a pilha não estiver cheia

    # Função que verifica se a pilha está vazia
    def __pilha_vazia(self):
        if self.__topo == -1:  # Verifica se o topo está no índice inicial (-1), indicando que a pilha está vazia
            return True  # Retorna True se a pilha estiver vazia
        else:
            return False  # Retorna False se a pilha não estiver vazia

    # Método público para empilhar um valor na pilha
    def empilhar(self, valor):
        if self.__pilha_cheia():  # Verifica se a pilha está cheia
            print('A pilha está cheia!')  # Se estiver cheia, exibe uma mensagem
        else:
            self.__topo += 1  # Incrementa o topo
            self.__valores[self.__topo] == valor  # Adiciona o valor à posição do topo

    # Método público para desempilhar um valor da pilha
    def desempilhar(self):
        if self.__pilha_vazia():  # Verifica se a pilha está vazia
            print('A pilha está vazia!')  # Se estiver vazia, exibe uma mensagem
        else:
            self.__topo -= 1  # Decrementa o topo, removendo o último valor da pilha

    # Método para visualizar o topo da pilha
    def visualizar_topo(self):
        if self.__topo != -1:  # Verifica se a pilha não está vazia
            return self.__valores[self.__topo]  # Retorna o valor no topo da pilha
        else:
            return -1  # Retorna -1 se a pilha estiver vazia