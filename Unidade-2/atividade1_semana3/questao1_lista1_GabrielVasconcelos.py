# Universidade Federal do Cariri
# Estrutura de Dados
# 2º semestre
# Gabriel Vasconcelos Andrade da Silva

def gerar_pa(primeiro_termo, quantidade_termos, razao):
    # Listando os termos da PA
    termos = []
    
    # Gerando os termos
    for i in range(quantidade_termos):
        termo = primeiro_termo + i * razao
        termos.append(termo)
    
    return termos

def soma_pa(termos):
    # Calculando a soma dos termos
    return sum(termos)

# Solicitando ao usuário os parâmetros de entrada
primeiro_termo = float(input("Informe o primeiro termo da PA: "))
quantidade_termos = int(input("Informe a quantidade de termos da PA: "))
razao = float(input("Informe a razão da PA: "))

# Termos da PA
termos_pa = gerar_pa(primeiro_termo, quantidade_termos, razao)

# Soma dos termos
soma_dos_termos = soma_pa(termos_pa)

# Exibindo os termos e a soma dos termos da PA
print("Os termos da PA são:", termos_pa)
print("A soma dos termos da PA é:", soma_dos_termos)