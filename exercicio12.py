def filtrar_numeros_pares(lista_numeros):
    """
    Filtra uma lista de números, removendo aqueles que não são pares.
    lista_numeros: A lista de números a ser filtrada.
    Returna a lista contendo apenas os números pares.
    """
    return [numero for numero in lista_numeros if numero % 2 == 0]

# Exemplo de uso da função:
lista_numeros = [int(x) for x in input("Digite os números separados por espaço: ").split()]

lista_pares = filtrar_numeros_pares(lista_numeros)
print("Lista de números pares:")
print(lista_pares)
