# Universidade Federal do Cariri
# Disciplina: Estrutura de Dados
# Professor(a): Luís Fabrício de Freitas Souza
# Aluno(a): Gabriel Vasconcelos Andrade da Silva
# Título do Código: Algoritmo de ordenação Merge Sort para lista de inteiros
# Data Implementação: 27-06-2024 

# Função base
def merge_sort(arr):
    
    if len(arr) <= 1:   # Base da recursão: se a lista tiver um ou zero elementos, então já está ordenada
        return arr
    
    mid = len(arr) // 2 # Encontrando o meio da lista
    
    # Dividindo a lista em duas metades recursivamente
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    return merge(left_half, right_half) # Mesclando as duas metades ordenadas

def merge(left, right):
    sorted_list = []    # Lista que irá conter os elementos ordenados  
    i = j = 0           # Índices para percorrer as listas left e right
    
    # Mesclando as listas left e right enquanto houver elementos em ambas
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])     # Adiciona o menor elemento de left à lista ordenada
            i += 1
        else:
            sorted_list.append(right[j])    # Adiciona o menor elemento de right à lista ordenada
            j += 1
    
    sorted_list.extend(left[i:])    # Se houver, adiciona os elementos restantes de left
    
    sorted_list.extend(right[j:])   # Se houver, adiciona os elementos restantes de right
    
    # Retorna a lista mesclada e ordenada
    return sorted_list

# Desempenho em diferentes cenários:
# - Listas pequenas: Merge Sort é eficiente, mas o overhead constante pode torná-lo mais lento que algoritmos mais simples como Bubble Sort para listas muito pequenas.
# - Listas grandes: Merge Sort é muito eficiente e é a escolha de muitos sistemas robustos para ordenação estável devido à sua consistência e garantia de complexidade.