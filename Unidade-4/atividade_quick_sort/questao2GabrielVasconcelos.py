# Universidade Federal do Cariri
# Disciplina: Estrutura de Dados
# Professor(a): Luís Fabrício de Freitas Souza
# Aluno(a): Gabriel Vasconcelos Andrade da Silva
# Título do Código: Algoritmo de ordenação Quick Sort para lista de strings
# Data Implementação: 27-06-2024 

# Definição da função quicksort para ordenar uma lista de strings em ordem alfabética
def quicksort(arr):
    
    if len(arr) <= 1:   # Caso base: Se a lista tiver 0 ou 1 elemento, retorna a própria lista
        return arr
    else:
        
        pivot = arr[len(arr) // 2]  # Escolhendo o elemento do meio como pivô
        
        # Particionando a lista em três partes: left (menores que o pivô), middle (iguais ao pivô) e right (maiores que o pivô)
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        
        # Ordenando recursivamente as partições left e right, e concatenando com middle para formar a lista ordenada
        return quicksort(left) + middle + quicksort(right)

# Desempenho em diferentes cenários:
# - Listas pequenas: Quick Sort é eficiente devido ao seu tempo médio de execução, embora em listas muito pequenas, o overhead de recursão possa torná-lo comparável a algoritmos mais simples como Bubble Sort.
# - Listas grandes: Quick Sort é muito eficiente devido ao seu tempo médio de execução, sendo preferido para ordenação rápida e eficiente em grandes conjuntos de dados.