# Universidade Federal do Cariri
# Estrutura de Dados
# 2º semestre
# Gabriel Vasconcelos Andrade da Silva

# Dicionário para armazenar os dados da tabela
dados = {
    "1": {"matricula": 1, "nome": "Ana", "sexo": "F", "departamento": "TI", "tempo_servico": 7, "salario": 3200.00},
    "2": {"matricula": 2, "nome": "Beatriz", "sexo": "F", "departamento": "TI", "tempo_servico": 4, "salario": 3720.00},
    "3": {"matricula": 3, "nome": "Carla", "sexo": "F", "departamento": "TI", "tempo_servico": 1, "salario": 2100.00},
    "4": {"matricula": 4, "nome": "Daniela", "sexo": "F", "departamento": "RH", "tempo_servico": 2, "salario": 3920.00},
    "5": {"matricula": 5, "nome": "Emílio", "sexo": "M", "departamento": "RH", "tempo_servico": 7, "salario": 4235.12},
    "6": {"matricula": 6, "nome": "Fernando", "sexo": "M", "departamento": "Marketing", "tempo_servico": 7, "salario": 1200.00},
    "7": {"matricula": 7, "nome": "Gabriela", "sexo": "F", "departamento": "Marketing", "tempo_servico": 8, "salario": 7234.89},
    "8": {"matricula": 8, "nome": "Hernandes", "sexo": "M", "departamento": "TI", "tempo_servico": 6, "salario": 4234.12},
    "9": {"matricula": 9, "nome": "Ítalo", "sexo": "M", "departamento": "RH", "tempo_servico": 13, "salario": 13934.23},
    "10": {"matricula": 10, "nome": "Janaína", "sexo": "F", "departamento": "RH", "tempo_servico": 7, "salario": 9341.89},
}

# Lista para armazenar os nomes das mulheres do setor de TI com salário acima de R$ 3.000,00
mulheres_ti_acima_3000 = []

# Iterando sobre os dados do dicionário
for matricula, dados_funcionario in dados.items():
    # Verificando se o funcionário é mulher, do setor de TI e tem salário acima de R$ 3.000,00
    if dados_funcionario["sexo"] == "F" and dados_funcionario["departamento"] == "TI" and dados_funcionario["salario"] > 3000.00:
        # Adicionando o nome da funcionária à lista
        mulheres_ti_acima_3000.append(dados_funcionario["nome"])

# Imprimindo a listagem de mulheres do setor de TI com salário acima de R$ 3.000,00
print("Mulheres do setor de TI com salário acima de R$ 3.000,00:")
for nome in mulheres_ti_acima_3000:
    print(f"- {nome}")