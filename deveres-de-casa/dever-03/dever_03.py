"""
Dever 03 - Verificar se um array é palíndromo usando recursão.

O programa permite que o usuário insira os valores manualmente.
A entrada pode ser:
- Números separados por espaço (ex: 1 2 3 2 1)
- Strings separadas por espaço (ex: a b c b a)
- Palavra contínua (ex: arara)
"""


def eh_palindromo(array, inicio=0, fim=None):
    """
    Verifica recursivamente se um array é palíndromo.

    A função compara os elementos das extremidades e avança
    em direção ao centro da lista.

    Args:
        array (list): Lista de elementos a ser verificada.
        inicio (int): Índice inicial da comparação.
        fim (int | None): Índice final da comparação.

    Returns:
        bool: True se for palíndromo, False caso contrário.
    """
    # Define o índice final na primeira chamada
    if fim is None:
        fim = len(array) - 1

    # Caso base: quando os índices se cruzam ou são iguais
    if inicio >= fim:
        return True

    # Se os elementos das extremidades forem diferentes, não é palíndromo
    if array[inicio] != array[fim]:
        return False

    # Chamada recursiva avançando para o centro
    return eh_palindromo(array, inicio + 1, fim - 1)


def processar_entrada(entrada):
    """
    Processa a entrada do usuário e converte para lista.

    Regras:
    - Se houver espaços → trata como lista
    - Se não houver espaços → trata como string (lista de caracteres)

    Args:
        entrada (str): Texto digitado pelo usuário.

    Returns:
        list: Lista de elementos (int ou str).
    """
    # Caso exista espaço, considera múltiplos elementos
    if " " in entrada:
        elementos = entrada.split()
        resultado = []

        for item in elementos:
            # Tenta converter para número
            try:
                resultado.append(int(item))
            except ValueError:
                resultado.append(item)

        return resultado

    # Caso seja uma string contínua, transforma em lista de caracteres
    return list(entrada)


def main():
    """
    Função principal do programa.

    Responsável por:
    - Receber entrada do usuário
    - Processar os dados
    - Exibir o resultado
    """
    entrada = input("Digite os elementos do array: ")

    array = processar_entrada(entrada)

    resultado = eh_palindromo(array)

    if resultado:
        print(f"{array} -> É palíndromo")
    else:
        print(f"{array} -> Não é palíndromo")


if __name__ == "__main__":
    main()
