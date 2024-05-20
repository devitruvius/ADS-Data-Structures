# Instituição: Universidade Federal do Cariri
# Disciplina: Estrutura de Dados
# Período: 2º Semestre
# Aluno: Gabriel Vasconcelos Andrade da Silva

def calcular_media(vetor, tamanho):
    soma = sum(vetor)
    media = soma / tamanho
    return media

def main():
    tamanho = int(input("Digite o tamanho do vetor: "))

    vetor = []

    for i in range(tamanho):
        elemento = int(input(f"Digite o {i+1}º elemento: "))
        vetor.append(elemento)

    media = calcular_media(vetor, tamanho)

    print("A média dos elementos do vetor é:", media)

if __name__ == "__main__":
    main()