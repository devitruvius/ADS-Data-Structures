# Universidade Federal do Cariri
# Disciplina: Estrutura de Dados
# Professor: Luís Fabrício de Freitas Souza
# Aluno: Gabriel Vasconcelos Andrade da Silva
# Matrícula: 2023009898
# Data da Implementação: 16-06-2024

class No:
    def __init__(self, chave):  # Define o construtor da classe No
        self.chave = chave      # Atribui a chave ao nó
        self.esq = None         # Inicializa o filho esquerdo como None
        self.dir = None         # Inicializa o filho direito como None

class Arvore:
    def __init__(self):         # Define o construtor da classe Arvore
        self.raiz = None        # Inicializa a raiz como None
        self.cont_espaco = 10   # Define a quantidade de espaços para formatação da impressão

    def inserir(self, chave: int) -> None:              # Método para inserir uma chave na árvore
        if self.raiz is None:                           # Se a raiz é None, a árvore está vazia
            self.raiz = No(chave)                       # Cria um novo nó como raiz
        else:                                           # Caso contrário, insere recursivamente
            self._inserir_recursivo(self.raiz, chave)   # Chama o método recursivo para inserir a chave

    def _inserir_recursivo(self, atual: No, chave: int) -> No:      # Método recursivo para inserir a chave
        if atual is None:                                           # Se o nó atual é None, encontrou o local para inserir
            return No(chave)                                        # Retorna um novo nó com a chave
        if chave <= atual.chave:                                    # Se a chave é menor ou igual à chave do nó atual
            atual.esq = self._inserir_recursivo(atual.esq, chave)   # Insere na subárvore esquerda
        else:                                                       # Caso contrário, a chave é maior
            atual.dir = self._inserir_recursivo(atual.dir, chave)   # Insere na subárvore direita
        return atual                                                # Retorna o nó atual

    def imprimir_arvore(self, raiz=None, espaco=0) -> None:     # Método para imprimir a árvore
        if raiz is None:                                        # Se o nó raiz é None, retorna (condição de parada)
            return
        espaco += self.cont_espaco                              # Incrementa o espaço para formatação
        self.imprimir_arvore(raiz.dir, espaco)                  # Chama recursivamente para imprimir a subárvore direita
        print(' ' * (espaco - self.cont_espaco), end='')        # Imprime os espaços
        print(raiz.chave)                                       # Imprime a chave do nó atual
        self.imprimir_arvore(raiz.esq, espaco)                  # Chama recursivamente para imprimir a subárvore esquerda

if __name__ == '__main__':                                  # Bloco que executa se o script for executado diretamente
    lista = [115, 98, 34, 56, 25, 95, 25, 132, 130, 133]    # Lista de chaves para inserir na árvore
    arvore = Arvore()                                       # Cria uma nova árvore
    for i in lista:                                         # Para cada chave na lista
        arvore.inserir(i)                                   # Insere a chave na árvore
    arvore.imprimir_arvore(arvore.raiz)                     # Imprime a estrutura da árvore a partir da raiz