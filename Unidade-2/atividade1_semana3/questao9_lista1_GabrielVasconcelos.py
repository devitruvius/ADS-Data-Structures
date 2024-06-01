# Universidade Federal do Cariri
# Estrutura de Dados
# 2º semestre
# Gabriel Vasconcelos Andrade da Silva

import random

def gerar_matriz(linhas, colunas):
    # Gerando a matriz M com elementos aleatórios no intervalo [0, 10]
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            elemento = random.randint(0, 10)  # Gera um número aleatório no intervalo [0, 10]
            linha.append(elemento)
        matriz.append(linha)
    return matriz

def verificar_matriz_diagonal(matriz):
    # Verificando se a matriz é diagonal
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i != j and matriz[i][j] != 0:
                return False
    return True

def main():
    # Solicitando ao usuário a quantidade de linhas e colunas
    linhas = int(input("Informe a quantidade de linhas da matriz: "))
    colunas = int(input("Informe a quantidade de colunas da matriz: "))

    # Verificando se a matriz pode ser diagonal
    if linhas != colunas:
        print("Para ser uma matriz diagonal, a matriz deve ser quadrada (mesmo número de linhas e colunas).")
        return

    # Gerando a matriz M
    matriz = gerar_matriz(linhas, colunas)

    # Exibindo a matriz gerada
    print("Matriz gerada:")
    for linha in matriz:
        print(linha)

    # Verificando se a matriz é diagonal
    if verificar_matriz_diagonal(matriz):
        print("A matriz é diagonal.")
    else:
        print("A matriz não é diagonal.")

# Executando o programa
if __name__ == "__main__":
    main()