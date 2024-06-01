# Universidade Federal do Cariri
# Estrutura de Dados
# 2º semestre
# Gabriel Vasconcelos Andrade da Silva

# Função para modificar origem e/ou destino de um voo
def modificar_voo(voos):
    num_voo = input("Digite o número do voo que deseja modificar: ")
    if num_voo in voos:
        nova_origem = input("Digite a nova origem do voo {}: ".format(num_voo))
        novo_destino = input("Digite o novo destino do voo {}: ".format(num_voo))
        voos[num_voo] = (nova_origem, novo_destino)
        print("Voo {} modificado com sucesso!".format(num_voo))
    else:
        print("Voo {} não encontrado.".format(num_voo))

# Função principal
def main():
    # Dicionário para armazenar os voos com origens e destinos
    voos = {}
    
    # Solicitando ao usuário que insira os dados dos voos
    num_voos = int(input("Digite o número de voos: "))
    for i in range(num_voos):
        num_voo = input("Digite o número do voo {}: ".format(i+1))
        origem = input("Digite a origem do voo {}: ".format(num_voo))
        destino = input("Digite o destino do voo {}: ".format(num_voo))
        voos[num_voo] = (origem, destino)
    
    # Chamando a função para modificar um voo, se desejado
    modificar = input("Deseja modificar algum voo? (s/n): ")
    if modificar.lower() == 's':
        modificar_voo(voos)
    
    # Imprimindo a nova listagem de voos
    print("\nNova listagem de voos:")
    for num_voo, (origem, destino) in voos.items():
        print("Voo {}: Origem - {}, Destino - {}".format(num_voo, origem, destino))

# Chamando a função principal
if __name__ == "__main__":
    main()