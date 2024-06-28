from questao2GabrielVasconcelos import quicksort

# Função para testar o algoritmo com diferentes conjuntos de dados
def test_quicksort():
    # Conjuntos de dados de teste (listas de strings desordenadas)
    test_cases = [
        ["banana", "apple", "cherry", "date"],
        ["hello", "world", "python", "programming"],
        ["a", "c", "b", "e", "d"],
        ["zebra", "monkey", "ant", "lion", "elephant"],
        ["quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    ]
    
    # Iterando sobre cada caso de teste
    for i, case in enumerate(test_cases):
        # Ordenando a lista usando quicksort
        sorted_case = quicksort(case)
        
        # Verificando se a lista está ordenada corretamente
        assert sorted_case == sorted(case), f"Erro no Teste Case {i + 1}: Esperado {sorted(case)}, obtido {sorted_case}"

        # Imprime os resultados dos testes
        print(f"Test Case {i + 1}:")
        print("Original:", case)
        print("Sorted:", sorted_case)
        print("-" * 40)

# Chama a função de teste
if __name__ == "__main__":
    test_quicksort()