def ordenar_por_tamanho(lista_palavras):
    """
    Ordena uma lista de palavras em ordem crescente de tamanho.
    lista_palavras: A lista de palavras a ser ordenada.
    Returna a lista de palavras ordenada por tamanho.
    """
    return sorted(lista_palavras, key=len)

# Exemplo de uso da função:
lista_palavras = input("Digite as palavras separadas por espaço: ").split()

lista_ordenada = ordenar_por_tamanho(lista_palavras)
print("Lista de palavras ordenadas por tamanho:")
print(lista_ordenada)
