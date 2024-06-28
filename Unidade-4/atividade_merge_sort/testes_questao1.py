import random
from questao1GabrielVasconcelos import merge_sort

# Testando a função com diferentes conjuntos de dados

def test_merge_sort():
    small_list = [38, 27, 43, 3, 9, 82, 10]
    sorted_small_list = merge_sort(small_list)
    print("Lista original:", small_list)
    print("Lista ordenada:", sorted_small_list)
    
    large_list = random.sample(range(1, 10001), 10000)
    sorted_large_list = merge_sort(large_list)
    print("Primeiros 10 elementos da lista original:", large_list[:10])
    print("Primeiros 10 elementos da lista ordenada:", sorted_large_list[:10])

if __name__ == "__main__":
    test_merge_sort()