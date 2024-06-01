# Universidade Federal do Cariri
# Estrutura de Dados
# 2º semestre
# Gabriel Vasconcelos Andrade da Silva

import random

def gerar_matriz(linhas, colunas):
    # Gerando a matriz M com elementos aleatórios no intervalo [0, 1]
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            elemento = random.uniform(0, 1)  # Gera um número aleatório no intervalo [0, 1]
            linha.append(elemento)
        matriz.append(linha)
    return matriz

def verificar_matriz_nula(matriz):
    # Verificando se todos os elementos da matriz são zero
    for linha in matriz:
        for elemento in linha:
            if elemento != 0:
                return False
    return True

def main():
    # Solicitando ao usuário a quantidade de linhas e colunas
    linhas = int(input("Informe a quantidade de linhas da matriz: "))
    colunas = int(input("Informe a quantidade de colunas da matriz: "))

    # Gerando a matriz M
    matriz = gerar_matriz(linhas, colunas)

    # Exibindo a matriz gerada
    print("Matriz gerada:")
    for linha in matriz:
        print(linha)

    # Verificando se a matriz é nula
    if verificar_matriz_nula(matriz):
        print("A matriz é nula.")
    else:
        print("A matriz não é nula.")

# Executando o programa
if __name__ == "__main__":
    main()