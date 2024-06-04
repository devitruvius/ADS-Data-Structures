# Universidade Federal do Cariri
# Estrutura de Dados
# 2º semestre
# Gabriel Vasconcelos Andrade da Silva

fila = [1, 2, 3]  # Inicializa a lista fila com os elementos 1, 2 e 3

fila.append(4)  # Adiciona o elemento 4 ao final da lista fila

fila.pop(2)  # Remove o elemento na posição 2 (terceiro elemento, uma vez que a indexação começa em 0) da lista fila

fila.remove(1)  # Remove o primeiro elemento de valor 1 encontrado na lista fila

from collections import deque  # Importa a classe deque do módulo collections

fila = deque(['amarelo', 'azul', 'branco'])  # Inicializa o deque fila com os elementos 'amarelo', 'azul' e 'branco'

fila.append('vermelha')  # Adiciona o elemento 'vermelha' ao final do deque fila

fila.popleft()  # Remove e retorna o primeiro elemento do deque fila (primeiro que foi inserido), que é 'amarelo'