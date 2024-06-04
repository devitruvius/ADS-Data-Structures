# Universidade Federal do Cariri
# Estrutura de Dados
# 2º semestre
# Gabriel Vasconcelos Andrade da Silva

import numpy as np  # Importa a biblioteca NumPy para trabalhar com arrays multidimensionais.

class No:
    def __init__ (self, valor):  # Define o método de inicialização da classe No, que recebe um parâmetro 'valor'.
        self.valor = valor  # Atribui o valor recebido ao atributo 'valor' do objeto.
        self.proximo = None  # Inicializa o atributo 'proximo' como None, indicando que inicialmente não há próximo nó.

    def mostrar_No(self):  # Define o método para mostrar o valor do nó.
        print(self.valor)  # Imprime o valor do nó.

class lista_Encadeada:  # Define a classe lista_Encadeada para representar a lista encadeada.
    def __init__(self):  # Define o método de inicialização da classe lista_Encadeada.
        self.primeiroLista = None  # Inicializa o atributo 'primeiroLista' como None, indicando que a lista está vazia no início.