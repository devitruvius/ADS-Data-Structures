# Instituição: Universidade Federal do Cariri
# Disciplina: Estrutura de Dados
# Período: 2º Semestre
# Aluno: Gabriel Vasconcelos Andrade da Silva

def main():
    vetor = []

    for i in range(10):
        num = int(input(f"Digite o {i+1}º número inteiro: "))
        vetor.append(num)

    valor_referencia = int(input("Digite o valor de referência inteiro: "))

    # a) Imprime os números do vetor maiores que o valor referência
    print("Números maiores que o valor de referência:")
    for num in vetor:
        if num > valor_referencia:
            print(num, end=" ")

    # b) Conta quantos números armazenados no vetor são menores que o valor de referência
    qtd_menores = sum(1 for num in vetor if num < valor_referencia)
    print("\nQuantidade de números menores que o valor de referência:", qtd_menores)

    # c) Conta quantas vezes o valor de referência aparece no vetor
    qtd_referencia = vetor.count(valor_referencia)
    print("Quantidade de vezes que o valor de referência aparece no vetor:", qtd_referencia)

if __name__ == "__main__":
    main()