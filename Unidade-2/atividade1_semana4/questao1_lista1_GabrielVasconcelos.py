# Universidade Federal do Cariri
# Estrutura de Dados
# 2º semestre
# Gabriel Vasconcelos Andrade da Silva

# Definindo a função para criar o relatório ordenado
def gerar_relatorio(clientes):
    # Ordenando os clientes com base no valor total de compras (segundo elemento da tupla)
    clientes_ordenados = sorted(clientes.items(), key=lambda x: x[1], reverse=True)
    
    # Imprimindo o cabeçalho do relatório
    print("Relatório de Clientes Potenciais:")
    print("{:<30} {:>15}".format("Razão Social", "Valor Total de Compras"))
    print("-" * 45)
    
    # Imprimindo os clientes ordenados
    for cliente, valor_compras in clientes_ordenados:
        print("{:<30} R$ {:>15.2f}".format(cliente, valor_compras))

# Função principal
def main():
    # Dicionário para armazenar os clientes e seus valores totais de compras
    clientes = {}
    
    # Solicitando ao usuário que insira os dados dos clientes
    num_clientes = int(input("Digite o número de clientes: "))
    for i in range(num_clientes):
        razao_social = input("Digite a razão social do cliente {}: ".format(i+1))
        valor_compras = float(input("Digite o valor total de compras do cliente {}: R$ ".format(i+1)))
        clientes[razao_social] = valor_compras
    
    # Chamando a função para gerar o relatório ordenado
    gerar_relatorio(clientes)

# Chamando a função principal
if __name__ == "__main__":
    main()