# Universidade Federal do Cariri
# Estrutura de Dados
# 2º semestre
# Gabriel Vasconcelos Andrade da Silva

import math

def calcular_media_geometrica(lista):
    # Encontrando o menor e o maior elemento da lista
    menor = min(lista)
    maior = max(lista)

    # Calculando a média geométrica entre o menor e o maior elemento
    media_geometrica = math.sqrt(menor * maior)
    return media_geometrica

def main():
    # Inicializando a lista
    L = []

    # Informando ao usuário para adicionar elementos à lista
    print("Preencha a lista L. Digite 'fim' para encerrar.")

    while True:
        # Solicitando os elementos ao usuário
        entrada = input("Digite um número (ou 'fim' para encerrar): ")

        # Verificando se o usuário deseja encerrar o preenchimento
        if entrada.lower() == 'fim':
            break

        try:
            # Convertendo a entrada para um número e adicionando à lista
            numero = float(entrada)
            L.append(numero)
        except ValueError:
            # Informando ao usuário se a entrada não é um número válido
            print("Entrada inválida. Por favor, digite um número.")

    # Verifica se a lista não está vazia
    if L:
        # Calculando a média geométrica entre o menor e o maior elemento
        media_geometrica = calcular_media_geometrica(L)
        # Imprimindo a média geométrica
        print(f"A média geométrica entre o menor e o maior elemento da lista é: {media_geometrica}")
    else:
        # Informando ao usuário que a lista está vazia
        print("A lista está vazia. Nenhum cálculo pode ser realizado.")

# Executando o programa
if __name__ == "__main__":
    main()