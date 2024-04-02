def gerar_histograma(lista_numeros):
    """
    Gera um histograma a partir de uma lista de números.
    lista_numeros A lista de números para construir o histograma.
    """
    for numero in lista_numeros:
        histograma = '*' * numero
        print(histograma)

# Exemplo de uso da função:
lista_numeros = [int(x) for x in input("Digite os números separados por espaço: ").split()]

print("Histograma:")
gerar_histograma(lista_numeros)
