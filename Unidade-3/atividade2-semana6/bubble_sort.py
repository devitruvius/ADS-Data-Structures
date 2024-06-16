# Universidade Federal do Cariri
# Disciplina: Estrutura de Dados
# Professor: Luís Fabrício de Freitas Souza
# Aluno: Gabriel Vasconcelos Andrade da Silva
# Matrícula: 2023009898
# Data da Implementação: 16-06-2024

def bubble_sort(arr):
    n = len(arr)  # Obtém o tamanho da lista
    for i in range(n):  # Loop para cada passagem (até n passagens no máximo)
        swapped = False  # Flag para verificar se houve trocas nesta passagem
        for j in range(0, n-i-1):  # Loop para percorrer a lista até o último elemento não ordenado
            if arr[j] > arr[j+1]:  # Compara elementos adjacentes
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Troca os elementos se estiverem na ordem errada
                swapped = True  # Marca que ocorreu pelo menos uma troca nesta passagem
        print(f"Passagem {i+1}: {arr}")  # Mostra o estado atual da lista após cada passagem
        if not swapped:  # Se não houve trocas nesta passagem
            # Mostra a última passagem com a mensagem de término do algoritmo
            print(f"Passagem {i+2}: {arr} (nenhuma troca, algoritmo termina)")
            break  # Sai do loop principal, pois a lista já está ordenada

# Lista inicial
arr = [5, 1, 4, 2, 8]
bubble_sort(arr)