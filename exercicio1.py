import random

def contar_numeros_positivos(lista):
    """ Conta quantos números positivos estão presentes em uma lista.
    lista: Uma lista de números inteiros.
    retorna o número de números positivos na lista.
    """
    contador = 0
    for numero in lista:
        if numero > 0:
            contador += 1
    return contador

# Gera uma lista de números aleatórios
lista_numeros = [random.randint(-10, 10) for _ in range(20)]

# Conta os números positivos na lista
quantidade_positivos = contar_numeros_positivos(lista_numeros)

print("Lista de números:", lista_numeros)
print("Quantidade de números positivos:", quantidade_positivos)
