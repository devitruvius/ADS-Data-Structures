# Introdução a Python Com Aplicações de SO
# página 193 - Questões 1, 2 e 3.
# Questão 3

from ponto import Ponto

def ler_pontos():
    pontos = []
    while True:
        entrada = input("Digite o nome, x e y do ponto separados por espaço (ou 'sair' para terminar): ")
        if entrada.lower() == 'sair':
            break
        try:
            nome, x, y = entrada.split()
            x = int(x)
            y = int(y)
            ponto = Ponto(nome, x, y)
            pontos.append(ponto)
        except ValueError:
            print("Entrada inválida. Certifique-se de digitar o nome, x e y corretamente separados por espaço.")
    return pontos

def main():
    pontos = ler_pontos()
    for ponto in pontos:
        print(ponto)

if __name__ == "__main__":
    main()
