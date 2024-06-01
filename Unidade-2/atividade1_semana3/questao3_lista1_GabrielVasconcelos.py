# Universidade Federal do Cariri
# Estrutura de Dados
# 2º semestre
# Gabriel Vasconcelos Andrade da Silva

import random

def cadastrar_participantes():
    # Listando os nomes dos participantes
    participantes = []

    while True:
        # Solicitando o nome
        nome = input("Digite o nome do participante (ou 'sair' para encerrar): ")
        
        # Verificando se o usuário deseja encerrar o processo
        if nome.lower() == 'sair':
            break

        # Adicionando o nome do participante à lista
        participantes.append(nome)

    return participantes

def sortear_ganhador(participantes):
    # Escolhendo aleatoriamente um participante da lista
    ganhador = random.choice(participantes)
    return ganhador

# Função principal do programa
def main():
    print("Cadastro de Participantes da Rifa")

    # Cadastro dos participantes
    participantes = cadastrar_participantes()

    # Verificando os participantes cadastrados
    if participantes:
        # Realiza o sorteio
        ganhador = sortear_ganhador(participantes)
        # Exibe o nome do ganhador
        print(f"O ganhador da rifa é: {ganhador}")
    else:
        print("Nenhum participante foi cadastrado.")

# Executando o programa
if __name__ == "__main__":
    main()