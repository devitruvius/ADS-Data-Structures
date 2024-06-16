# Universidade Federal do Cariri
# Disciplina: Estrutura de Dados
# Professor: Luís Fabrício de Freitas Souza
# Aluno: Gabriel Vasconcelos Andrade da Silva
# Matrícula: 2023009898
# Data da Implementação: 16-06-2024

def selection_sort(arr):
    n = len(arr)  # Obtém o tamanho da lista
    for i in range(n - 1):  # Loop externo para percorrer até o penúltimo elemento
        # Encontrando o índice do menor elemento restante
        min_index = i  # Assume-se que o menor elemento é o primeiro não ordenado
        for j in range(i + 1, n):  # Loop interno para encontrar o índice do menor elemento
            if arr[j] < arr[min_index]:  # Se encontrar um elemento menor
                min_index = j  # Atualiza o índice do menor elemento
        
        # Trocando o menor elemento encontrado com o primeiro elemento não ordenado
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Troca os elementos de posição
        
        # Mostrando o estado da lista após cada passagem completa
        print(f"Passagem {i + 1}: {arr}")  # Imprimindo a lista após a passagem atual

# Lista inicial
arr = [29, 10, 14, 37, 13]
selection_sort(arr)