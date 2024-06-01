# Universidade Federal do Cariri
# Estrutura de Dados
# 2º semestre
# Gabriel Vasconcelos Andrade da Silva

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
    
    # Contando a quantidade de voos com origem em Natal
    qtd_voos_natal = sum(1 for origem, _ in voos.values() if origem.lower() == 'natal')
    
    # Imprimindo a quantidade de voos com origem em Natal
    print("Quantidade de voos com origem em Natal: ", qtd_voos_natal)

# Chamando a função principal
if __name__ == "__main__":
    main()