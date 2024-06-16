# Universidade Federal do Cariri
# Disciplina: Estrutura de Dados
# Professor: Luís Fabrício de Freitas Souza
# Aluno: Gabriel Vasconcelos Andrade da Silva
# Matrícula: 2023009898
# Data da Implementação: 16-06-2024

def insertion_sort(arr):
    for i in range(1, len(arr)): # Itera sobre os índices da lista a partir do segundo elemento até o final
        current = arr[i] # Armazena o valor do elemento atual em uma variável current
        j = i - 1  # Inicializa j como o índice anterior ao elemento atual

        # Enquanto j é maior ou igual a 0 e o valor atual é menor que o elemento na posição j
        while j >= 0 and current < arr[j]:
            
            arr[j + 1] = arr[j] # Move o elemento na posição j para a direita          
            j -= 1 # Decrementa j para comparar com o próximo elemento à esquerda

        # Insere o elemento atual na posição correta após o término do loop while
        arr[j + 1] = current
        # Imprime o estado da lista após cada inserção
        print(f"Inserção {i}: {arr} (elemento {current} inserido na posição correta)") 

# Lista inicial
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)