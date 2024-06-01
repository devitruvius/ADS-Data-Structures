# Universidade Federal do Cariri
# Estrutura de Dados
# 2º semestre
# Gabriel Vasconcelos Andrade da Silva

import requests  # Biblioteca para fazer requisições HTTP

# Dicionário para armazenar dados das séries (a ser preenchido)
series_data = {}

# Função para buscar informações de uma série na API
def buscar_serie(nome_serie):
  """
  # Busca informações de uma série em uma suposta API e retorna um dicionário com os dados da série.

  Argumentos:
    nome_serie (str): Nome da série a ser pesquisada.

  Retorno:
    dict: Dicionário com os dados da série, ou None se a série não for encontrada.
  """
  url = "https://api.example.com/series/" + nome_serie.replace(" ", "+")  # Substitui espaços por "+"
  response = requests.get(url)

  if response.status_code == 200:
    dados_serie = response.json()
    return dados_serie
  else:
    return None

# Função para encontrar os atores principais de uma série
def encontrar_atores_principais(nome_serie):
  """
  Encontra os atores principais de uma série com base nos dados da suposta API.

  Argumentos:
    nome_serie (str): Nome da série a ser pesquisada.

  Retorno:
    list: Lista com os nomes dos atores principais, ou None se a série não for encontrada.
  """
  dados_serie = buscar_serie(nome_serie)

  if dados_serie:
    atores_principais = dados_serie.get("atores_principais", [])
    return atores_principais
  else:
    return None

# Função principal
def main():
  while True:
    nome_serie = input("Digite o nome da série: ")

    atores_principais = encontrar_atores_principais(nome_serie)

    if atores_principais:
      print("Atores principais de", nome_serie + ":")
      for ator in atores_principais:
        print(" -", ator)
    else:
      print("Série não encontrada.")

    continuar = input("Deseja buscar outra série? (s/n): ")
    if continuar.lower() != 's':
      break

# Chamando a função principal
if __name__ == "__main__":
  main()