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

    def excluir_inicio_lista(self):  # Define o método para excluir o primeiro nó da lista.
        if self.primeiroLista.proximo == None:  # Verifica se a lista está vazia.
            print('Lista vazia')  # Exibe uma mensagem indicando que a lista está vazia.
            return None  # Retorna None, pois não há nenhum nó para ser removido.

        temporaria = self.primeiroLista  # Armazena o primeiro nó em uma variável temporária.

        self.primeiroLista = self.primeiroLista.proximo  # Atualiza o primeiro nó para ser o próximo da lista.
        return temporaria  # Retorna o nó removido.
    
    def pesquisar(self, valor):  # Define o método para pesquisar um valor na lista.
        if self.primeiroLista == None:  # Verifica se a lista está vazia.
            print('Lista Vazia')  # Exibe uma mensagem indicando que a lista está vazia.
            return None  # Retorna None, pois não há nós na lista para pesquisar.

        atual = self.primeiroLista  # Inicia a variável 'atual' no primeiro nó da lista.
        while atual.valor != valor:  # Itera sobre a lista até encontrar o nó com o valor especificado.
            if atual.proximo == None:  # Verifica se chegou ao final da lista sem encontrar o valor.
                return None  # Retorna None, indicando que o valor não foi encontrado.
            else: 
                atual = atual.proximo  # Move para o próximo nó na lista.
        return atual  # Retorna o nó com o valor especificado.