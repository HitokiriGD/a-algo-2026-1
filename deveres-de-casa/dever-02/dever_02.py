"""
Dever 02 - Fatorial Recursivo e Complexidade O(n)

Implementação recursiva do cálculo de fatorial,
medição de tempo de execução e análise assintótica.

Autor: Gabriel Diogo
Disciplina: Análise de Algoritmos
"""

import sys
import time


sys.setrecursionlimit(2000)


def fatorial(n):
    """
    Calcula o fatorial de um número usando recursão.

    Args:
        n (int): Número inteiro não negativo.

    Returns:
        int: Resultado do fatorial de n.
    """
    if n == 0 or n == 1:
        return 1

    return n * fatorial(n - 1)


def medir_tempo(n):
    """
    Mede o tempo de execução do cálculo fatorial.

    Args:
        n (int): Número para cálculo do fatorial.

    Returns:
        float: Tempo em segundos.
    """
    inicio = time.time()
    resultado = fatorial(n)
    fim = time.time()

    return resultado, fim - inicio


def main():
    """
    Executa cálculo manual e testes automáticos.
    """
    numero = int(input("Digite um número inteiro: "))

    resultado, tempo = medir_tempo(numero)

    print(f"Fatorial de {numero}: {resultado}")
    print(f"Tempo de execução: {tempo:.8f} segundos")
    print("-" * 40)

    valores = [10, 100, 500, 1000]

    print("Testes automáticos:")

    for n in valores:
        _, tempo_execucao = medir_tempo(n)

        print(f"n = {n}")
        print(f"Tempo: {tempo_execucao:.8f} segundos")
        print("-" * 40)

    print("Análise de complexidade:")
    print("A complexidade é O(n), pois há uma chamada recursiva para cada valor até 1.")


if __name__ == "__main__":
    main()
