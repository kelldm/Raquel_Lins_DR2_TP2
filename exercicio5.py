def gerar_quadrados():
    """
    Gera uma lista dos quadrados dos números de 1 a 20.
    retorna uma lista dos quadrados dos números de 1 a 20.
    """
    lista_quadrados = []
    for numero in range(1, 21):
        quadrado = numero ** 2
        lista_quadrados.append(quadrado)
    return lista_quadrados

# Chama a função para gerar a lista
lista_de_quadrados = gerar_quadrados()

# printa a lista
print("Lista dos quadrados dos números de 1 a 20:")
print(lista_de_quadrados)
