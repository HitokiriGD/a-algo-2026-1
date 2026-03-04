"""
Dever 01 - Barreira do n²

Comparação empírica entre:
1. Insertion Sort (O(n²))
2. sorted() do Python (Timsort - O(n log n))

Autor: Gabriel Diogo
Disciplina: Análise de Algoritmos
"""

import random
import time


def insertion_sort(lista):
    """
    Ordena uma lista usando o algoritmo Insertion Sort.

    Args:
        lista (list): Lista de números a ser ordenada.

    Returns:
        list: Lista ordenada.
    """
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = chave

    return lista


def gerar_lista_aleatoria(tamanho):
    """
    Gera uma lista de números aleatórios.

    Args:
        tamanho (int): Quantidade de elementos.

    Returns:
        list: Lista com números aleatórios.
    """
    return [random.randint(0, 100000) for _ in range(tamanho)]


def medir_tempo_execucao(funcao, lista):
    """
    Mede o tempo de execução de uma função de ordenação.

    Args:
        funcao (callable): Função de ordenação.
        lista (list): Lista a ser ordenada.

    Returns:
        float: Tempo em segundos.
    """
    inicio = time.time()
    funcao(lista.copy())
    fim = time.time()

    return fim - inicio


def main():
    """
    Executa os testes comparando os algoritmos.
    """
    tamanhos = [1000, 5000, 10000, 20000, 50000]

    for n in tamanhos:
        lista = gerar_lista_aleatoria(n)

        tempo_insertion = medir_tempo_execucao(insertion_sort, lista)
        tempo_sorted = medir_tempo_execucao(sorted, lista)

        print(f"Tamanho da lista: {n}")
        print(f"Insertion Sort: {tempo_insertion:.6f} segundos")
        print(f"Sorted (Timsort): {tempo_sorted:.6f} segundos")
        print("-" * 40)


if __name__ == "__main__":
    main()
