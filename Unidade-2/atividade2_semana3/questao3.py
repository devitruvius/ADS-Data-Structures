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

    def inserir_Inicio(self, valor):  # Define o método para inserir um novo nó no início da lista.
        novo = No(valor)  # Cria um novo nó com o valor fornecido.
        novo.proximo = self.primeiroLista  # Define o próximo do novo nó como o atual primeiro nó da lista.
        self.primeiroLista = novo  # Atualiza o primeiro nó da lista para ser o novo nó criado.

    def mostrar(self):  # Define o método para mostrar todos os nós da lista.
        atual = self.primeiroLista  # Inicia a variável 'atual' no primeiro nó da lista.
        while atual != None:  # Enquanto não atingir o final da lista (quando 'atual' for None).
            atual.mostrar_No()  # Mostra o valor do nó atual.
            atual = atual.proximo  # Move para o próximo nó na lista.