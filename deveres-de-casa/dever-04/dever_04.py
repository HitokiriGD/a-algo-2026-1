"""
Dever 04
"""

import math


def F(n):
    """
    Função recursiva que calcula F(n)

    Passo 1: caso base
    Se n == 1, retorna 2
    """

    if n == 1:
        return 2

    """
    chamada recursiva
    Assume que F(n-1) já está correto

    constrói solução atual
    F(n) = 2 * F(n-1) + n²
    """
    return 2 * F(n - 1) + n**2


def main():
    """
    Função principal:
    - recebe n do usuário
    - calcula F(n)
    """

    n = int(input("Digite o valor de n: "))

    if n < 1:
        print("n deve ser >= 1")
        return

    resultado = F(n)

    print(f"F({n}) = {resultado}")


if __name__ == "__main__":
    main()
